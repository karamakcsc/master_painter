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
        WHERE painter_mobile = %s AND docstatus = 1 AND is_reedem = 0
    """, (painter_mobile,), as_dict=True)
    return result[0]['Points Balance']