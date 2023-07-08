# Copyright (c) 2023, KCSC and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document
from frappe.model.document import Document
from master_painter.qr_code import get_qr_code

class QRGeneration(Document):
    def __init__(self, *args, **kwargs):
        super(QRGeneration, self).__init__(*args, **kwargs)
    def on_submit(self):
        for qr_code in self.qr_codes:
            MasterPainterQRLibrary(qr_code.item_number, qr_code.item_name, qr_code.title)
    
    def validate(self):
        for qr_code in self.qr_codes:
            qr_code.title = self.generate_random_qr_code()
            qr_code.qr_code = get_qr_code(qr_code.title)

    def generate_random_qr_code(self):
        # Generate a random string with uppercase letters
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        
        # Generate the QR code using the random string
        qr_code = get_qr_code(random_string)

        return random_string

@frappe.whitelist()
def MasterPainterQRLibrary(item_number, item_name, title):
    entry = {
        "qr_code": title,
        "item_number": item_number,
        "item_name": item_name
    }
    (frappe.new_doc("Master Painter QR Library")
        .update(entry)
        .insert(ignore_permissions=True, ignore_mandatory=True)).run_method('save')
    frappe.db.commit()