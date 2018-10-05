# -*- coding: utf-8 -*-
# Copyright (c) 2013, IBT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		dict(label=_("Delivery Date"), fieldtype="Date", width=100),
		dict(label=_("ID"), fieldtype="Link", options='Sales Order', width=80),
		dict(label=_("Customer"), fieldtype="Link", options='Customer', width=130),
		dict(label=_("Mobile"), fieldtype="Data", width=100),
		dict(label=_("Company"), fieldtype="Link", options='Company', width=120),
		dict(label=_("Grand Total"), fieldtype="Currency", width=80),
		dict(label=_("Status"), fieldtype="Data", width=110),
		dict(label=_("Store"), fieldtype="Link", options='Store', width=100),
		dict(label=_("Transaction Date"), fieldtype="Date", width=120),
	]

	return columns

def get_data(filters):
	
	where_clause = ' and transaction_date = '
	where_clause += filters.transaction_date and '"%s" ' % filters.transaction_date or 'DATE_ADD(CURDATE(), INTERVAL -1 DAY) '

	data = frappe.db.sql("""
		SELECT
			delivery_date as 'Delivery Date', name as 'ID', customer as 'Customer', mobile as 'Mobile', company as 'Company', grand_total as 'Grand Total', status as 'Status', store as 'Store', transaction_date as 'Transaction Date'
		FROM
			`tabSales Order`
		WHERE
			docstatus < 2
			{conditions} """.format(conditions=where_clause), as_dict=1)

	return data
