# My funground sketchbook

A place to keep your [funground](https://funground-hq.github.io) sketches on GitHub. You can write
them, run them and save them in your browser, with nothing to install, and run the same files on
your own computer too.

## Make your own copy

1. Sign in to GitHub.
2. Press **Use this template**, then **Create a new repository**. Give it a name, such as
   `sketchbook`. A public repository lets you share your sketches with a link.

## Write and run sketches in your browser

1. On your new repository's page, press the **.** key (full stop). The page becomes an editor: this is
   github.dev, GitHub's own editor.
2. The first time only, add the **funground** extension to the editor: open the Extensions view (the
   four squares on the left), search for **funground** and press **Install**.
   *Not yet possible: the extension is waiting to be published in the Visual Studio Marketplace. Until
   then, the steps below are for testers who serve it from their own computer
   ([how](https://github.com/funground-hq/funground-web/tree/main/vscode-extension#try-it-in-githubdev-or-vscodedev-before-it-is-published)).*
3. Open a sketch from the `sketches` folder, for example `first_sketch.py`.
4. Press **Ctrl+Enter** (**Cmd+Enter** on a Mac), or the ▷ button at the top right. A panel opens
   beside your code and the sketch runs in it. The first time takes a few seconds, while Python loads
   into the page.
5. Change the code. The sketch runs again a moment after you stop typing. If something is wrong, the
   panel shows the error and the line is underlined in red.

The panel runs your code in a part of the page of its own, so a sketch can never use your GitHub account.

## Save your work

Saving is GitHub's own: open **Source Control** (the branch icon on the left), write a few words about
what you changed, and press **Commit & Push**. Your sketch is now saved in your repository.

## What is here

| | |
|---|---|
| `sketches/` | Your sketches. Start with `first_sketch.py`, `bounce.py`, `mouse.py`. Add your own: any `.py` file that uses funground |
| `sketches/data/` | Pictures and sounds your sketches load, such as `f.load_image("data/photo.png")` in `photo.py`, and the tune `hear_and_see.py` plays |
| `sketches/palette.py` | Not a sketch: colours that `pattern.py` uses with `import palette`. Change them and run `pattern.py` again |

## Run the same sketches on your computer

Install Python and funground ([Get started](https://funground-hq.github.io/get-started/)), download your
repository (the green **Code** button, then **Download ZIP**, or `git clone`), and run a sketch:

    python sketches/first_sketch.py

## What does not work in the browser yet

- The microphone: sketches that listen need your computer (or the [Play](https://funground-hq.github.io/play/)
  page on the funground website).
- A few things only a computer has, such as your own installed fonts (`f.system_font()`) and saving
  videos (`.mp4`). funground tells you when you use one.

This is a preview of funground 0.2, made for Chrome first.

## Licence

The sketches and the files in `sketches/data/` are free to use for anything (CC0, see `LICENSE`).
The funground extension is free software under the LGPL 2.1 only; its code is at
[funground-hq/funground-web](https://github.com/funground-hq/funground-web).
