# -*- coding: utf-8 -*-
# Copyright (c) 2022, Atom Global and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class BookingForm(Document):
	pass

@frappe.whitelist()
def make_so(source_name, target_doc=None):
	target_doc = get_mapped_doc("Booking Form", source_name,
	{"Booking Form": {
	"doctype": "Sales Order",
	"field_map": {
	"service_type1": "service_type",
	"job_date_": "date"
	}
	}},
	target_doc)
				
	return target_doc
