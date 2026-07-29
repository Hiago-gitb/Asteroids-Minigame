# Asteroids 🚀

A classic Asteroids arcade game clone built with Python and Pygame.

Control a triangular spaceship, dodge and destroy asteroids as they fly across the screen. Each asteroid splits into smaller, faster pieces until it's small enough to be destroyed entirely.

![Python](https://img.shields.io/badge/python-3.13-blue?logo=python)
![Pygame](https://img.shields.io/badge/pygame-2.6.1-purple?logo=pygame)

## Controls

| Key     | Action          |
| ------- | --------------- |
| `W`     | Thrust forward  |
| `S`     | Thrust backward |
| `A`     | Rotate left     |
| `D`     | Rotate right    |
| `Space` | Shoot           |

## Features

- **Infinite asteroid field** — Asteroids continuously spawn from all four edges of the screen.
- **Destructible asteroids** — Large asteroids split into two medium ones; medium asteroids split into two small ones; small asteroids are destroyed.
- **Shooting cooldown** — Fire rate is capped at 0.3 seconds between shots.
- **Collision detection** — Crashing into an asteroid ends the game.
- **Game logging** — Game state and key events are logged in JSONL format for analysis and debugging.

## How to Run

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Using uv

```bash
uv run main.py
```

### Using pip

```bash
pip install pygame==2.6.1
python main.py
```

## Project Structure

| File               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `main.py`          | Game loop, sprite group setup, and event handling         |
| `player.py`        | Player ship — movement, rotation, and shooting            |
| `asteroid.py`      | Asteroid behavior — movement and splitting on destruction |
| `asteroidfield.py` | Spawns asteroids at random intervals from screen edges    |
| `shot.py`          | Projectile fired by the player                            |
| `circleshape.py`   | Base class for all circular sprites (collision detection) |
| `constants.py`     | Tuning constants — speeds, sizes, spawn rates, etc.       |
| `logger.py`        | JSONL logging of game state and events for debugging      |

## Constants (tunable in `constants.py`)

| Constant              | Value | Description                       |
| --------------------- | ----- | --------------------------------- |
| `SCREEN_WIDTH`        | 1280  | Window width                      |
| `SCREEN_HEIGHT`       | 720   | Window height                     |
| `PLAYER_TURN_SPEED`   | 300   | Degrees per second                |
| `PLAYER_SPEED`        | 200   | Pixels per second                 |
| `PLAYER_SHOOT_SPEED`  | 500   | Bullet speed                      |
| `ASTEROID_SPAWN_RATE` | 0.8s  | Seconds between spawns            |
| `ASTEROID_MIN_RADIUS` | 20    | Smallest asteroid size            |
| `ASTEROID_KINDS`      | 3     | Size tiers (small, medium, large) |

## Built With

- [Pygame](https://www.pygame.org/) — The cross-platform set of Python modules for writing video games.
- [uv](https://docs.astral.sh/uv/) — Fast Python package and project manager.

