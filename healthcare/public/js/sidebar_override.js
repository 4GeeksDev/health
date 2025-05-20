// sidebar_override.js
document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ sidebar_override.js cargado");

  const observer = new MutationObserver(() => {
    // 1. Cambia etiquetas del menú lateral
    document.querySelectorAll('.sidebar-item-label').forEach(label => {
      if (label.textContent.includes("ERPNext Settings")) {
        label.textContent = label.textContent.replace("ERPNext Settings", "Settings").trim();
      } else if (label.textContent.includes("ERPNext Integrations")) {
        label.textContent = label.textContent.replace("ERPNext Integrations", "4Geeks Integrations").trim();
      }
    });

    // 2. Cambia títulos del dashboard (más específico)
    document.querySelectorAll(".widget-title, .ellipsis").forEach(el => {
      if (el.textContent.includes("ERPNext")) {
        el.textContent = el.textContent.replace("ERPNext", "").trim();
      }
    });

    // ⚠️ Ya NO tocaremos todos los p, span y div indiscriminadamente
    // Esto evita errores por modificar estructuras internas de Frappe
  });

  // Observa solo el menú lateral y el contenido principal
  const sidebar = document.querySelector(".sidebar");
  const content = document.querySelector(".page-container");
  
  if (sidebar) {
    observer.observe(sidebar, { childList: true, subtree: true });
  }

  if (content) {
    observer.observe(content, { childList: true, subtree: true });
  }
});
