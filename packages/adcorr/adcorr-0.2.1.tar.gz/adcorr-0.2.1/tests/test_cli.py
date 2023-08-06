import subprocess
import sys

from adcorr import __version__


def test_cli_version_shows_version():
    cmd = [sys.executable, "-m", "adcorr", "--version"]
    assert __version__ == subprocess.check_output(cmd).decode().strip()


def test_cli_help_shows_help():
    cmd = [sys.executable, "-m", "adcorr", "--help"]
    assert (
        subprocess.check_output(cmd)
        .decode()
        .strip()
        .startswith("Usage: python -m adcorr")
    )


def test_cli_noargs_shows_help():
    cmd = [sys.executable, "-m", "adcorr"]
    assert (
        subprocess.check_output(cmd)
        .decode()
        .strip()
        .startswith("Usage: python -m adcorr")
    )
