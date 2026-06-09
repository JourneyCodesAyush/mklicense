# mklicense

![Python Version](https://img.shields.io/badge/python-3.14+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**mklicense** is a minimal CLI tool to generate license files for your projects.

> Generates a `LICENSE` file for your project from the command line, no browser needed.

---

## Quick Start

```powershell
git clone https://github.com/JourneyCodesAyush/mklicense.git
cd mklicense

uv sync
uv pip install -e . --link-mode=copy

mklicense mit "Your Name"
```

---

## Usage

```bash
mklicense [-h] [--year YEAR] [-d DIR] [{mit,unlicense,gplv3,apache2}] author
```

```bash
# Generate an MIT license for the current directory
mklicense mit "Ayush"

# Generate an Unlicense with a custom year
mklicense unlicense "Ayush" --year 2024

# Generate a license in a specific directory
mklicense mit "Ayush" --dir ./my-project
```

> [!NOTE]
> If a `LICENSE` file already exists in the target directory, `mklicense` will not overwrite it.

---

## Options

| Flag     | Default      | Description                            |
| -------- | ------------ | -------------------------------------- |
| `--year` | Current year | Year to use in the license             |
| `--dir`  | `.`          | Directory where `LICENSE` is generated |

---

## Supported Licenses

- `mit` — MIT License
- `unlicense` — The Unlicense (public domain)
- `gplv3` — GNU General Public License v3.0
- `apache2` — Apache License 2.0

---

## Development

Run tests:

```bash
uv run pytest
```

---

## Motivation

There is already a [mklicense](https://github.com/cezaraugusto/mklicense) written in JavaScript. It fetches license text from [choosealicense.com](https://choosealicense.com) at runtime — which ironically contradicts its own stated philosophy of not trusting external sources to store your license text.

This tool hardcodes the license text directly. No network calls, no external dependencies, works offline. Just stdlib.

---

## License

This project is licensed under the [**MIT License**](./LICENSE).
