$("#new_org_save").click(function () {
	console.log($("#new_org_input"))
	$("#id_organization").append('<option>' + $("#new_org_input").val() + '</option>')
	$("#new_org_modal").modal("hide");

})