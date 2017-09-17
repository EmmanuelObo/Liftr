function getLocation() {
  console.log("entered!")
    if (navigator.geolocation) {
      console.log(navigator.geolocation.getCurrentPosition(storePosition));

    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function storePosition(position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
    send_ajax(lat,long);
}

function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
}

function send_ajax() {
    $.ajax({
            type: 'POST',
            url: "/coordinates/",
            data: {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    latitude: lat,
                    longitude: long },
            dataType: 'json',
            success: function() {
              console.log("Succes");
            },
            error: function(error) {
              console.log(error);
            }});
}
