$(document).ready(function(){
    $('#datechooser').datepicker({
      "dateFormat":"yy-mm-dd",
      showButtonPanel: false
    }).on("change", function(){
        location.href = "/mytimesheet/?date=" + $(this).val();
    });
} );


function showDateAt() {
    location.href = "/mytimesheet/?date=" + $("#datechooser").val();
}