# Copyright (c) 2023, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MasterPainterItem(Document):
	pass



@frappe.whitelist()
def get_point_amount(name=None):
    result = frappe.db.sql("""
        SELECT point_amount 
        FROM `tabMaster Painter Item Category` 
        WHERE name = %s 
        ORDER BY creation DESC
        LIMIT 1
    """, (name,), as_dict=True)
    
    if result:
        return result[0].point_amount
    else:
        return 0  # or any default value if no matching record is found
