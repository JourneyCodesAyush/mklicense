import pytest
from mklicense.licenses import LICENSES


def test_mit_replaces_year():
    result = LICENSES["mit"].replace("[year]", "2026")
    assert "2026" in result

def test_mit_replaces_author():
    result = LICENSES["mit"].replace("[fullname]", "Ayush")
    assert "Ayush" in result

def test_gplv3_replaces_year():
    result = LICENSES["gplv3"].replace("[year]", "2026")
    assert "2026" in result

def test_gplv3_replaces_author():
    result = LICENSES["gplv3"].replace("[fullname]", "Ayush")
    assert "Ayush" in result

def test_apache2_replaces_year():
    result = LICENSES["apache2"].replace("[year]", "2026")
    assert "2026" in result

def test_apache2_replaces_author():
    result = LICENSES["apache2"].replace("[fullname]", "Ayush")
    assert "Ayush" in result
