function setURL(parm, val) {
      url = location.href;
      if ( url.indexOf("?") === -1 ) {
            location.href = url + "?" + parm + '='+ val;
        } else {
            if ( url.indexOf(param) === -1 ) {
                location.href += "&" + parm + '='+ val;
            } else {

                posParm = url.indexOf(param) + parm.length + 1;

            }
        }
}


function showDateAt() {
    setURL( "date", $("#datechooser").val());
}

$(document).ready(function(){
    $('#datechooser').datepicker({
      "dateFormat":"yy-mm-dd",
      showButtonPanel: false
    }).on("change", function(){
        setURL("date", $(this).val());
    });
} );