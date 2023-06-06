from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json


# @frappe.whitelist()
# def get_painter_no(mobile_number=None, first_name=None):
#     return frappe.db.sql("""SELECT tp.mobile_number,tp.first_name
#                             FROM `tabPainter` tp
#                             WHERE tp.mobile_number = %s
#                             ORDER BY tp.creation DESC;""",
#                             (mobile_number,first_name),as_dict=True)





@frappe.whitelist()
def get_painter_no(mobile_number=None, first_name=None):
    # Assuming you have imported and configured the necessary modules for Frappe
 results = frappe.db.sql("""SELECT tp.mobile_number, tp.first_name
                              FROM `tabPainter` tp
                              WHERE tp.mobile_number = %s
                              ORDER BY tp.creation DESC;""",
                            (mobile_number, first_name),
                            as_dict=True)
    
    return results

url = "http://ugc.kcsc.com.jo/api/method/master_painter.api.get_painter_no"
query_params = {
    'mobile_number': '%s'  # Adjust the value as per your requirements
}

headers = {
    'Authorization': 'Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==',
    'Cookie': 'full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image='
}

response = requests.get(url, headers=headers, params=query_params)

print(response.text)
