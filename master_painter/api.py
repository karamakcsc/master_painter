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
def send_sms(numbers,accpass,msg):
    url = "https://josmsservice.com/SMSServices/Clients/Prof/RestSingleSMS_General/SendSMS"

    # Parameters
    params = {
        "senderid": "JotunPaints",
        "numbers": numbers,
        "accname": "Jotun",
        "accpass": accpass,
        "msg": msg,
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


@frappe.whitelist()
def update_qr(qr_code=None):
    if qr_code is None:
        return

    doc = frappe.get_doc("Master Painter QR Library", {"qr_code": qr_code})
    if doc:
        doc.is_sold = 1
        doc.save()




@frappe.whitelist()
def get_qr(qr_code=None):
    if qr_code is None:
        return {
            'qr_code': None,
            'item_number': None
        }

    doc = frappe.get_value("Master Painter QR Library", {"qr_code": qr_code}, ["item_number", "is_sold"], order_by="creation DESC")
    if not doc:
        return {
            'qr_code': None,
            'item_number': None,
            'is_sold': 0
        }

    item_number, is_sold = doc

    if is_sold == 1:
        return {
            'qr_code': qr_code,
            'item_number': None,
            'is_sold': 1
        }

    return {
        'qr_code': qr_code,
        'item_number': item_number,
        'is_sold': 0
    }











# @frappe.whitelist()
# def update_inv(qr_code=None, erp_inv_name=None, num_items_to_add=5):
#     url = "http://ugc.kcsc.com.jo/api/resource/Painter Invoice/{erp_inv_name}"
#     headers = {
#         "Authorization": "Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==",
#         "Content-Type": "application/json",
#         "Cookie": "sid=Guest"
#     }

#     data = {
#         "items": []
#     }

#     for i in range(num_items_to_add):
#         new_item = {
#             "qr_code": qr_code
#         }
#         data["items"].append(new_item)

#     response = requests.put(url, headers=headers, data=json.dumps(data))

#     print(response.text)

# # Assuming you have the value for erp_inv_name
# erp_inv_name = "{erp_inv_name}"

# update_inv(qr_code="{qr_code}", erp_inv_name=erp_inv_name, num_items_to_add=5)

# @frappe.whitelist()
# def update_inv(qr_code=None, erp_inv_name=None, num_items_to_add=5):
#     url = f"http://ugc.kcsc.com.jo/api/resource/Painter Invoice/{erp_inv_name}"
#     headers = {
#         "Authorization": "Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==",
#         "Content-Type": "application/json",
#         "Cookie": "sid=Guest"
#     }

#     data = {
#         "items": [qr_code]
#     }

#     response = requests.put(url, headers=headers, data=json.dumps(data))

#     print(response.text)

# # Assuming you have the value for erp_inv_name
# erp_inv_name = "<provide_erp_inv_name>"
# qr_code = "E355P5O18E0X0"

# update_inv(qr_code=qr_code, erp_inv_name=erp_inv_name, num_items_to_add=5)

# @frappe.whitelist()
# def update_inv(qr_code=None, erp_inv_name=None, num_items_to_add=1):
#     url = f"http://ugc.kcsc.com.jo/api/resource/Painter Invoice/{erp_inv_name}"
#     headers = {
#         "Authorization": "Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==",
#         "Content-Type": "application/json",
#         "Cookie": "sid=Guest"
#     }

#     data = {
#         "items": []
#     }

#     for i in range(num_items_to_add):
#         new_item = {
#             "qr_code": qr_code
#         }
#         data["items"].append(new_item)

#     response = requests.put(url, headers=headers, data=json.dumps(data))

#     print(response.text)

# # Assuming you have the value for erp_inv_name and qr_code
# erp_inv_name = "{erp_inv_name}"
# qr_code = "{qr_code}"

# update_inv(qr_code=qr_code, erp_inv_name=erp_inv_name, num_items_to_add=1)



@frappe.whitelist()
def update_inv(qr_code=None,erp_inv_name=None):
    url = "https://ugc.kcsc.com.jo/api/resource/Painter%20Invoice/{erp_inv_name}"
    headers = {
        "Authorization": "Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==",
        "Content-Type": "application/json",
        "Cookie": "sid=Guest"
    }

    # Fetch the existing data
    response = requests.get(url, headers=headers)
    existing_data = response.json()

    # Retrieve the existing items
    existing_items = existing_data.get("data", {}).get("items", [])

    # Find the first empty row index
    empty_row_index = None
    for i, item in enumerate(existing_items):
        if not item.get("qr_code"):
            empty_row_index = i
            break

    # Check if an empty row was found
    if empty_row_index is not None:
        # Update the empty row with the new qr_code
        existing_items[empty_row_index]["qr_code"] = qr_code
    else:
        # Create a new item with the qr_code
        new_item = {"qr_code": qr_code}

        # Insert the new item at the end of the list
        existing_items.append(new_item)

    # Update the data with the updated items
    existing_data["data"]["items"] = existing_items

    # Send the updated data in a PUT request
    response = requests.put(url, headers=headers, data=json.dumps(existing_data))

    if response.status_code == 200:
        print("Data successfully written to the database.")
    else:
        print(f"Failed to write data to the database. Response: {response.text}")


# Assuming you have the value for qr_code
qr_code = "{qr_code}"
erp_inv_name = "{erp_inv_name}"

update_inv(qr_code=qr_code,erp_inv_name=erp_inv_name)
#####################################################################################################

# @frappe.whitelist()
# def update_inv(qr_code=None, erp_inv_name=None, APIresponse=None):
#     url = f"https://ugc.kcsc.com.jo/api/resource/Painter%20Invoice/{erp_inv_name}"
#     headers = {
#         "Authorization": "Basic NzJkNGZhMjUzNmZhMWIxOjgwYjY1NWYzNmY2MWFjYw==",
#         "Content-Type": "application/json",
#         "Cookie": "sid=Guest"
#     }

#     # Fetch the existing data
#     response = requests.get(url, headers=headers)
#     existing_data = response.json()

#     # Retrieve the existing items
#     existing_items = existing_data.get("data", {}).get("items", [])

#     # Find the first empty row index
#     empty_row_index = None
#     for i, item in enumerate(existing_items):
#         if not item.get("qr_code"):
#             empty_row_index = i
#             break

#     # Check if an empty row was found
#     if empty_row_index is not None:
#         # Update the empty row with the new qr_code
#         existing_items[empty_row_index]["qr_code"] = APIresponse
#     else:
#         # Create a new item with the qr_code
#         new_item = {"qr_code": APIresponse}

#         # Insert the new item at the end of the list
#         existing_items.append(new_item)

#     # Update the data with the updated items
#     existing_data["data"]["items"] = existing_items

#     # Send the updated data in a PUT request
#     response = requests.put(url, headers=headers, json=existing_data)  # Use 'json' parameter instead of 'data'

#     if response.status_code == 200:
#         print("Data successfully written to the database.")
#     else:
#         print(f"Failed to write data to the database. Response: {response.text}")


# # Assuming you have the values for APIresponse and erp_inv_name
# APIresponse = "APIresponse"
# erp_inv_name = "erp_inv_name"

# update_inv(qr_code=APIresponse, erp_inv_name=erp_inv_name)
