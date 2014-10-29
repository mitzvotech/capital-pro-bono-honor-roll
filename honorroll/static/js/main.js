$("#new_org_save").click(function () {
	console.log($("#new_org_input"))
	$("#id_organization").prepend('<option>' + $("#new_org_input").val() + '</option>')
                $("#id_organization").val($("#new_org_input").val())
	$("#new_org_modal").modal("hide");
})