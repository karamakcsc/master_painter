// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Master Painter QR Library', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Master Painter QR Library', {
    item_number: function(frm) {
		// frappe.msgprint("hi")
        frappe.call({
            method: "master_painter.master_painter.doctype.master_painter_qr_library.master_painter_qr_library.get_item_name",
            args: {
                item_number: frm.doc.item_number
            },
            callback: function(r) {
                frm.set_value('item_name', r.message);
            }
        });
    }
});
