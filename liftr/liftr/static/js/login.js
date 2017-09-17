function send_login() {
var csrftoken = getCookie('csrftoken')
    $.ajax({
            type: 'POST',
            url: "/user_login/",
            data: {
                    csrfmiddlewaretoken: csrftoken,
                    username: $('#username').val(),
                    password: $('#inputPassword').val() },
            dataType: 'json',
            success: function() {
              console.log("Succes");
            },
            error: function(err) {
              console.log(err);
            }});
}

    function getCookie(name)
    {
        var cookieValue = null;
        if (document.cookie && document.cookie != '')
        {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++)
            {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '='))
                    {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
            }
        }
        return cookieValue;
    }
