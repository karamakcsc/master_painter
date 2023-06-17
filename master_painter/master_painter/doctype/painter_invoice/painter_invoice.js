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
		// frappe.msgprint("hi")
        frappe.call({
            method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_store",
            args: {
                painter_mobile: frm.doc.painter_mobile
            },
            callback: function(r) {
				frm.set_value('mc_name', r.message);
            }
        });
    }
});


frappe.ui.form.on('Painter Invoice', {
    onload: function(frm) {
		// frappe.msgprint("hi")
        frappe.call({
            method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_store",
            args: {
                painter_mobile: frm.doc.painter_mobile
            },
            callback: function(r) {
				frm.set_value('mc_name', r.message);
            }
        });
    }
});


frappe.ui.form.on('Painter Invoice', {
    onload: function(frm) {
		// frappe.msgprint("hi")
        frappe.call({
            method: "master_painter.master_painter.doctype.painter_invoice.painter_invoice.get_painter_level",
            args: {
                painter_mobile: frm.doc.painter_mobile
            },
            callback: function(r) {
				frm.set_value('painter_level', r.message);
            }
        });
    }
});


frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item Category Matrix", {"painter_level": frm.doc.painter_level, "item_category": d.item_category}, "point_amount", function(value) {
            d.point_amount = value.point_amount;
            cur_frm.refresh_field();
        });
});


frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        frappe.db.get_value("Master Painter Item", {"item_number": d.item_number}, "item_price", function(value) {
            d.sys_rate = value.item_price;
            cur_frm.refresh_field();
        });
});

frappe.ui.form.on('Painter Sales Item', {
    items_remove: function(frm, cdt, cdn) {
        update_total_points(frm);
    },
    selling_rate: function(frm, cdt, cdn) {
        update_total_points(frm);
    }
});
function update_total_points(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.point_amount);
    });
    frm.set_value('total_points', total);
    refresh_field("total_points");
}

frappe.ui.form.on('Painter Sales Item', {
    items_remove: function(frm, cdt, cdn) {
        update_price_difference(frm);
    },
    selling_rate: function(frm, cdt, cdn) {
        update_price_difference(frm);
    }
});
function update_price_difference(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.price_diff);
    });
    frm.set_value('total_diff', total);
    refresh_field("total_diff");
}



frappe.ui.form.on("Painter Sales Item", "selling_rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
if (d.qr_code)  {
  if (d.selling_rate > 0){
  d.price_diff = flt(d.selling_rate - d.sys_rate)
  cur_frm.refresh_field();
}
}
});


frappe.ui.form.on('Painter Sales Item', {
    items_remove: function(frm, cdt, cdn) {
        update_total_sys_rate(frm);
    },
    selling_rate: function(frm, cdt, cdn) {
        update_total_sys_rate(frm);
    }
});
function update_total_sys_rate(frm) {
    var total = 0;
    frm.doc.items.forEach(function(d) {
        total += flt(d.sys_rate);
    });
    frm.set_value('total_sys_rate', total);
    refresh_field("total_sys_rate");
}