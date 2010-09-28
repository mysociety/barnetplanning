$(function(){

    if ($('#map').length) {
        var map = new OpenLayers.Map('map');
        var layer = new OpenLayers.Layer.OSM('OS StreetView', 'http://os.openstreetmap.org/sv/${z}/${x}/${y}.png', {
            minZoomLevel: 6,
            maxZoomLevel: 18
        });
        map.addLayer(layer);
        map.setCenter(new OpenLayers.LonLat(-0.2005, 51.652963).transform(
            new OpenLayers.Projection("EPSG:4326"),
            new OpenLayers.Projection("EPSG:900913")
        ), 12);
    }

    $('#id_postcode').change(function(){
        var val = $(this).val();
        $.getJSON('http://mapit.mysociety.org/postcode/' + encodeURIComponent(val) + '?callback=?',  function(data){
            map.setCenter(new OpenLayers.LonLat(data['wgs84_lon'], data['wgs84_lat']).transform(
                new OpenLayers.Projection("EPSG:4326"),
                new OpenLayers.Projection("EPSG:900913")
            ), 15);
        });
    });

    $("input[@name='radius']").click(function(){
    });

});
