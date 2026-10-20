# Making a Game (Alien Invasion)

This project follows chapters 12 to 14 of *Python Crash Course* (3rd edition). It builds a
game with Pygame, one step at a time.

## Layout

Each chapter has the same structure as the chapters in Part I.

```
alien-invasion/
  build_stage.py
  final/                        the finished game from chapter 14, step 06, with its own README
  ch12-a-ship-that-fires-bullets/
    lessons/
      01-window-and-events/   alien_invasion.py, lesson.md, lesson-images/
      02-frame-rate/          alien_invasion.py, lesson.md, lesson-images/
      ...
      17-limit-bullets/      alien_invasion.py, settings.py, lesson.md, lesson-images/
      18-fullscreen-optional/ alien_invasion.py, lesson.md
    try-it-yourself/
      lesson.md
      12-1-blue-sky/          blue_sky.py, settings.py, lesson.md, lesson-images/
      12-2-game-character/    character.py, game_character.py, settings.py, images/, lesson.md
      12-4-rocket/            rocket.py, rocket_game.py, settings.py, images/, lesson.md
      12-5-keys/              keys.py, lesson.md, lesson-images/
      12-6-sideways-shooter/  rocket.py, missile.py, settings.py, sideways_shooter.py,
                              images/, lesson.md, lesson-images/
    textbook-downloads/
      2nd-edition/lessons/    the book's downloads, unchanged
      3rd-edition/lessons/    the book's downloads, unchanged
      3rd-edition/try-it-yourself/   the book's exercise downloads, unchanged
  ch13-aliens/
    lessons/                    01-creating-the-first-alien through
                                09-aliens-reach-bottom-and-game-over
    try-it-yourself/            13-1 to 13-6
    textbook-downloads/         the book's downloads, unchanged
  ch14-scoring/
    lessons/                    01-adding-the-play-button through
                                06-level-and-ships
    try-it-yourself/            14-1 to 14-8
                                (14-7 needs its images/ and sounds/ folders copied in)
    textbook-downloads/         the book's downloads, unchanged
```

- **Step folders** under `lessons` hold the files that step adds or changes, and the lesson.
  Nothing is repeated across steps, so the repo keeps one copy of each file.
- **`lesson-images`** holds screenshots that appear in a lesson. The build never copies it.
- **`images`** holds game assets. The build copies it. The 14-7 animations are copied in from the 3rd Edition
  folder, as described on its lesson page.
- **`sounds`** holds the 14-7 sound files, which are copied in from the same place as the downloads.
- **`try-it-yourself`** holds the chapter's exercises. Each one is a standalone program.
- **`textbook-downloads`** holds the book's own files, copied without changes. Nothing in it
  is edited.

### Lesson format

- Step 1 of each chapter shows its full file. Later steps show only the changed code, with
  `--snip--` for the code that stays the same, followed by a list of what changed.
- A new file is shown in full.
- `#pylint` and `#NOSONAR` comments are left out of lesson code. They stay in the files.
- Each lesson has a **Running this step** section with the command for that step.
- Each lesson's **Output** section shows the result, with a screenshot where one is needed.

A step folder whose name ends in `-optional` is built only when you build its own chapter. It isn't
carried into later chapters.

## Building a stage

`build_stage.py` builds the project as it stands after a chapter and step. It copies every
earlier chapter, then the steps of the named chapter up to and including the step you name.

To see the project after chapter 12, step 17:

```pwsh
cd C:\Development\training\training-python\part-ii-projects\making-a-game\alien-invasion
python build_stage.py ch12 17 --run
```

To build without running, leave out `--run`. The build goes into `build\ch12-step-17`.

To list every chapter and step:

```pwsh
python build_stage.py --list
```

The `build\` folder is temporary, and it should not be committed.

## Requirements

Pygame, with a working sound device for the music and sound effects. Install it once with
`python -m pip install pygame`.
