from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json


# @frappe.whitelist()
# def get_painter_no(mobile_number=None, first_name=None):
#     return frappe.db.sql("""
#         SELECT tp.mobile_number
#         FROM `tabPainter` tp
#         WHERE tp.mobile_number = %s
#         ORDER BY tp.creation DESC;
#         """, (mobile_number,), as_dict=True)


from flask import Flask, request, jsonify
# import frappe

app = Flask(__name__)

# Endpoint for the Engati response
@app.route('/engati-response', methods=['Get'])
def engati_response():
    # Retrieve the Engati user object from the request
    engati_user = request.json.get('user')

    # Extract the phone number from the Engati user object
    mobile_number = engati_user.get('phone_no')

    # Call the Frappe function with the mobile number
    results = get_painter_no(mobile_number=mobile_number)

    # Return the results as a JSON response
    return jsonify(results)

# Frappe function to get the painter mobile number
@frappe.whitelist()
def get_painter_no(mobile_number=None, first_name=None):
    return frappe.db.sql("""
        SELECT tp.mobile_number
        FROM `tabPainter` tp
        WHERE tp.mobile_number = %s
        ORDER BY tp.creation DESC;
        """, (mobile_number,), as_dict=True)

if __name__ == '__main__':
    app.run()



# @frappe.whitelist()
# def get_painter_no(mobile_number=None, first_name=None):
#     return frappe.db.sql("""
#         SELECT *
#         FROM `tabPainter` tp
#         WHERE tp.mobile_number = %s
#         ORDER BY tp.creation DESC;
#         """, (mobile_number, first_name), as_dict=True)
