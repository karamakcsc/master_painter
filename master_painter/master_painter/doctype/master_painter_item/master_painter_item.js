// Copyright (c) 2023, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Master Painter Item', {
	// refresh: function(frm) {

	// }
});



// cur_frm.fields_dict['point_amount'].get_query = function(doc) {
// 	return {
// 		filters: {
// 			"name": doc.item_category
// 		}
// 	}
// }


frappe.ui.form.on('Master Painter Item', {
	item_category: function(frm) {
		frappe.call({
			method: "master_painter.master_painter.doctype.master_painter_item.master_painter_item.get_point_amount",
			args: {
				name: frm.doc.item_category // Pass the item category name as an argument
			},
			callback: function(r) {
				frm.set_value('point_amount', r.message); // Set the returned value as the 'point_amount' field value
			}
		});
	}
});
