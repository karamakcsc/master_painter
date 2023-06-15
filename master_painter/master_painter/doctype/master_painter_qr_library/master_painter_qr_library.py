# Copyright (c) 2023, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MasterPainterQRLibrary(Document):
	pass




@frappe.whitelist()
def get_item_name(item_number=None):
    result = frappe.get_list(
        "Master Painter Item",
        filters={'item_number': item_number},
        fields=['item_name'],
        order_by='creation DESC',
        limit=1
    )

    if result:
        return result[0].item_name
    else:
        return 0
