$(function(){

    if ($('#map').length) {
        var map = new OpenLayers.Map('map');
        var layer = new OpenLayers.Layer.OSM('OS StreetView', 'http://os.openstreetmap.org/sv/${z}/${x}/${y}.png');
        map.addLayer(layer);
        map.zoomToMaxExtent();
    }

    $('#id_postcode').change(function(){
        var val = $(this).val();
        $.getJSON('http://mapit.mysociety.org/postcode/' + encodeURIComponent(val) + '?callback=?',  function(data){
            alert(data['wgs84_lat']);
        });
    });

    $("input[@name='radius']").click(function(){
    });

});
