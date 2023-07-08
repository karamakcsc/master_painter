from . import __version__ as app_version

app_name = "master_painter"
app_title = "Master Painter"
app_publisher = "KCSC"
app_description = "Master Painter"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@kcsc.com.jo"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/master_painter/css/master_painter.css"
# app_include_js = "/assets/master_painter/js/master_painter.js"

# include js, css files in header of web template
# web_include_css = "/assets/master_painter/css/master_painter.css"
# web_include_js = "/assets/master_painter/js/master_painter.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "master_painter/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------
# add methods and filters to jinja environment
jinja = {
	"methods": [
		"master_painter.qr_code.get_qr_code"
	],
	# "filters": "qr_demo.utils.jinja_filters"
}
# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "master_painter.install.before_install"
# after_install = "master_painter.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "master_painter.uninstall.before_uninstall"
# after_uninstall = "master_painter.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "master_painter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Painter Invoice": {
		"onload": "master_painter.master_painter.doctype.painter_invoice.painter_invoice.set_item_details"
		# "after_save": "master_painter.master_painter.doctype.painter_invoice.painter_invoice.set_point_amount"
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"master_painter.tasks.all"
#	],
#	"daily": [
#		"master_painter.tasks.daily"
#	],
#	"hourly": [
#		"master_painter.tasks.hourly"
#	],
#	"weekly": [
#		"master_painter.tasks.weekly"
#	]
#	"monthly": [
#		"master_painter.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "master_painter.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "master_painter.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "master_painter.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"master_painter.auth.validate"
# ]

