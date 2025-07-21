import subprocess
import tempfile
import os
import pytest


def write_temp_file(content="Line one\nLine two\n"):
    temp = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
    temp.write(content)
    temp.close()
    return temp.name


def test_cli_default_output():
    filepath = write_temp_file()
    result = subprocess.run(["python3", "unix_wc.py", filepath], capture_output=True, text=True)
    assert result.returncode == 0
    parts = result.stdout.strip().split()
    assert len(parts) == 4
    os.remove(filepath)


@pytest.mark.parametrize("flag,expected_value", [
    ("-l", "2"),
    ("--lines", "2"),
    ("-w", "4"),
    ("--words", "4"),
    ("-m", "19"),  # Includes \n
    ("--chars", "19"),
])
def test_cli_flags(flag, expected_value):
    filepath = write_temp_file("one two\nthree four\n")
    result = subprocess.run(["python3", "unix_wc.py", flag, filepath], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == expected_value
    os.remove(filepath)


def test_cli_invalid_path():
    result = subprocess.run(["python3", "unix_wc.py", "nonexistent.txt"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "No such file" in result.stderr or "Error" in result.stderr
