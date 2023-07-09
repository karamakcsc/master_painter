// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Redeem', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Redeem', {
    onload: function(frm) {
        painter_name(frm);
    },

    painter_mobile: function(frm) {
        painter_name(frm);
    }
});

function painter_name(frm) {
    if (frm.doc.docstatus === 0) {
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
		frm.set_query("sales_invoice_no", "sales_invoices", function(doc, cdt, cdn) {
			let d = locals[cdt][cdn];
			return {
				filters: [
					['Painter Invoice', 'docstatus', '=', 1],
					['Painter Invoice', 'is_reedem', '=', 0],
					['Painter Invoice', 'painter_mobile', '=', frm.doc.painter_mobile]
				]
			};
		});
	},
});


frappe.ui.form.on("Redeem Item", "sales_invoice_no", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    frappe.db.get_value("Painter Invoice", d.sales_invoice_no, "posting_date", function(value) {
        d.posting_date = value.posting_date;
        refresh_field("sales_invoices"); 
    });
});


frappe.ui.form.on('Redeem', {
    onload: function(frm) {
        get_point_amount(frm);
    },

    painter_mobile: function(frm) {
        get_point_amount(frm);
    }
});

function get_point_amount(frm) {
    if (frm.doc.docstatus === 0) {
        frappe.call({
            method: "master_painter.master_painter.doctype.redeem.redeem.get_point_amount",
            args: {
                painter_mobile: frm.doc.painter_mobile
            },
            callback: function(r) {
                frm.set_value('point_balance', r.message);
            }
        });
    }
}


frappe.ui.form.on("Redeem Item", "sales_invoice_no", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    frappe.db.get_value("Painter Invoice", d.sales_invoice_no, "total_points", function(value) {
        d.total_point = value.total_points;
        refresh_field("sales_invoices"); 
    });
});


frappe.ui.form.on("Redeem", {
    refresh: function(frm) {
        update_point_after_redeem(frm);
        update_total_points(frm);
        update_total_redeem_point(frm);
        update_total_redeem_amount(frm);
    },
    validate: function(frm) {
        update_point_after_redeem(frm);
        update_total_points(frm);
        update_total_redeem_point(frm);
        update_total_redeem_amount(frm);
    },
    redeem_point: function(frm, cdt, cdn) {
        update_total_points(frm);
        update_total_redeem_point(frm);
        update_total_redeem_amount(frm);
    },
    items_remove: function(frm, cdt, cdn) {
        update_total_points(frm);
        update_total_redeem_point(frm);
        update_total_redeem_amount(frm);
    }
});

var update_point_after_redeem = function(frm) {
    frm.doc.point_after_redeem = flt(frm.doc.point_balance - frm.doc.redeem_point);
    refresh_field("point_after_redeem");
};

var update_total_points = function(frm) {
    var total = 0;
    frm.doc.sales_invoices.forEach(function(d) {
        total += flt(d.total_point);
    });
    frm.set_value('total_points', total);
    refresh_field("total_points");
};

var  update_total_redeem_point = function(frm) {
    var total = 0;
    frm.doc.sales_invoices.forEach(function(d) {
        total += flt(d.redeem_point);
    });
    frm.set_value('total_redeem_point', total);
    refresh_field("total_redeem_point");
};

var  update_total_redeem_amount = function(frm) {
    var total = 0;
    frm.doc.sales_invoices.forEach(function(d) {
        total += flt(d.redeem_amount);
    });
    frm.set_value('total_redeem_amount', total);
    refresh_field("total_redeem_amount");
};


frappe.ui.form.on("Redeem", {
    validate: function(frm) {
        if (frm.doc.total_redeem_point !== frm.doc.redeem_point) {
            frappe.msgprint('Total Redeem Point is not equal The Redeem Point');
            validated = false;
        }
        if (frm.doc.redeem_point > frm.doc.point_balance) {
            frappe.msgprint('Redeem Point Greater Than Point Balance');
            validated = false;
        }
    }
});

frappe.ui.form.on("Redeem Item", "redeem_point", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    if (d.redeem_point > d.total_point) {
        frappe.msgprint('Redeem Point In Sales Invoice Greater Than Total Point In Sales Invoice');
        validated = false;
    }
});

frappe.ui.form.on("Redeem Item", "sales_invoice_no", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
        d.redeem_point = d.total_point;
        refresh_field("sales_invoices"); 
});



frappe.ui.form.on("Redeem Item", "sales_invoice_no", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    frappe.db.get_single_value("Redeem Setting", "point_rate")
        .then(function(value) {
            d.point_rate = value;
            d.redeem_amount = flt(d.point_rate  * d.redeem_point)
            refresh_field("sales_invoices");
        });
});
