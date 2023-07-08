// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Redeem', {
	// refresh: function(frm) {

	// }
});


// frappe.ui.form.on('Redeem', {
//     onload: function(frm) {
//         frappe.call({
//             method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_name",
//             args: {
//                 painter_mobile: frm.doc.painter_mobile
//             },
//             callback: function(r) {
//                 frm.set_value('painter_name', r.message);
//             }
//         });
//     }
// });




frappe.ui.form.on('Redeem', {
    onload: function(frm) {
        painter_name(frm);
    },

    painter_mobile: function(frm) {
		painter_name(frm);
    }
});

function  painter_name(frm) {
    if (docstatus === 0){
        frappe.call({
            method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_name",
            args: {
                painter_mobile: frm.doc.painter_mobile
            },
            callback: function(r) {
                frm.set_value('painter_name', r.message);
            }
        });
}
}


frappe.ui.form.on('Redeem', {
	setup: function(frm) {
		frm.set_query("sales_invoive_no", "sales_invoices", function(doc, cdt, cdn) {
			let d = locals[cdt][cdn];
			return {
				filters: [
					['Painter Invoice', 'docstatus', '=', 1],
					['Painter Invoice', 'is_redeem', '=', 0],
					['Painter Invoice', 'painter_mobile', '=', frm.doc.painter_mobile]
				]
			};
		});
	},
});


// frappe.ui.form.on("Remeed Item", "sales_invoive_no", function(frm, cdt, cdn) {
//     var d = locals[cdt][cdn];
//     frappe.db.get_value("Painter Invoice", d.sales_invoive_no, "posting_date", function(value) {
//         d.posting_date = value.posting_date;
//         refresh_field("sales_invoices"); // Refresh the items field to reflect the updated posting_date
//     });
// });
