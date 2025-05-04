import frappe

def setup_module_profiles():
    if not frappe.db.exists("Module Profile", "Default Restricted"):
        profile = frappe.new_doc("Module Profile")
        profile.name = "Default Restricted"
        profile.restrict_to_domain = ""
        profile.blocked_modules = [
            {"module": "Manufacturing"},
            {"module": "Agriculture"},
            {"module": "Education"},
            {"module": "Non Profit"},
            {"module": "Projects"},
            {"module": "CRM"},
            {"module": "Support"},
            {"module": "Website"}
        ]
        profile.save(ignore_permissions=True)
        frappe.db.commit()

    users = frappe.get_all("User", filters={"enabled": 1, "module_profile": ""})
    for u in users:
        user = frappe.get_doc("User", u.name)
        user.module_profile = "Default Restricted"
        user.save(ignore_permissions=True)
