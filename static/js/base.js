/*funciones base*/

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

jQuery.fn.resetValidation = function() {
    var el = "#" + this[0].id;
    var formArray = $(this[0]).serializeArray();
    for (var i = 0; i < formArray.length; i++){
        $(el + " input[name=" + formArray[i]['name'] +"]").removeClass('is-invalid');
        $(el + " select[name=" + formArray[i]['name'] +"]").removeClass('is-invalid');
        $(el + " textarea[name=" + formArray[i]['name'] +"]").removeClass('is-invalid');
    }
};

jQuery.fn.validateFromJSON = function(responseJSON) {
    var el = this[0].id;
    $.each(responseJSON, function( index, value ) {
        $("#" + el + " input[name=" + index +"]").addClass("is-invalid");
        $("#" + el + " select[name=" + index +"]").addClass("is-invalid");
        $("#" + el + " textarea[name=" + index +"]").addClass("is-invalid");
        $("#" + el + " input[name=" + index +"]").next().html(value);
        $("#" + el + " select[name=" + index +"]").next().html(value);
        $("#" + el + " textarea[name=" + index +"]").next().html(value);
    });
};
