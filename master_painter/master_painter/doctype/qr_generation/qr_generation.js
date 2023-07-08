// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('QR Generation', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on("QR Generation Item", {
    item_number: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_name", function(value) {
            frappe.model.set_value(cdt, cdn, "item_name", value.item_name);
        });
    },
    onload: function(frm) {
        frm.doc.items.forEach(function(d) {
            frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_name", function(value) {
                frappe.model.set_value(d.doctype, d.name, "item_name", value.item_name);
            });
        });
    },
	validate: function(frm) {
        frm.doc.items.forEach(function(d) {
            frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_name", function(value) {
                frappe.model.set_value(d.doctype, d.name, "item_name", value.item_name);
            });
        });
    },
	before_save: function(frm) {
        frm.doc.items.forEach(function(d) {
            frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_name", function(value) {
                frappe.model.set_value(d.doctype, d.name, "item_name", value.item_name);
            });
        });
    }
});
