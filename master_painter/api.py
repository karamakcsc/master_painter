from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json
from frappe import _

@frappe.whitelist()
def get_painter_no(mobile_number=None, docstatus=None):
    if mobile_number is None and docstatus is None:
        return {
            'mobile_number': None,
            'first_name': None,
            'painter_level': None,
            'docstatus': None
        }

    result = frappe.db.sql("""
        SELECT tp.mobile_number, tp.first_name, tp.painter_level, tp.docstatus
        FROM `tabPainter` tp
        WHERE tp.mobile_number = %s OR tp.docstatus = %s
        ORDER BY tp.creation DESC;
        """, (mobile_number, docstatus), as_dict=True)

    # Reset all memory or variables here
    frappe.clear_cache()

    if not result:
        return {
            'mobile_number': None,
            'first_name': None,
            'painter_level': None,
            'docstatus': None
        }

    return result

# @frappe.whitelist()
# def get_painter_no_active(mobile_number=None):
#     result = frappe.db.sql("""
#         SELECT tp.mobile_number, tp.first_name, tp.painter_level
#         FROM `tabPainter` tp
#         WHERE tp.mobile_number = %s 
#         ORDER BY tp.creation DESC;
#         """, (mobile_number,), as_dict=True)
    
#     # Reset all memory or variables here
#     frappe.clear_cache()
    
#     return result




@frappe.whitelist()
def get_painter_no_active(mobile_number=None, docstatus=None):
    if mobile_number is None :
        return {
            'mobile_number': None
        }

    result = frappe.db.sql("""
        SELECT tp.mobile_number
        FROM `tabPainter` tp
        WHERE tp.mobile_number = %s OR tp.docstatus = %s
        ORDER BY tp.creation DESC;
        """, (mobile_number, docstatus), as_dict=True)

    # Reset all memory or variables here
    frappe.clear_cache()

    if not result:
        return {
            'mobile_number': None
        }

    return result




# @frappe.whitelist()
# def get_painter_no_active(mobile_number=None, docstatus=None):
#     result = frappe.db.sql("""
#         SELECT tp.mobile_number, tp.first_name, tp.painter_level, tp.docstatus
#         FROM `tabPainter` tp
#         WHERE tp.mobile_number = %s OR tp.docstatus = %s
#         ORDER BY tp.creation DESC;
#         """, (mobile_number, docstatus), as_dict=True)
    
#     # Reset all memory or variables here
#     frappe.clear_cache()
    
#     if not result:
#         return None
    
#     return result








#######################


import json
import frappe

@frappe.whitelist()
def get_painter_no_active1(mobile_number=None, docstatus=None):
    if mobile_number is None:
        return {
            "data": {
                "type": "text",
                "text": "your message"
            }
        }

    result = frappe.db.sql("""
        SELECT tp.mobile_number
        FROM `tabPainter` tp
        WHERE tp.mobile_number = %s OR tp.docstatus = %s
        ORDER BY tp.creation DESC;
        """, (mobile_number, docstatus), as_dict=True)

    # Reset all memory or variables here
    frappe.clear_cache()

    if not result:
        return {
            "data": {
                "type": "text",
                "text": "your message"
            }
        }

    # Convert the result to text
    response_text = '\n'.join([f"mobile_number: {row['mobile_number']}" for row in result])

    return {
        "data": {
            "type": "text",
            "text": response_text
        }
    }

# Example usage
# mobile_number = "1234567890"  # Provide a valid mobile number
# docstatus = 1  # Provide a valid docstatus value

# response = get_painter_no_active(mobile_number, docstatus)
# response_json = json.dumps(response)

# print(response_json)


