// Copyright (c) 2022, Atom Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Booking Form', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Booking Form', "refresh", function(frm){
	frm.add_custom_button(__("Sales Order"), function() {


		frappe.model.open_mapped_doc({
			method: 'erpnext.selling.doctype.sales_order.sales_order.make_so',
			frm: cur_frm
		})
	}, __('Create')
	)
});

