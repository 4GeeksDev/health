import frappe

def assign_default_module_profile(doc, method):
    frappe.msgprint("Hook ejecutado para asignar módulo por defecto")  # prueba visual
    if not doc.module_profile:
        doc.module_profile = "Default Restricted"
        doc.save(ignore_permissions=True)
