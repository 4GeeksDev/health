import frappe

def assign_default_module_profile(doc, method):
    # Verifica si el Module Profile ya existe
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
            {"module": "Website"},
        ]
        profile.save(ignore_permissions=True)
        frappe.db.commit()

    # Asignar solo si el usuario no tiene uno definido
    if not doc.module_profile:
        doc.module_profile = "Default Restricted"
        doc.save(ignore_permissions=True)
