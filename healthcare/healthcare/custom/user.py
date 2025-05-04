import frappe

def ensure_default_module_profile():
	if frappe.db.exists("Module Profile", "Default Restricted"):
		return

	profile = frappe.new_doc("Module Profile")
	profile.module_profile_name = "Default Restricted"  # campo correcto
	profile.restrict_to_domain = ""
	profile.blocked_modules = [
		{"module": "Manufacturing"},
		{"module": "Agriculture"},
		{"module": "Education"},
		{"module": "Non Profit"},
		{"module": "Projects"},
		{"module": "CRM"},
		{"module": "Support"},
		{"module": "Website"},
		{"module": "Subcontracting"},
		{"module": "Telephony"},
		{"module": "Utilities"},
		{"module": "Workflow"},
		{"module": "Portal"},
		{"module": "Printing"},
		{"module": "Quality Management"},
		{"module": "Regional"},
		{"module": "Email"},
		{"module": "EDI"},
		{"module": "ERPNext Integrations"},
		{"module": "Geo"},
		{"module": "Integrations"},
		{"module": "Social"},
		{"module": "Maintenance"},
		{"module": "Custom"},
		{"module": "Desk"},
		{"module": "Automation"},
		{"module": "Business Theme V14"},
		{"module": "Analytics"},
	]
	profile.save(ignore_permissions=True)
	frappe.db.commit()


def assign_default_module_profile(doc, method):
	frappe.logger().info(f"Assigning Default Restricted to user {doc.name}")
	# Asegurarse que el perfil existe
	ensure_default_module_profile()

	# Asignar perfil si el usuario no tiene
	if not doc.module_profile:
		doc.module_profile = "Default Restricted"
		doc.save(ignore_permissions=True)
