
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

String.prototype.toHHMMSS = function () {
    var sec_num = parseInt(this, 10); // don't forget the second param
    var hours   = Math.floor(sec_num / 3600);
    var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
    var seconds = sec_num - (hours * 3600) - (minutes * 60);

    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}
    return hours+':'+minutes+':'+seconds;
}


function computeDuration() {

    $(".time").each(function(index,elem){
        console.log(index);
        if ( index % 2 !== 0 ) {
            e_date =  Date.parse($(this).text());
            diff = e_date - s_date;
            $(this).parent().next($('.duration')).text((diff / 1000).toString().toHHMMSS());
        } else {
            s_date =  Date.parse($(this).text());
        }
    });

}