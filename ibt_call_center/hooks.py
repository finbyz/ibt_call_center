# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ibt_call_center"
app_title = "Ibt Call Center"
app_publisher = "IBT"
app_description = "Call Center"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "callcenteribt@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ibt_call_center/css/ibt_call_center.css"
# app_include_js = "/assets/ibt_call_center/js/ibt_call_center.js"

# include js, css files in header of web template
# web_include_css = "/assets/ibt_call_center/css/ibt_call_center.css"
# web_include_js = "/assets/ibt_call_center/js/ibt_call_center.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ibt_call_center.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ibt_call_center.install.before_install"
# after_install = "ibt_call_center.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ibt_call_center.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ibt_call_center.tasks.all"
# 	],
# 	"daily": [
# 		"ibt_call_center.tasks.daily"
# 	],
# 	"hourly": [
# 		"ibt_call_center.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ibt_call_center.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ibt_call_center.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ibt_call_center.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ibt_call_center.event.get_events"
# }

doc_events = {
	'Sales Order': {
		'before_submit': 'ibt_call_center.api.so_after_submit'
	}
}