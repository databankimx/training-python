# Leveling Up

## What this step does

Each time the player clears a fleet, the game gets faster. The ship, the bullets and the aliens all
speed up by the same factor, so each new fleet is a little harder than the last.

Starting a new game puts the speeds back to their first values. Without that, each new game would
begin at the speed the previous one finished on.

To make this work, `settings.py` is split into two groups. Static settings stay the same for the whole
run. Dynamic settings change during play, and are reset at the start of each game.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch14 3 --run
```

Click Play. Clear a fleet to see the game speed up. Press Q to quit.

## The code

`settings.py` is reorganized. The static settings are set in `__init__()`, and the speeds that change
during play are set in `initialize_dynamic_settings()`:

```python
class Settings:
    --snip--

    def __init__(self) -> None:
        """Initialize the game's static settings."""
        --snip--
        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self) -> None:
        """Increase the speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
```

`alien_invasion.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
class AlienInvasion:
    --snip--

    def _check_play_button(self, mouse_pos: tuple[int, int]) -> None:
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            --snip--

    def _check_bullet_alien_collisions(self) -> None:
        """Respond to bullet-alien collisions, and create a new fleet when the fleet is destroyed."""
        --snip--
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

            # Speed up the game for the next fleet.
            self.settings.increase_speed()
```

What changed:

- `settings.py` has a `speedup_scale` setting, set to 1.1.
- `initialize_dynamic_settings()` sets the ship, bullet and alien speeds, and the fleet direction. It's
  called when `__init__()` runs, and again each time a new game starts.
- `increase_speed()` is new. It multiplies the ship, bullet and alien speeds by `speedup_scale`.
- `_check_play_button()` resets the dynamic settings before it resets the statistics.
- `_check_bullet_alien_collisions()` calls `increase_speed()` when the fleet has been cleared.

## Walkthrough

**Static and dynamic.** The static settings stay the same for the whole run, such as the screen size and
the number of ships. The dynamic settings are the ones that change, so they're kept in their own method.
That lets the game set them back to their first values without touching anything else.

**The speed-up factor.** `speedup_scale` controls how fast the game gets harder. At 2, each new fleet
would be twice as fast as the one before it. At 1, the speed would never change. A value like 1.1 makes
the game harder without making it impossible. If the game is too hard too quickly, lower the value. If
it's too easy, raise it a little.

**The fleet direction.** `fleet_direction` is reset along with the other dynamic settings, so the fleet
always moves right at the start of a new game.

**Drop speed.** `fleet_drop_speed` isn't increased. When the aliens move faster across the screen, they
reach the edge sooner, and so they also drop down sooner.

**Resetting the speeds.** Without the reset in `_check_play_button()`, every new game would start with
the speeds from the previous one.

## Output

The game starts at the same speed as before. Each time you clear a fleet, the ship, bullets and aliens
move a little faster.

## Changed files

- `settings.py`: splits the static and dynamic settings, and adds `speedup_scale` and `increase_speed()`
- `alien_invasion.py`: resets the dynamic settings on Play, and speeds the game up when a fleet is cleared
