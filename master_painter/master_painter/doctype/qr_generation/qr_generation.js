// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('QR Generation', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('QR Generation', {
    onload: function(frm) {
        frm.get_field('qr_codes').grid.cannot_add_rows = true;
    }
    });

frappe.ui.form.on('QR Generation', {
    item_number: function(frm, cdt, cdn) {
        if (frm.doc.item_number) {
            var child_table = frm.doc.qr_codes || [];
            var max_rows = 57;
            
            // Insert new rows if needed
            for (var i = child_table.length; i < max_rows; i++) {
                var child_doc = frappe.model.get_new_doc('QR Generation Item');
                child_doc.item_number = frm.doc.item_number;
                child_table.unshift(child_doc);
            }
            
            // Remove excess rows
            if (child_table.length > max_rows) {
                child_table.splice(max_rows, child_table.length - max_rows);
            }
            
            // Remove last row if empty
            var last_row = child_table[child_table.length - 1];
            if (last_row && !last_row.item_number) {
                child_table.pop();
            }
            
            frm.set_value('qr_codes', child_table);
            refresh_field('qr_codes');
            
            // Fetch and set item_name for each child row
            child_table.forEach(function(d) {
                frappe.db.get_value("Master Painter Item", { "item_number": d.item_number }, "item_name", function(value) {
                    frappe.model.set_value(d.doctype, d.name, "item_name", value.item_name);
                });
            });
        }
    }
});

frappe.ui.form.on("QR Generation Item", {
    item_number: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item", { "item_number": d.item_number }, "item_name", function(value) {
            frappe.model.set_value(cdt, cdn, "item_name", value.item_name);
        });
    }
});

frappe.ui.form.on("QR Generation", {
    qr_codes_add: function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item", { "item_number": frm.doc.item_number }, "item_name", function(value) {
            frappe.model.set_value(row.doctype, row.name, "item_name", value.item_name);
        });
    },
    validate: function(frm) {
        frm.doc.qr_codes.forEach(function(row) {
            frappe.db.get_value("Master Painter Item", { "item_number": frm.doc.item_number }, "item_name", function(value) {
                frappe.model.set_value(row.doctype, row.name, "item_name", value.item_name);
            });
        });
    }
});
