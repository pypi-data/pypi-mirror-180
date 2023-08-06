import requests
import gzip
import shutil

from typing import Literal
from pathlib import Path

HOME = Path.home()

REPO = "https://github.com/zakird/wkhtmltopdf_binary_gem"

VERSIONS = [
    "archlinux_amd64",
    "centos_6_amd64",
    "centos_6_i386",
    "centos_7_amd64",
    "centos_7_i386",
    "centos_8_amd64",
    "debian_10_amd64",
    "debian_10_i386",
    "debian_9_amd64",
    "debian_9_i386",
    "macos_cocoa",
    "ubuntu_16.04_amd64",
    "ubuntu_16.04_i386",
    "ubuntu_18.04_amd64",
    "ubuntu_18.04_i386",
    "ubuntu_20.04_amd64",
    "ubuntu_22.04_amd64",
]


def wkhtmltopdf_bin(
    version: Literal[tuple(VERSIONS)] = "ubuntu_22.04_amd64",
    final_path: Path = HOME,
    final_name: str = "wkhtmltopdf",
):
    if version not in VERSIONS:
        raise ValueError("Please choose a valid version to download")

    filename = f"wkhtmltopdf_{version}.gz"
    url = f"{REPO}/blob/master/bin/{filename}?raw=true"
    gz_path = HOME / filename
    bin_path = final_path / final_name

    r = requests.get(url, stream=True)

    if gz_path.is_file():
        gz_path.unlink()
    with open(gz_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    if bin_path.is_file():
        bin_path.unlink()
    with gzip.open(gz_path, "rb") as f_in:
        with open(bin_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    gz_path.unlink()

    return str(bin_path)


wkhtmltopdf_path = wkhtmltopdf_bin()
