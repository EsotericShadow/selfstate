# SSRM-3D Primary Browser World Demo

This directory is the stable launcher for the maintained browser-world app shell.
It was created by Report 303 to stop scattering review attention across older
bridge artifacts.

Use:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html`.

The launcher targets `../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`. It does not implement a second world.

The launcher includes a browser-local manual pass recorder, defect ledger, and
triage workflow. Defects can be tied to manual steps, marked by severity, moved
from open to resolved with a resolution note, and exported as public local review
evidence.

Boundary: Primary demo packaging for the deterministic browser-local maintained app shell only; no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous natural language, no moral patienthood, no production persistence, no finished gameplay, no complete 3D engine, and no metaphysical frequency claim.
