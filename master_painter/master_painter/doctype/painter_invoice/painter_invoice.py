# Copyright (c) 2023, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import db

class PainterInvoice(Document):
	pass



@frappe.whitelist()
def get_painter_name(painter_mobile=None):
    result = frappe.get_list(
        "Painter",
        filters={'name': painter_mobile},
        fields=['first_name', 'middle_name', 'last_name'],
        order_by='creation DESC',
        limit=1
    )

    if result:
        painter = result[0]
        return painter.get('first_name', '') + ' ' + painter.get('middle_name', '') + ' ' + painter.get('last_name', '')
    else:
        return 0
    doc.save()


@frappe.whitelist()
def get_painter_level(painter_mobile=None):
    result = frappe.get_list(
        "Painter",
        filters={'name': painter_mobile},
        fields=['painter_level'],
        order_by='creation DESC',
        limit=1
    )

    if result:
        return result[0].painter_level
    else:
        return 0
    doc.save()



# def get_item(doc, method):
#     for row in doc.items:
#         item = frappe.get_doc("Master Painter QR Library", {"qr_code": row.qr_code})
#         if item:
#             row.item_name = item.item_name
#             row.item_number = item.item_number
#     doc.save()

# def get_item_category(doc, method):
#     for row in doc.items:
#         item = frappe.get_doc("Master Painter Item", {"item_number": row.item_number})
#         if item:
#             row.item_category = item.item_category
#     doc.save()


def set_item_details(doc, method):
    for row in doc.items:
        item_qr = frappe.get_doc("Master Painter QR Library", {"qr_code": row.qr_code})
        if item_qr:
            row.item_name = item_qr.item_name
            row.item_number = item_qr.item_number

            item_category = frappe.get_doc("Master Painter Item", {"item_number": item_qr.item_number})
            if item_category:
                row.item_category = item_category.item_category

            item_volume = frappe.get_doc("Master Painter Item", {"item_number": item_qr.item_number})
            if item_volume:
                row.item_volume = item_category.item_volume
    doc.save()
