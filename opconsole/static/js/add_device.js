function showFormForType() {
   var typeId = $("#devType").val();
   if ( typeId != -1 ) {
        $(".formWizard").hide();
        $("#" + typeId).show();
   }
}
$(document).ready(function() {$(".formWizard").hide();});