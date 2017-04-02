# Steve's Pyglet development and packaging experiments

## Prerequisites

Must have Python installed with dylib! For pyenv, that means:

```sh
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.5.1
```

## Usage

* `make run`: Run the game. When the game exits, run it again. Update this
  target to point to whatever you're working on at the moment.
* `make dist`: Generate an executable with PyInstaller.
