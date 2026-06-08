import argparse
from datetime import datetime
from pathlib import Path

from mklicense.licenses import LICENSES


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
        choices=["mit", "unlicense", "gplv3", "apache2"],
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
