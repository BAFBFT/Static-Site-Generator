import shutil
from pathlib import Path


def safe_delete(dir: Path) -> None:
    try:
        for subdir in dir.iterdir():
            if subdir.is_file():
                subdir.unlink()
                continue
            shutil.rmtree(subdir)
        print(f"succesfully deleted contents in {dir}")
    except FileNotFoundError:
        print("Source file doesn't exist")

def move_files(src: Path, dest: Path) -> None:
    for file in src.iterdir():
        if file.is_dir():
            new_dir = dest / file.name
            new_dir.mkdir()
            move_files(file, new_dir)
            continue
        try:
            shutil.copy(file, dest)
            print(f"{file} succesfully copied to {dest}")
        except FileNotFoundError:
            print("Source file doesn't exist")

def file_transfer(src: Path, dest: Path) -> None:
    safe_delete(dest)
    move_files(src, dest)
