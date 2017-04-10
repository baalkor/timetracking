$("#btnClearZone").hide();
$("#btnSaveZone").hide();

var dialog = $( "#save-message" ).dialog({
    autoOpen: false,
    buttons: {
        "Cancel" : function () {
            dialog.dialog("close");
        },
        "Save" : function() {
            if ( $("#zone_name").val() !== "" || ZONES !== undefined ) {
                dialog.dialog("close");
            }

        }
    }
});