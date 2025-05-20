// sidebar_override.js
document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ sidebar_override.js cargado");

  const observer = new MutationObserver(() => {
    // 1. Cambia etiquetas del menú lateral
    document.querySelectorAll('.sidebar-item-label').forEach(label => {
      if (label.textContent.includes("ERPNext")) {
        label.textContent = label.textContent.replace("ERPNext", "").trim();
      }
    });

    // 2. Cambia encabezados
    document.querySelectorAll("h4, h3, .widget-title, .ellipsis").forEach(h => {
      if (h.textContent.includes("ERPNext")) {
        h.textContent = h.textContent.replace("ERPNext", "").trim();
      }
    });

    // 3. Cambia párrafos, spans y divs
    document.querySelectorAll("p, span, div").forEach(p => {
      if (p.textContent.includes("ERPNext")) {
        p.textContent = p.textContent.replace(/ERPNext/g, "").trim();
      }
    });
  });

  // Observa cambios en todo el cuerpo del documento
  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
});
