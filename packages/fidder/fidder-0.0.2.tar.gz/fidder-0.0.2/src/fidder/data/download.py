import os
import shutil
import subprocess
from pathlib import Path

from .._cli import cli


@cli.command(name="download", no_args_is_help=True)
def download_training_data(output_directory: Path):
    """Download training data from Zenodo."""
    subprocess.run(
        [
            "zenodo_get",
            "7104305",
            "--output-dir",
            str(output_directory),
        ]
    )
    zipped_archive = output_directory / "tilt_images_with_fiducials.zip"
    shutil.unpack_archive(
        zipped_archive,
        extract_dir=output_directory,
    )
    os.remove(zipped_archive)
