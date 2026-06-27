# Neon Comet Runner

A self-contained mobile-first neon space shooter built with pure HTML, CSS, and JavaScript. The game is now level-based: survive each wave, fill the level meter, then defeat a distinct boss to advance.

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
- Each level starts with a wave phase. The level meter fills over time and faster when you destroy meteors.
- At 100%, normal wave spawning stops and a named boss arrives with a large health bar.
- Bosses move across the top of the screen, take bullet damage, fire projectiles, and summon extra meteors.
- Defeat a boss for a score bonus, clear feedback, reward powerups, and a short transition into the next harder level.
- Move across almost the full portrait screen, with margins for the HUD and dash button.
- Destroyed meteors explode into particles, score, and occasional powerups.
- Collect falling powerups: spread shot, rapid fire, shield, magnet, and score boost.
- Energy shards still raise combo, add points, and recharge dash.
- Double tap, press the dash button, Space, or Shift to activate slow-motion dash. Shield and slow dash can phase through meteors, boss contact, and boss projectiles.
- Use the pause button or Escape to pause.

High score is saved in `localStorage` on the device/browser.
