function clearError() {
    $("#error").text( "" );
}
function addError(msg){
    var oldText=$("#error").text();
    $("#error").text( oldText + msg);
}

function cipherDict(key,dict) {

    var bDict = {};



    for (var key in dict) {

        var bKey = btoa(key);
        var bData = btoa(dict[key]);

        bKey  = bKey;
        bData = bData;
        bDict[bKey] = bData;
    }

    return bDict;

}

function webTimestamp() {
    clearError();
    $("#timestamp").prop('disabled', true);

    var devKey = Cookies.get("DEV_KEY");
    if (devKey === undefined )  {
        addError("Supercookie expired!, ask support te retrive it");
        return;
    }

    navigator.geolocation.getCurrentPosition(function(position) {
           var latitude = position.coords.latitude;

           var longitude = position.coords.longitude;

           data = cipherDict(devKey.substring(0,16),{
                deviceData:navigator.userAgent,
                longitude:longitude,
                latitude:latitude,
                time:Date.now(),
                devKey:devKey,
                timezone:Intl.DateTimeFormat().resolvedOptions().timeZone
           });


           $.ajax({
            method:"POST",
            data:data,
            url:"/api/timesheet/new/",
            success:function(data) {
                $("#timestamp").prop('disabled', false);
                if ( data.code > 0 ) {
                    addError(data.status);
                } else {
                    addError("Success!");
                }
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
    if ( ! navigator.geolocation && ! ( window.btoa && window.atob) ) {
        addError("Your browser doesnt meet requirement.");
        $("#timestamp").prop('disabled','true');
    }
});