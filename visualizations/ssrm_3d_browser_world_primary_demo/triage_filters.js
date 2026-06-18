(() => {
  const DEFECT_LEDGER_KEY = "ssrm_primary_demo_defect_ledger";
  const FILTER_KEY = "ssrm_primary_demo_defect_filter_state";
  const DEFAULT_FILTER = { status: "all", severity: "all" };

  const parseJson = (value, fallback) => {
    try {
      return value ? JSON.parse(value) : fallback;
    } catch (_error) {
      return fallback;
    }
  };

  const escapeText = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#39;",
  }[char]));

  const ensureStyles = () => {
    if (document.getElementById("triage-filter-styles")) return;
    const style = document.createElement("style");
    style.id = "triage-filter-styles";
    style.textContent = `
      .triage-filter-panel {
        margin-top: 1rem;
        padding: 1rem;
        border: 1px solid rgba(220, 238, 255, 0.2);
        border-radius: 18px;
        background: rgba(5, 13, 25, 0.5);
      }
      .triage-filter-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
      }
      .filter-pill {
        border: 1px solid rgba(150, 190, 220, 0.35);
        border-radius: 999px;
        padding: 0.45rem 0.8rem;
        background: rgba(255, 255, 255, 0.06);
        color: inherit;
        cursor: pointer;
      }
      .filter-pill.active {
        background: #d2f68d;
        border-color: #d2f68d;
        color: #142016;
        font-weight: 800;
      }
      .inline-filter {
        display: inline-flex;
        gap: 0.55rem;
        align-items: center;
        margin-bottom: 0.75rem;
        font-weight: 700;
      }
      .inline-filter select {
        border-radius: 10px;
        border: 1px solid rgba(220, 238, 255, 0.25);
        background: #071120;
        color: inherit;
        padding: 0.4rem 0.55rem;
      }
      .defect-ledger-view {
        display: grid;
        gap: 0.65rem;
        margin-top: 0.75rem;
      }
      .defect-row {
        border: 1px solid rgba(220, 238, 255, 0.16);
        border-radius: 14px;
        padding: 0.75rem;
        background: rgba(255, 255, 255, 0.045);
      }
      .defect-row header {
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem;
        align-items: center;
        margin-bottom: 0.4rem;
      }
      .defect-badge {
        border-radius: 999px;
        padding: 0.15rem 0.5rem;
        background: rgba(255, 255, 255, 0.08);
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }
      .defect-badge.open { background: rgba(255, 191, 112, 0.18); }
      .defect-badge.resolved { background: rgba(163, 244, 177, 0.18); }
      .empty-ledger {
        margin: 0;
        opacity: 0.78;
      }
    `;
    document.head.appendChild(style);
  };

  const readFilter = () => ({ ...DEFAULT_FILTER, ...parseJson(localStorage.getItem(FILTER_KEY), {}) });
  const writeFilter = (filter) => localStorage.setItem(FILTER_KEY, JSON.stringify(filter));
  const readLedger = () => {
    const ledger = parseJson(localStorage.getItem(DEFECT_LEDGER_KEY), []);
    return Array.isArray(ledger) ? ledger : [];
  };

  let filter = readFilter();

  const matchesFilter = (defect) => {
    const status = defect.status || "open";
    const severity = defect.severity || "watch";
    return (filter.status === "all" || filter.status === status)
      && (filter.severity === "all" || filter.severity === severity);
  };

  const render = () => {
    const summary = document.getElementById("triageFilterSummary");
    const view = document.getElementById("defectLedgerView");
    const severity = document.getElementById("defectSeverityFilter");
    const buttons = [...document.querySelectorAll("[data-triage-status]")];
    if (!summary || !view) return;

    buttons.forEach((button) => button.classList.toggle("active", button.dataset.triageStatus === filter.status));
    if (severity && severity.value !== filter.severity) severity.value = filter.severity;

    const ledger = readLedger();
    const filtered = ledger.filter(matchesFilter);
    const open = ledger.filter((defect) => (defect.status || "open") === "open").length;
    const resolved = ledger.filter((defect) => defect.status === "resolved").length;
    const blockingOpen = ledger.filter((defect) => (defect.status || "open") === "open" && defect.severity === "blocking").length;
    summary.textContent = `${filtered.length}/${ledger.length} shown | open ${open} | resolved ${resolved} | blocking open ${blockingOpen}`;

    if (!filtered.length) {
      view.innerHTML = '<p class="empty-ledger">No defects match the current reviewer filter.</p>';
      return;
    }

    view.innerHTML = filtered.map((defect) => {
      const status = escapeText(defect.status || "open");
      const severity = escapeText(defect.severity || "watch");
      const step = escapeText(defect.stepId || "unmapped");
      const note = escapeText(defect.note || "No note recorded.");
      const resolution = defect.resolutionNote ? `<p><strong>Resolution:</strong> ${escapeText(defect.resolutionNote)}</p>` : "";
      return `<article class="defect-row">
        <header>
          <strong>${escapeText(defect.id || "D-?")}</strong>
          <span class="defect-badge ${status}">${status}</span>
          <span class="defect-badge">${severity}</span>
          <span class="defect-badge">${step}</span>
        </header>
        <p>${note}</p>
        ${resolution}
      </article>`;
    }).join("");
  };

  const wire = () => {
    ensureStyles();
    const severity = document.getElementById("defectSeverityFilter");
    document.querySelectorAll("[data-triage-status]").forEach((button) => {
      button.addEventListener("click", () => {
        filter = { ...filter, status: button.dataset.triageStatus || "all" };
        writeFilter(filter);
        render();
      });
    });
    if (severity) {
      severity.value = filter.severity;
      severity.addEventListener("change", () => {
        filter = { ...filter, severity: severity.value || "all" };
        writeFilter(filter);
        render();
      });
    }
    ["recordDefect", "resolveLatestDefect"].forEach((id) => {
      const button = document.getElementById(id);
      if (button) button.addEventListener("click", () => window.setTimeout(render, 0));
    });
    window.addEventListener("storage", (event) => {
      if (event.key === DEFECT_LEDGER_KEY || event.key === FILTER_KEY) {
        filter = readFilter();
        render();
      }
    });
    render();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
