function send_login() {
    $.ajax({
            type: 'POST',
            url: "/user_login/",
            data: {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    username: $('#username').val(),
                    password: $('#inputPassword').val() },
            dataType: 'json',
            success: function() {
              console.log("Succes");
            },
            error: function(error) {
              console.log(error);
            }});
}
