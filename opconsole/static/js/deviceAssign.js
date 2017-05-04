function getAssignedZone() {
    var zonesId = [];
    $(".zone").each(function( index, element ) {
        zones.append( $(element).attr("id")) );
    });


}
$(document).ready(function(){

    getAssignedZone();
})