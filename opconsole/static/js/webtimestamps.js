function addError(msg){
    var oldText=$("#error").text();
    $("#error").text( oldText + msg);
}
function webTimestamp() {
    $("#timestamp").prop('disabled', true);
    devKey = Cookies.get("DEV_KEY");
    if ( devKey.length != 63 ) {
        addError("Supercookie correctly set. Ask support team to download it.")
    }
}

$(document).ready(function(){
    setUpCSRFHeader();
});