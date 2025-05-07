import frappe

def create_default_module_profile():
    # Crear el perfil solo si no existe
    if not frappe.db.exists("Module Profile", "Default Restricted"):
        profile = frappe.new_doc("Module Profile")
        profile.module_profile_name = "Default Restricted"
        profile.custom_blocked_modules = [
            {"module": m} for m in [
                "CRM", "Projects", "Manufacturing", "Support",
                "Education", "Non Profit", "Website", "Agriculture", "HR"
            ]
        ]
        profile.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.logger().info("✅ Se creó el Module Profile 'Default Restricted'.")

    # Asignar ese perfil a todos los usuarios del sistema, excepto Administrator
    system_users = frappe.get_all("User", filters={
        "enabled": 1,
        "user_type": "System User",
        "name": ["!=", "Administrator"]
    })

    for user in system_users:
        u = frappe.get_doc("User", user.name)
        if not u.module_profile:
            u.module_profile = "Default Restricted"
            u.save(ignore_permissions=True)
            frappe.logger().info(f"✔ Asignado 'Default Restricted' a {u.name}")
