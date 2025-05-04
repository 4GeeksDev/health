import frappe

def assign_default_module_profile(doc, method):
    # Crear Module Profile si no existe
    if not frappe.db.exists("Module Profile", "Default Restricted"):
        profile = frappe.new_doc("Module Profile")
        profile.module_profile_name = "Default Restricted"  # <- este es el campo correcto
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

    # Asignar el módulo al usuario si no tiene uno
    if not doc.module_profile:
        doc.module_profile = "Default Restricted"
        doc.save(ignore_permissions=True)
