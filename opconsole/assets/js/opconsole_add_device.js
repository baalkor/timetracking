function getEmployeeId() {
    return $("#employeeId").val();
}

function initDevice() {
    data =  {
        tempCode:$("#code").val(),
        deviceData:navigator.userAgent,
        timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,
        serial:"undef",
        employeeId:getEmployeeId(),
        deviceId:$("#devId").val(),
        phoneNumber:"",
        name:$("#name").val()
    };

    $.ajax({
        method:"POST",
        url:"/api/device/init/",
        data:data,
        success:function(data) {
            Cookies.set("DEV_KEY",  data.devKey  );

            location.replace("/devices/" + data.id);
        }
    }).fail(function(){
        $("#error").text("Error check code");
    });
}

function requestWebCode() {

    $.get("/api/device/init/?typeId=1&employeeId=" + getEmployeeId() , function(data) {
        $("#broswerCode").show();
        $("#btnReqCode").prop('disabled', true);
        $("#lblCode").text ( data.tempCode ) ;
        $("#devId").val(data.id);
        $("#initDate").val(data.initDate);
    });
}

function showFormForType() {
   var typeId = $("#devType").val();
   if ( typeId != -1 ) {
        $(".formWizard").hide();
        $("#" + typeId).show();
   }
}
