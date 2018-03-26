// Copyright (c) 2016, IBT and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales Order Summary"] = {
	"filters": [
		{
			fieldname: 'transaction_date',
			label: __("Date"),
			fieldtype: "Date",
			default: frappe.datetime.nowdate()	
		}
	]
}
