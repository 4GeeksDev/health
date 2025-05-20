import frappe
import json
import os

def apply_custom_workspaces():
    workspace_path = frappe.get_app_path("healthcare", "config", "workspace")
    filenames = ["projects.json", "crm.json", "manufacturing.json", "erpnext_integrations.json", "settings.json"]

    for filename in filenames:
        full_path = os.path.join(workspace_path, filename)
        with open(full_path) as f:
            data = json.load(f)

        if frappe.db.exists("Workspace", data.get("name")):
            frappe.delete_doc("Workspace", data.get("name"), force=True)

        doc = frappe.get_doc(data)
        doc.flags.ignore_permissions = True
        doc.flags.ignore_links = True
        doc.insert(ignore_permissions=True)
