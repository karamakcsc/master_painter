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



@frappe.whitelist(allow_guest=True)
def send_sms(numbers,accpass ):
    url = "https://josmsservice.com/SMSServices/Clients/Prof/RestSingleSMS_General/SendSMS"

    # Parameters
    params = {
        "senderid": "JotunPaints",
        "numbers": numbers,
        "accname": "Jotun",
        "accpass": accpass,
        "msg": "Content of the message",
        # "id": "12345"  # Optional message ID
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return "SMS sent successfully!"
        else:
            return f"Failed to send SMS. Error: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Failed to send SMS: {str(e)}"
