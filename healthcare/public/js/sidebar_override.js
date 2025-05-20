// sidebar_override.js
setTimeout(() => {
  console.log("✅ sidebar_override.js ejecutado con delay");

  // Cambia etiquetas del menú lateral
  document.querySelectorAll('.sidebar-item-label').forEach(label => {
    if (label.textContent.includes("ERPNext Settings")) {
      label.textContent = "Settings";
    } else if (label.textContent.includes("ERPNext Integrations")) {
      label.textContent = "4Geeks Integrations";
    }
  });

  // Cambia encabezados específicos
  document.querySelectorAll(".widget-title, .ellipsis").forEach(el => {
    if (el.textContent.includes("ERPNext")) {
      el.textContent = el.textContent.replace("ERPNext", "").trim();
    }
  });

}, 1500); // Espera 1.5 segundos para asegurar que Frappe haya terminado de renderizar
