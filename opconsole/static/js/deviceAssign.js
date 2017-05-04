function getDevId() { return $("#devId").val(); }
function getAssignedZone() {
    var zonesId = [];
    var devId = getDevId();
    $(".zone").each(function( index, element ) {
        checkIfIsLinked($(element).prop("id"),this);
    });
}


function checkIfIsLinked(zoneId, element) {
    $.ajax({
        method:"GET",
        url:"/api/device/assigned/",
        data:{devId:getDevId(),zoneId:zoneId},
        success:function(data) {
          $(element).attr("checked", data.assigned );
          if ( data.assigned ) {
              $('#txtAssign_' + zoneId).text("un-assign");
          } else {
            $('#txtAssign_' + zoneId).text("Assign");
          }
        }
    }).fail(function(error){
        $("#error").text(error.message);
    });
}
function toggle(zoneId, element) {
    $.ajax({
        method:"GET",
        url:"/api/device/assigned/",
        data:{devId:getDevId(),zoneId:zoneId},
        success:function(data){ toggleAssigment(zoneId,element,!data.assigned);}
    }).fail(function(error){
        $("#error").text(error.message);
    });
}
function toggleAssigment(zoneId,element,val) {

    if (val) {
        url = "/api/device/assign/";
    } else {
        url = "/api/device/unassign/";
    }
    console.log(url);
    $.ajax({
        method:"POST",
        url:url,
        data:{devId:getDevId(),zoneId:zoneId},
        success:function(data) {
            location.reload();
        }
    }).fail(function(error){
        $("#error").text(error.message);
    });
}

$(document).ready(function(){
    getAssignedZone();
    setUpCSRFHeader();

})