<p align="center">
  <img src="docs/assets/logo.png" width="160">
</p>

# BeeHive documentation

The documentation site for [BeeHive](https://github.com/BeeHive-org/BeeHive) —
a flexible open electronics platform for building research equipment and
teaching electronics.

Built with [Zensical](https://zensical.org/) and managed with
[uv](https://docs.astral.sh/uv/).

## Develop

```bash
uv sync              # install dependencies
uv run poe serve     # live-reload preview at http://127.0.0.1:8000
uv run poe build     # build the static site into ./site
uv run poe gen       # regenerate the Ingredients catalogue from docs/data/ingredients/
uv run poe sync      # refresh the vendored board BOMs from the BeeHive repo
```

`serve` and `build` run `gen` first, so the auto-generated
[Ingredients catalogue](docs/ingredients/index.md) always mirrors the YAML in
[`docs/data/ingredients/`](docs/data/ingredients/).

Board bills-of-materials are pulled from the BeeHive hardware repo's
`kitspace.yaml` and **vendored** into [`docs/data/kitspace/`](docs/data/kitspace/)
so builds stay offline. Run `uv run poe sync` occasionally (and commit the
result) to refresh them; `gen` reads the vendored copy and never needs the
network.

## Structure

Everything the site needs lives under `docs/`, so it can be dropped into another
repository as a self-contained folder:

- `docs/` — the Markdown pages (`ingredients/*.md` is **generated** — don't edit
  by hand).
- `docs/data/ingredients/` — the board catalogue, single source of truth (YAML).
- `docs/data/kitspace/` — vendored board BOMs (from `uv run poe sync`).
- `docs/scripts/build_ingredients.py` — generates the Ingredients pages.
- `docs/scripts/sync_kitspace.py` — refreshes the vendored BOMs.
- `zensical.toml` — site config, theme, and navigation.
- `docs/stylesheets/extra.css` — the "bumblebee" pixi.sh-style layout.

See [Contributing](docs/contributing.md) for how to add boards and recipes.
