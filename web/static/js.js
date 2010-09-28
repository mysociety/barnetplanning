$(function(){

    $('#id_postcode').change(function(){
        var val = $(this).val();
        $.getJSON('http://mapit.mysociety.org/postcode/' + encodeURIComponent(val) + '?callback=?',  function(data){
            alert(data['wgs84_lat']);
        });
    });

    $("input[@name='radius']").click(function(){
    });

});
