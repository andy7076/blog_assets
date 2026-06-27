# 雷霆突击 Thunder Strike

Mobile-first vertical arcade shooter built from scratch in one self-contained HTML file. It uses pure HTML, CSS, and JavaScript with no external libraries or build tools.

## Local Run

Open `index.html` directly in a browser:

```bash
xdg-open /root/.hermes/workspaces/thunder-strike/index.html
```

Or serve the folder locally:

```bash
cd /root/.hermes/workspaces/thunder-strike
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Controls

- Mobile: drag anywhere on the playfield. The fighter follows by relative offset so the finger does not cover the ship.
- Desktop: drag, or use WASD/arrow keys. Space triggers Bomb. Escape pauses.
- Auto-fire is always enabled.

## Features

- Chinese-first UI with English toggle.
- Menu, playing, paused, and game-over state machine.
- Wave, boss, and clear phase flow.
- Enemy waves with scouts, strikers, tanks, and drones.
- Boss fights with three rotating boss identities and projectile patterns.
- Powerups: Spread, Laser, Rapid, Shield, Magnet, and Bomb.
- Score, combo, lives, HP, local high score, particles, hitbox indicator, and mobile haptics when available.

## Public Deployment

This project is static. Deploy the folder as-is to any static host:

- GitHub Pages
- Netlify
- Vercel static project
- Cloudflare Pages
- Any CDN or web server that can serve `index.html`

No build command is needed. The publish directory is:

```text
/root/.hermes/workspaces/thunder-strike
```
