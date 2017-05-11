
function updateDate(newVal) {

    var newUrl = $.query.set("date", newVal).toString();

    location.href = newUrl;
}

function showDateAt() {
    updateDate($("#datechooser").val());
}

$(document).ready(function(){
    $('#datechooser').datepicker({
      "dateFormat":"yy-mm-dd",
      showButtonPanel: false
    }).on("change", function(){
        updateDate($(this).val());
    });
} );