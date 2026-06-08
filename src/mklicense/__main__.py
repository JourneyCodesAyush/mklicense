import argparse
from datetime import datetime
from pathlib import Path

LICENSES: dict[str, str] = {
    "mit": """MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    "unlicense": """This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
""",
}


def valid_year(value: str) -> int:
    year: int = int(value)
    if year < 1970 or year > datetime.now().year:
        raise argparse.ArgumentTypeError(f"Invalid year: {value}")

    return year


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to generate licenses for your projects."
    )

    parser.add_argument(
        "license",
        choices=["mit", "unlicense"],
        nargs="?",
        help="License type to add to the project",
    )
    parser.add_argument(
        "--year",
        type=valid_year,
        default=datetime.now().year,
        help="Year of the license",
    )
    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=".",
        help="Directory where license file is generated",
    )
    parser.add_argument("author", help="The name of the author")

    args = parser.parse_args()

    license: str = LICENSES[args.license]
    license = license.replace("[year]", str(args.year))
    license = license.replace("[fullname]", args.author)

    if not (Path(args.dir).is_dir()):
        print(f"{args.dir} does NOT exist")
        return

    LICENSE_PATH: Path = Path(args.dir) / "LICENSE"
    if LICENSE_PATH.is_file():
        print(f"{LICENSE_PATH} already exists.")
        return

    with open(str(LICENSE_PATH), "w") as f:
        f.write(license)
    print(f"Created {LICENSE_PATH}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{str(e)}")
