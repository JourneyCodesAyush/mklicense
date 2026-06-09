import sys
from pathlib import Path
import pytest
from mklicense.__main__ import main

def test_license_file_created(tmp_dir):
    sys.argv = ["mklicense", "mit", "Ayush", "--dir", tmp_dir]
    main()
    assert (Path(tmp_dir) / "LICENSE").is_file()

def test_license_file_content(tmp_dir):
    sys.argv = ["mklicense", "mit", "Ayush", "--dir", tmp_dir]
    main()
    content = (Path(tmp_dir) / "LICENSE").read_text()
    assert "Ayush" in content

def test_existing_license_not_overwritten(tmp_dir):
    license_path = Path(tmp_dir) / "LICENSE"
    license_path.write_text("original")
    sys.argv = ["mklicense", "mit", "Ayush", "--dir", tmp_dir]
    main()
    assert license_path.read_text() == "original"

def test_invalid_dir_returns_early(tmp_dir, capsys):
    sys.argv = ["mklicense", "mit", "Ayush", "--dir", "/nonexistent/path"]
    main()
    captured = capsys.readouterr()
    assert "does NOT exist" in captured.out
