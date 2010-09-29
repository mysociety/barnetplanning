$(function(){

    if ($('#map').length) {
        var map = new OpenLayers.Map('map');
        var osLayer = new OpenLayers.Layer.OSM('OS StreetView', 'http://os.openstreetmap.org/sv/${z}/${x}/${y}.png', {
            attribution: 'Map hosted by <a href="http://openstreetmap.org/">OpenStreetMap</a>. Contains Ordnance Survey data &copy; Crown copyright and database right 2010',
            minZoomLevel: 9,
            maxZoomLevel: 16,
            numZoomLevels: null
        });
        polygonLayer = new OpenLayers.Layer.Vector('Polygon Layer');
        map.addLayers([osLayer, polygonLayer]);
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
            $("input[name='radius']:checked").click();
        });
    });

    $("input[name='radius']").click(function(){
        var radius = $(this).val();
        createCircle(map.center.lon, map.center.lat, radius);
        if (radius>1000 && map.zoom > 14) {
            map.zoomTo(14);
        }
        if (radius<500 && map.zoom < 15) {
            map.zoomTo(15);
        }
    });

});

function createCircle(x, y, radius) {
    var point = new OpenLayers.Geometry.Point(x, y);
    var circle = OpenLayers.Geometry.Polygon.createRegularPolygon(point, radius, 50);
    var feature = new OpenLayers.Feature.Vector(circle);
    polygonLayer.removeAllFeatures();
    polygonLayer.addFeatures([feature]);
}

