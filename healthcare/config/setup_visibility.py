import frappe

def setup_4geeks_health_visibility():
    # Módulos a ocultar para usuarios estándar
    modules_to_hide = [
        "Manufacturing", "Agriculture", "Education", "Non Profit",
        "Projects", "CRM", "Support", "Website"
    ]

    # Roles estándar a los que se les ocultarán los módulos
    standard_roles = [
        "Healthcare Practitioner", "Accounts User", "Stock User", "HR User", "Buying User", "Sales User"
    ]

    for role in standard_roles:
        profile_name = f"4Geeks Health - {role}"

        # Verificar si ya existe para evitar duplicados
        if not frappe.db.exists("Module Profile", {"module_profile_name": profile_name}):
            profile = frappe.get_doc({
                "doctype": "Module Profile",
                "module_profile_name": profile_name,
                "restrict_to_role": role,
                "modules": [{"module": m} for m in modules_to_enable]
            })
            profile.insert(ignore_permissions=True)


    # Módulos esenciales que deben estar disponibles para los roles estándar
    modules_to_enable = [
        "Healthcare", "Accounting", "Stock", "Buying", "HR", "Selling"
    ]

    for role in standard_roles:
        profile_name = f"4Geeks Health - {role}"
        profile = frappe.get_doc({
            "doctype": "Module Profile",
            "module_profile_name": profile_name,
            "restrict_to_role": role,
            "modules": [{"module": m} for m in modules_to_enable]
        })
        profile.insert(ignore_permissions=True)

    frappe.db.commit()
