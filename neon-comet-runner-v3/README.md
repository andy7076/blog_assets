# Neon Comet Runner

A self-contained mobile-first neon space shooter built with pure HTML, CSS, and JavaScript.

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

- Touch anywhere and slide; the ship uses anchored relative drag, so it moves from its current position and never jumps under your finger.
- The ship fires automatically while playing. Keep the bullet stream on meteors to break their HP before they reach you.
- Move across almost the full portrait screen, with margins for the HUD and dash button.
- Destroyed meteors explode into particles, score, and occasional powerups.
- Collect falling powerups: spread shot, rapid fire, shield, magnet, and score boost.
- Energy shards still raise combo, add points, and recharge dash.
- Double tap, press the dash button, Space, or Shift to activate slow-motion dash.
- Use the pause button or Escape to pause.

High score is saved in `localStorage` on the device/browser.
