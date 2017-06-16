function updateDate(newVal) {
    var newUrl = $.query.set("date", newVal).toString();
    location.href = newUrl;
}

function showDateAt() {
    updateDate($("#datechooser").val());
}

function initMyTimeSheetJS() {
    $("date").datepicker({
      format:'yyyy-mm-dd'
    });
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


function sendabsenceRequest(userid) {
    var absense_data = {};
    $(".absence-data").each(function(index, element ) {
        absense_data[element.id] = element.value;
    });
    absense_data["userid"] = userid;
    absense_data['type'] = $('input[name=optabsences]:checked').val()
    $.ajax({
	    url:"/api/absences/add/",
	    method:"POST",
	    data:absense_data
   }).then(function(success){
	console.log("Request sent");
   }).catch(function(failure){
	console.log("Failure request sent");
   });
}
