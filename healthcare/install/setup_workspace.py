import frappe
import json
import os

def apply_custom_workspaces():
    workspace_path = frappe.get_app_path("healthcare", "config", "workspace")
    filenames = [
        "projects.json",
        "crm.json",
        "manufacturing.json",
        "website.json"
        "support.json"
    ]

    for filename in filenames:
        full_path = os.path.join(workspace_path, filename)
        with open(full_path) as f:
            data = json.load(f)

        workspace_name = data.get("name")

        # Si el Workspace ya existe, actualízalo
        if frappe.db.exists("Workspace", workspace_name):
            doc = frappe.get_doc("Workspace", workspace_name)
            doc.update(data)
            doc.is_hidden = 1
            doc.flags.ignore_permissions = True
            doc.flags.ignore_links = True
            doc.save(ignore_version=True)
        else:
            # Si no existe, insertarlo como nuevo
            doc = frappe.get_doc(data)
            doc.flags.ignore_permissions = True
            doc.flags.ignore_links = True
            doc.insert(ignore_permissions=True)
