---
title: Contributing
description: How to contribute boards, recipes, and fixes to BeeHive.
---

# Contributing

BeeHive is open source and community-driven. Contributions aren't confined to
one institution — anyone can add a board, share a recipe, or improve the docs.

## Ways to contribute

- 🧩 **A new board (ingredient).** Design a daughter board that follows the
  [design rules](introduction/design-rules.md) and share it. See
  [Build your own board](techniques/build-your-own-board.md).
- 🍯 **A new recipe.** Built an instrument with BeeHive? Document it as a recipe
  so others can reproduce it — especially outside neuroscience.
- 🐛 **Fixes & improvements.** Corrections to boards, code, or these docs are all
  welcome.

## Adding a board to the catalogue

The [Ingredients catalogue](ingredients/index.md) is generated from YAML — you
don't edit the page directly:

1. Add an entry to `data/ingredients/boards.yaml` (or drop in a new
   `data/ingredients/<board>.yaml`).
2. Run `uv run poe gen` to regenerate the catalogue.
3. Preview with `uv run poe serve`.

See the comments at the top of `boards.yaml` for the field reference. If the
board has a project in the [BeeHive repo's](https://github.com/BeeHive-org/BeeHive)
`kitspace.yaml`, add its `kitspace:` key too — `uv run poe sync` then vendors the
board's bill of materials and fabrication-file links into the catalogue.

## Editing the docs

The docs are a [Zensical](https://zensical.org/) site managed with
[uv](https://docs.astral.sh/uv/):

```bash
uv sync                 # install dependencies
uv run poe serve        # live-reload preview at http://127.0.0.1:8000
uv run poe build        # build the static site into ./site
```

`serve` and `build` regenerate the Ingredients catalogue first, so it always
matches the YAML.

## Get in touch

- Issues & discussion:
  [github.com/BeeHive-org/BeeHive/issues](https://github.com/BeeHive-org/BeeHive/issues)
- Email: [a.maia-chagas@sussex.ac.uk](mailto:a.maia-chagas@sussex.ac.uk)

If in doubt — reach out. We're glad to help.
