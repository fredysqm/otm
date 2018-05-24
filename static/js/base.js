/*funciones base*/
(function($) {
    var ajaxQueue = $({});
    $.ajaxQueue = function(ajaxOpts) {
        var oldComplete = ajaxOpts.complete;
        ajaxQueue.queue(function(next) {
            ajaxOpts.complete = function() {
                if (oldComplete) oldComplete.apply(this, arguments);
                next();
            };
            $.ajax(ajaxOpts);
        });
    };
})(jQuery);

jQuery.fn.csrfSafeMethod = function(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

jQuery.fn.getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

jQuery.fn.getJSONdata = function() {
    var formArray = $(this[0]).serializeArray();
    var returnArray = {};
    
    for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
    }

    return JSON.stringify ( returnArray );
};

jQuery.fn.fillItems = function(url_data, param_key, param_value) {
    var el = this[0];
    $.ajaxQueue({
        type: "GET",
        url: url_data,
        success: function(data) {
            $(el).empty();
            $(el).append('<option value="">---</option>');
            $.each(data.results, function (key, value) {
                $(el).append('<option value=' + value[param_key] + '>' + value[param_value] + '</option>');
            });
        }
    });
};

jQuery.fn.fillForm = function(url_data) {
    var el = this[0];
    $.ajaxQueue({
        type: "GET",
        url: url_data,
        success: function(data) {
            $.each(data, function (key, value) {
                $(el).find("[name=" + key + "]").val(value);
            });
        }
    });
};

jQuery.fn.resetValidation = function() {
    var el = this[0];
    var formArray = $(el).serializeArray();
    for (var i = 0; i < formArray.length; i++){
        $(el).find("[name=" + formArray[i]["name"] + "]").removeClass("is-invalid");
    }
};

jQuery.fn.validateFromJSON = function(responseJSON) {
    var el = this[0];
    $.each(responseJSON, function( index, value ) {
        $(el).find("[name=" + index + "]").addClass("is-invalid");
        $(el).find("[name=" + index + "]").next().html(value);
    });
};
