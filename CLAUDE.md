# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

SCAFFSS (Super Cool Awesome Framework For Static Sites) is a single-file Python static-site generator. The entire implementation lives in `src/scaffss.py` — there are no dependencies beyond the Python stdlib.

## Running

```
python3.12 src/scaffss.py -i <input-folder> -o <output-folder>
```

The `Makefile` is gitignored (per `.gitignore`) and holds personal-use targets (e.g. `make build-personal-website`), so it's not a stable interface — invoke the script directly when testing.

There are no tests, linters, or build steps.

## How the generator works

The input folder must contain two subfolders:
- `scaffold/` — the pages/assets that get walked and written to output (directory structure is mirrored)
- `components/` — snippets injected into scaffold pages

**Output is wiped first.** The script deletes everything under the output folder before writing. Point `-o` only at a dedicated build directory.

**Component injection** is a line-level textual substitution. A line containing `{{{ component_name.html }}}` is replaced by the contents of `components/component_name.html`. Key behaviors to preserve when editing:
- Only `.css` and `.html` files are processed; all other file types are copied verbatim via `shutil.copyfile`.
- The placeholder must be on its own line with both `{{{` and `}}}` present — multiple components per line are not supported, and partial-line substitutions aren't either.
- Each injected component line is prefixed with spaces matching the column of the opening `{` in the host line, so the component inherits the host's indentation.
- Components are not recursively expanded (a component containing `{{{ ... }}}` won't trigger a second pass).

**Variables** come from an optional `config.json` (a single JSON object) in the input folder. Any `{{ name }}` token (two braces, identifier name) in a `.html`/`.css` line, whether from a scaffold page or an injected component line, is replaced with `str(config[name])`. The regex excludes the three-brace include syntax. An unknown name exits with an error naming the file, so a typo never silently ships an empty value.
