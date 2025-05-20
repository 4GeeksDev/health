def apply_custom_workspaces():
    workspace_path = frappe.get_app_path("healthcare", "config", "workspace")
    filenames = ["projects.json", "crm.json", "manufacturing.json", "erpnext_integrations.json", "settings.json"]

    for filename in filenames:
        full_path = os.path.join(workspace_path, filename)
        with open(full_path) as f:
            data = json.load(f)

        doc = frappe.get_doc(data)
        doc.flags.ignore_permissions = True
        doc.flags.ignore_links = True
        doc.save(ignore_version=True)