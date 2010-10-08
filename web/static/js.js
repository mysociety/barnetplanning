var map;

$(function(){

    if ($('#map').length) {
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 12,
            center: new google.maps.LatLng(51.652963, -0.2005),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
    }

    $('#id_postcode').change(function(){
        var val = $(this).val();
        $.ajax({
            url: 'http://mapit.mysociety.org/postcode/' + encodeURIComponent(val),
            dataType: 'jsonp',
            success: function(data) {
                hide_error('#id_postcode');
                if (data['error']) {
                    if (data['code'] == 400) {
                        show_error('#id_postcode', "That doesn't appear to be a valid postcode, sorry.");
                    } else if (data['code'] == 404) {
                        show_error('#id_postcode', "Sorry, we couldn't find that postcode.");
                    }
                    return;
                }
                if (data['shortcuts']['council'] != 2489) {
                    show_error('#id_postcode', "That postcode doesn't appear to be within Barnet, sorry.");
                    return;
                }
                if (!map) return;
                map.setCenter(new google.maps.LatLng(data['wgs84_lat'], data['wgs84_lon']));
                map.setZoom(14);
                $("input[name='radius']:checked").click();
            },
            error: function(xhr) {
            }
        });
    });
    if ($('#id_postcode').val()) {
        $('#id_postcode').change();
    }

    $("input[name='radius']").click(function(){
        var radius = $(this).val();
        if (!map) return;
        createCircle(map.getCenter(), radius);
        if (radius>1000 && map.getZoom() > 13) {
            map.setZoom(13);
        }
        if (radius<500 && map.getZoom() < 14) {
            map.setZoom(14);
        }
    });

    $('#alert_form').submit(function(){
        var go = true;
        if (!$('#id_email').val()) {
            show_error('#id_email', 'Please enter your email address.');
            go = false;
        }
        if (!$('#id_postcode').val()) {
            show_error('#id_postcode', 'Please enter a postcode.');
            go = false;
        }
        return go;
    });
});

var circle;
function createCircle(c, radius) {
    if (circle) {
        circle.setCenter(c);
        circle.setRadius(parseInt(radius));
    } else {
        circle = new google.maps.Circle({
            map: map,
            center: c,
            radius: parseInt(radius),
            fillColor: '#ee9900',
            strokeColor: '#ee9900',
            strokeWeight: 1
        });
    }
}

function show_error(id, text) {
    $(id).parent().before("<ul class='errorlist'><li>" + text + "</li></ul>");
}

function hide_error(id) {
    $(id).parent().prev('ul.errorlist').remove();
}

