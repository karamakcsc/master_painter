from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json


@frappe.whitelist()
def get_painter_no(mobile_number=None, first_name=None):
    return frappe.db.sql("""
        SELECT tp.mobile_number
        FROM `tabPainter` tp
        WHERE tp.mobile_number = %s
        ORDER BY tp.creation DESC;
        """, (mobile_number,), as_dict=True)





# @frappe.whitelist()
# def get_painter_no(mobile_number=None, first_name=None):
#     return frappe.db.sql("""
#         SELECT *
#         FROM `tabPainter` tp
#         WHERE tp.mobile_number = %s
#         ORDER BY tp.creation DESC;
#         """, (mobile_number, first_name), as_dict=True)
