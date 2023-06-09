// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Painter Invoice', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Painter Invoice', {
    onload: function(frm) {
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
});


frappe.ui.form.on('Painter Invoice', {
    onload: function(frm) {
        if (frm.doc.docstatus === 0) {
            frappe.call({
                method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_level",
                args: {
                    painter_mobile: frm.doc.painter_mobile
                },
                callback: function(r) {
                    if (r && r.message) {
                        frm.set_value('painter_level', r.message);
                    } else {
                        frappe.msgprint("Unable to retrieve painter level.");
                    }
                }
            });
        }
    }
});



frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item Category Matrix", {"painter_level": frm.doc.painter_level, "item_category": d.item_category}, "point_amount", function(value) {
            d.point_amount = value.point_amount;
        });
});


frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_price", function(value) {
            d.sys_rate = value.item_price;
        });
});


frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
if (d.qr_code)  {
  if (d.selling_rate > 0){
  d.price_diff = flt(d.selling_rate - d.sys_rate)
  cur_frm.refresh_field();
}
}
});



frappe.ui.form.on("Painter Sales Item", {
    refresh: function(frm) {
        update_total_selling_rate(frm);
        update_total_sys_rate(frm);
        update_total_points(frm);
        update_total_diff_rate(frm);
    },
    validate: function(frm) {
        update_total_selling_rate(frm);
        update_total_sys_rate(frm);
        update_total_points(frm);
        update_total_diff_rate(frm);
    },
    selling_rate: function(frm, cdt, cdn) {
        update_total_selling_rate(frm);
        update_total_sys_rate(frm);
        update_total_points(frm);
        update_total_diff_rate(frm);
    },
    items_remove: function(frm, cdt, cdn) {
        update_total_selling_rate(frm);
        update_total_sys_rate(frm);
        update_total_points(frm);
        update_total_diff_rate(frm);
    }
});

var update_total_selling_rate = function(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.selling_rate);
    });
    frm.set_value('total_selling_rate', total);
    refresh_field("total_selling_rate");
};

var update_total_sys_rate = function(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.sys_rate);
    });
    frm.set_value('total_sys_rate', total);
    refresh_field("total_sys_rate");
};

var update_total_points = function(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.point_amount * d.item_volume);
    });
    frm.set_value('total_points', total);
    refresh_field("total_points");
};

var update_total_diff_rate = function(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.price_diff);
    });
    frm.set_value('total_diff', total);
    refresh_field("total_diff");
};
