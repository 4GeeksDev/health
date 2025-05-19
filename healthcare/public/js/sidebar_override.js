frappe.ready(() => {
  const observer = new MutationObserver(() => {
    // 1. Elimina la palabra "ERPNext" de las etiquetas del menú lateral
    const labels = document.querySelectorAll('.sidebar-item-label');
    labels.forEach(label => {
      if (label.textContent.includes("ERPNext")) {
        label.textContent = label.textContent.replace("ERPNext", "").trim();
      }
    });

    // 2. Elimina "ERPNext" de títulos (h3, h4, etc.) y algunos encabezados de widgets
    const headers = document.querySelectorAll("h4, h3, .widget-title, .ellipsis");
    headers.forEach(h => {
      if (h.textContent.includes("ERPNext")) {
        h.textContent = h.textContent.replace("ERPNext", "").trim();
      }
    });

    // 3. También elimina "ERPNext" de párrafos, spans y divs (por si se repite en otro lugar)
    const paragraphs = document.querySelectorAll("p, span, div");
    paragraphs.forEach(p => {
      if (p.textContent.includes("ERPNext")) {
        p.textContent = p.textContent.replace(/ERPNext/g, "").trim();
      }
    });
  });

  // Observa cambios en todo el `body`, incluso elementos que se carguen dinámicamente (como el sidebar)
  observer.observe(document.body, { childList: true, subtree: true });
});
