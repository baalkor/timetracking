function clearError() {
    $("#error").text( "" );
}
function addError(msg){
    var oldText=$("#error").text();
    $("#error").text( oldText + msg);
}

function webTimestamp() {
    clearError();
    $("#timestamp").prop('disabled', true);
    var devKey = Cookies.get("DEV_KEY");

    navigator.geolocation.getCurrentPosition(function(position) {
           var latitude = position.coords.latitude;
           var longitude = position.coords.longitude;
           data = {
            longitude:longitude,
            latitude:latitude,
            time:Date.now(),
            devKey:devKey
           }

           $.ajax({
            method:"POST",
            url:"/api/timesheet/new/",
            success:function() {
                console.log("Sent timestamp sucessfuly!");
            }
           }).fail(function(error){
                addError(error.message);
           })


    }, function(error) {
        if (error.code == error.PERMISSION_DENIED) {
            addError("You declined, could not process, try reloading the page");
            $("#timestamp").prop('disabled', false);
         } else {
            addError(error.message);
         }
    });

}

$(document).ready(function(){
    setUpCSRFHeader();
    if ( ! navigator.geolocation) {
        addError("Your browser doesnt support geolocation.");
    }
});