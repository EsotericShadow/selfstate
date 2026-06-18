const HANDOFF_KEY = 'ssrm_primary_demo_handoff';

function recordLaunch(kind) {
  const payload = {
    kind,
    report: 303,
    target: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'primary-demo-launcher-only'
  };
  localStorage.setItem(HANDOFF_KEY, JSON.stringify(payload));
  renderHandoff(payload);
}

function renderHandoff(payload) {
  const node = document.getElementById('handoffStatus');
  if (!node) return;
  node.textContent = `Last handoff: ${payload.kind} launch toward ${payload.target} at ${payload.recordedAt}.`;
}

for (const [id, kind] of [['cleanLaunch', 'clean'], ['resumeLaunch', 'resume']]) {
  const node = document.getElementById(id);
  if (node) node.addEventListener('click', () => recordLaunch(kind));
}

try {
  const existing = JSON.parse(localStorage.getItem(HANDOFF_KEY) || 'null');
  if (existing) renderHandoff(existing);
} catch (error) {
  localStorage.removeItem(HANDOFF_KEY);
}
