
$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};
    updater.poll();
});


var utils = {
    isJson: function (item) {
        item = typeof item !== "string" ? JSON.stringify(item) : item;
        try {
            item = JSON.parse(item);
        } catch (e) {
            return false;
        }
        return typeof item === "object" && item !== null;
    }

}


var recorder = {
    // register record click function when add record
    recordClickEvent: function (e) {
        if($(this).hasClass("active")){
            console.log('already active');
            return;
        }
        $("#requestList .list-group-item.active").removeClass("active");
        this.classList.add("active");
        const requestId = $(this).attr('id');
        recorder.recordClickCallback(requestId)
    },

    // retrieve record detail when click record
    recordClickCallback: function (request_id) {
        $.ajax({
            url: "/inspect/http/" + request_id,
            type: "GET",
            contentType: "application/json;charset=utf-8",
            dataType: "json",
            success: function (response) {
                const record = response.data;
                $("#recordDetail").html(record.detail);
                // have request body
                if (!_.isEmpty(record.request.data)) {
                    var requestData = record.request.data;
                    if (utils.isJson(requestData)){
                        new PrettyJSON.view.Node({
                            el: $('#requestBodyContent'),
                            data: JSON.parse(requestData),
                            dateFormat: "YYYY-MM-DD HH24:MI:SS",
                        });
                    }else {
                        $('#requestBodyContent').html("<pre><code>" + requestData + "</code></pre>");
                    }
                }
                // have response body
                if (!_.isEmpty(record.response.data)){
                    var responseData = record.response.data;
                    if (utils.isJson(responseData)){
                        new PrettyJSON.view.Node({
                            el: $('#responseBodyContent'),
                            data: JSON.parse(responseData),
                            dateFormat: "YYYY-MM-DD HH24:MI:SS",
                        });
                    }else{
                        $('#responseBodyContent').html("<pre>" + responseData + "</pre>");
                    }
                }
            },
            error: function(response) {
                // Failed to retrieve detail of request_id
                console.log('Failed to retrieve detail of request_id');
            },
        })
    },

    // do replay on server
    replayRequest: function (record) {
        $.ajax({
            url: '/inspect/http/' + record.request_id,
            type: 'POST',
            contentType: 'application/json;charset=utf-8;',
            // timeout: 1000 * 10,  // 10 seconds
            success: function (response) {
                console.log('success');
                console.log(response);
            },
            error: function(response) {
                console.log('Failed to replay request: ', response);
            },
        })
    },

    // replayFromBrowser
    // replayRequestV2: function (record) {
    //     const queries = $.param(record.request.queries, true)
    //     $.ajax({
    //         url: queries ? (record.path + '?' + queries): record.path,
    //         type: record.method,
    //         headers: record.request.headers,
    //         contentType: record.request.headers['Content-Type'],
    //         data: record.request.data,
    //         // timeout: 1000 * 10,  // 10 seconds
    //         success: function (response) {
    //             console.log('success');
    //             console.log(response);
    //         },
    //         error: function(response) {
    //             console.log('Failed to replay request: ', response);
    //         },
    //     })
    // },

    // clear all records
    clearRecords: function (){
        $.ajax({
            url: "/inspect/http",
            type: "DELETE",
            contentType: "application/json;charset=utf-8",
            dataType: "json",
            success: function (response) {
                $("#recordDetail>*").remove();
                $("#requestList>.record").remove();
                console.log('clear all records!');
            },
            error: function(response) {
                console.log('Failed to clear records.', response);
            },
        })
    },
}


var updater = {  // update records
    errorSleepTime: 500,  // ms
    lastRequestID: null,
    limitation: 0, // number of records to display

    poll: function() {
        const data = {};
        if (updater.lastRequestID) data.last_request_id = updater.lastRequestID;
        $.ajax({
            url: "/inspect/http/live",
            type: "POST",
            contentType: "application/json;charset=utf-8",
            dataType: "json",
            data: JSON.stringify(data),
            success: updater.onSuccess,
            error: updater.onError
        });
    },

    onSuccess: function(response) {
        try {
            updater.newRecords(response);
        } catch (e) {
            console.log('Wrong Response Body!', e)
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newRecords: function(response) {
        if (!response.data) return;
        var records = response.data;
        updater.limitation = response.limit || 0;
        updater.lastRequestID = records[records.length - 1].request_id;
        for (var i = 0; i < records.length; i++) {
            const record = records[i];
            const existing = $("#" + record.request_id);
            if (existing.length > 0) return;
            const ele = $(record.html);
            ele.click(recorder.recordClickEvent) // register click event
            $("#requestList").prepend(ele);
            $("#requestList>span:gt(" + (updater.limitation - 1).toString(10) + ")").remove();
        }
    },
};