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
uv run poe gen       # regenerate the Ingredients catalogue from data/ingredients/
```

`serve` and `build` run `gen` first, so the auto-generated
[Ingredients catalogue](docs/ingredients/index.md) always mirrors the YAML in
[`data/ingredients/`](data/ingredients/).

## Structure

- `docs/` — the Markdown pages (`ingredients/index.md` is **generated** — don't
  edit by hand).
- `data/ingredients/` — the board catalogue, single source of truth (YAML).
- `scripts/build_ingredients.py` — generates the Ingredients page from the YAML.
- `zensical.toml` — site config, theme, and navigation.
- `docs/stylesheets/extra.css` — the "bumblebee" pixi.sh-style layout.

See [Contributing](docs/contributing.md) for how to add boards and recipes.
