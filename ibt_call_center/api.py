import frappe
from frappe import _
from email.utils import formataddr

@frappe.whitelist()
def so_after_submit(self, method):

	if self.store_email != '' and self.store != None:
		message = """<p>&nbsp;</p>
				<table style="height: 43px;" border="1" width="504">
				<tbody>
				<tr>
				<td style="width: 244px;"><strong>Customer Name</strong></td>
				<td style="width: 244px;"> {0} </td>
				</tr>
				<tr>
				<td style="width: 244px;"><strong>Mobile Number</strong></td>
				<td style="width: 244px;"> {1} </td>
				</tr>
				<tr>
				<td style="width: 244px;"><strong>Order Type</strong></td>
				<td style="width: 244px;"> {2} </td>
				</tr>
				<tr>
				<td style="width: 244px;"><strong>Total</strong></td>
				<td style="width: 244px;"> {3} </td>
				</tr>
				</tbody>
				</table>""".format(self.customer, self.mobile, self.order_type, self.grand_total)

		sender = formataddr(['Notifications', 'callcenteribt@gmail.com'])

		frappe.sendmail(recipients=[self.store_email], 
						sender= sender,
						subject= 'New Order ' + self.store + ' Store - ' + self.customer,
						message= message,
						now= 1)
