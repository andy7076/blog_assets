# Neon Comet Runner

A self-contained mobile-first browser game built with pure HTML, CSS, and JavaScript.

## Run locally

Open `index.html` directly in a browser:

```bash
xdg-open /root/.hermes/workspaces/mobile-rush-game/index.html
```

Or serve the folder with any static server:

```bash
cd /root/.hermes/workspaces/mobile-rush-game
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Controls

- Touch anywhere and slide; the comet moves by the same drag amount instead of jumping under your finger.
- Dodge meteors and collect energy shards.
- Double tap, press the dash button, Space, or Shift to activate slow-motion dash.
- Use the pause button or Escape to pause.

High score is saved in `localStorage` on the device/browser.
