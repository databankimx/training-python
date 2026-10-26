# Running the Game in Fullscreen Mode

## What this step does

Pygame has a fullscreen mode. Some games look better full screen, and some run more smoothly.
This step is optional. It's the only fullscreen example in the project, and it's the last step
in this chapter. Chapter 13 continues from step 17, in a window, so skip this step if you want
the windowed game.

Instead of a fixed window size, the screen now takes the size of the monitor. Because the size
isn't known until the screen exists, the settings are updated from the screen after it's created.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 18 --run
```

Press Q to quit. Pygame has no default way to close a fullscreen window, so make sure Q works
before you run the game this way.

## The code

`alien_invasion.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
class AlienInvasion:
    --snip--

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        --snip--
```

What changed:

- The screen is created with a size of `(0, 0)` and the `pygame.FULLSCREEN` flag. Pygame then
  chooses a size that fills the screen.
- The screen's width and height are copied into `self.settings`, so the rest of the game uses
  the real size.
- Nothing else changes. The ship and bullets already read their positions from the screen and
  the settings.

## Walkthrough

**Size (0, 0).** Passing zero for the width and height asks Pygame to pick a size that fills the
screen. The `pygame.FULLSCREEN` flag makes the window fullscreen.

**Updating the settings.** `self.screen.get_rect()` gives the rect of the screen that was just
created. Its `width` and `height` are the real screen size, and we store them in `self.settings`.

**Going back to a window.** If you prefer the game in its own window, change the call back to
`pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))` and set the
width and height in `settings.py`. Then the screen size is fixed again.

## Output

The game fills the monitor. The ship sits at the bottom center of the screen, and the bullets
travel up it. The screen looks the same as in the last step, only larger.

## Chapter summary

This chapter built Alien Invasion's first playable version, one step at a time. Here is what the
finished project does, and the ideas behind it.

**The window and the loop.** The game is a class, `AlienInvasion`, that opens a window and runs a
loop. Each pass through the loop does four things: it checks for events, updates the game, draws
the screen, and waits so the frame rate stays steady. `pygame.event.get()` reports key presses
and window events, and `pygame.display.flip()` makes the drawn screen visible.

**Settings in one place.** The screen size, colors, speeds and bullet values live in
`settings.py`. Changing the game's behavior means editing that file, not searching through the
code.

**Classes for the parts of the game.** `Ship` holds the ship's image, position and movement.
`Bullet` holds a bullet's rectangle, position and speed. Each class has its own file, and the main
class puts them together.

**Rects and positions.** Pygame draws images and checks their edges through a rect. A rect stores
whole pixels, so the ship and the bullets keep their exact positions as decimal numbers, and copy
them into the rect each frame. That's why movement is smooth at fractional speeds.

**Input as flags.** A key press turns a movement flag on, and a key release turns it off. The
ship reads the flags in `update()` on every frame. This keeps input handling separate from
movement, so holding two keys works, and the ship stops when a key is released.

**Groups and cleanup.** Bullets are kept in a `pygame.sprite.Group`, which updates and draws them
all at once. A bullet that leaves the screen is removed, so the game doesn't keep track of
bullets nobody can see. The number of bullets on screen is limited, which is part of the game's
challenge.

**Keeping the code tidy.** Refactoring moved the event handling and the drawing into their own
methods. Each method does one job, which makes the main loop easy to read and each part easy to
change.

**Testing ideas on the way.** Each step was small enough to run and check. The exercises apply
the same ideas to new programs: a blue window, a character, a rocket that moves in four
directions, printing key codes, and a sideways shooter.

The next chapter adds aliens. The ship and bullets you have now are the base for that work.

---
