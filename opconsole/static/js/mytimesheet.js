
function updateDate(newVal) {

    var newUrl = $.query.set("date", newVal).toString();

    location.href = newUrl;
}

function showDateAt() {
    updateDate($("#datechooser").val());
}

function initMyTimeSheetJS() {

    $('#datechooser').datepicker({
      "dateFormat":"yy-mm-dd",

      showButtonPanel: false
    }).on("change", function(){
        updateDate($(this).val());
    });

    $("#dialog-form").dialog({
        modal: true,
        height: "auto",
        width: 400,
        title:"Manual timestamp",
        autoOpen:false,
        buttons: {
        "Ask approval": function() {
            $.post("/api/timestamp/modification/",
            {
                "id":$("#userId").val(),
                "timezone":Intl.DateTimeFormat().resolvedOptions().timeZone,
                "time": Date.parse(
                    $("#manualDate").val() + " " + $("#time").val()
                 ),
                "action":"manual"
            },function(em) {
                $( "#dialog-form" ).dialog( "close" );
                location.reload();
            },location.reload()
            );


        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });
    $("#dialog-form").hide();
}

$( document ).ready(function() {
            initWebTimestampJS();
            initMyTimeSheetJS();
});