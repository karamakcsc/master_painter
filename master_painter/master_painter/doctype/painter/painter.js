// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Painter', {
	// refresh: function(frm) {

	// }
});



// frappe.ui.form.on('Painter', {
// 	on_submit: function(frm) {
// 	//   var numbers = frm.doc.mobile_number;  // Use the mobile_number field value from the form
// 	//   var accpass = "pP$psJpsnyYClk2v";  // Replace with your actual account password
// 	  frappe.call({
// 		method: "master_painter.api.send_sms",
// 		args: {
// 			"numbers": frm.doc.name,
// 			"accpass": "pP$psJpsnyYClk2v"
// 		},
		
// 		callback: function(response) {
			
// 		  // Handle the response from the server-side method
// 		  var result = response.message;
// 		  console.log(result);
// 		  // Perform any additional actions based on the response
// 		}
// 	  });
// 	}
//   });



// frappe.ui.form.on('Painter', {
// 	after_insert: function(frm) {
// 	  frappe.msgprint("hi");
// 	  frappe.call({
// 		method: "master_painter.api.send_sms",
// 		args: {
// 		  "numbers": frm.doc.name,
// 		  "accpass": "pP$psJpsnyYClk2v"
// 		},
// 		callback: function(response) {
// 		  // Handle the response from the server-side method
// 		  var result = response.message;
// 		  console.log(result);
// 		  // Perform any additional actions based on the response
// 		}
// 	  });
// 	}
//   });
  


var smsCount = 0;

frappe.ui.form.on("Painter", "refresh", function(frm) {
  if (frm.doc.docstatus == 1) {
        frm.add_custom_button(__("Send SMS"), function() {
            // When this button is clicked, do this
            frappe.call({
                method: "master_painter.api.send_sms",
                args: {
                    "numbers": frm.doc.name,
                    "accpass": "pP$psJpsnyYClk2v",
                    "msg": frm.doc.msg
                },
                callback: function(response) {
                    // Handle the response from the server-side method
                    var result = response.message;
                    console.log(result);
                    // Perform any additional actions based on the response
                    
                    // Increment the SMS count
                    incrementSMSCount(frm);
                }
            });
        });
    }
});

function incrementSMSCount(frm) {
    smsCount++;
    frm.set_value("sms_count", smsCount);
    frm.refresh_field("sms_count");
}

frappe.ui.form.on("Painter", "refresh", function(frm) {
if (frm.doc.sms_count ==0) {frappe.msgprint("Please Send SMS To Activate The Painter");}
});