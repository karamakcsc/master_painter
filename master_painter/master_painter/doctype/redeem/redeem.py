# Copyright (c) 2023, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe import db
from frappe.model.document import Document

class Redeem(Document):
    pass


@frappe.whitelist()
def get_point_amount(painter_mobile=None):
    result = frappe.db.sql("""
        SELECT SUM(total_points) AS `Points Balance`, name
        FROM `tabPainter Invoice`
        WHERE painter_mobile = %s AND docstatus = 1 AND is_redeem = 0
    """, (painter_mobile,), as_dict=True)
    return result[0]['Points Balance']

########Test################
# @frappe.whitelist()
# def update_inv_after_redeem(name=None):
#     invoice = frappe.get_doc("Painter Invoice", name)
    
#     if invoice.is_redeem == 0:
#         frappe.db.set_value("Painter Invoice", invoice.name, "is_redeem", 1)
    
#     return {"is_redeem_updated": True}
########Test################