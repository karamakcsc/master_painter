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
