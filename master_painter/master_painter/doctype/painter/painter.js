// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Painter', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Painter', {
	on_submit: function(frm) {
	//   var numbers = frm.doc.mobile_number;  // Use the mobile_number field value from the form
	//   var accpass = "pP$psJpsnyYClk2v";  // Replace with your actual account password
	frappe.msgprint("hi")
	  frappe.call({
		method: "master_painter.api.send_sms",
		args: {
			"numbers": frm.doc.name,
			"accpass": "pP$psJpsnyYClk2v"
		},
		
		callback: function(response) {
			
		  // Handle the response from the server-side method
		  var result = response.message;
		  console.log(result);
		  // Perform any additional actions based on the response
		}
	  });
	}
  });
  