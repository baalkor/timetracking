function getEmployeeId() {
    return $("#employeeId").val();
}

function getWebOSData() {
    console.log(navigator)
}



function requestWebCode() {

    $.get("/api/device/init/?typeId=1&employeeId=" + getEmployeeId() , function(data) {
        $("#broswerCode").show();
        $("#lblCode").text ( data.tempCode ) ;
    });
}

function showFormForType() {
   var typeId = $("#devType").val();
   if ( typeId != -1 ) {
        $(".formWizard").hide();
        $("#" + typeId).show();
   }
}
$(document).ready(function() {$(".formWizard").hide();});