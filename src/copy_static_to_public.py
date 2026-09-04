import shutil
from pathlib import Path


def safe_delete(dir: Path) -> None:
    try:
        shutil.rmtree(dir)
        print(f"succesfully deleted contents in {dir}")
    except FileNotFoundError:
        print("Source file doesn't exist")

def move_files(src: Path, dest: Path) -> None:
    for file in src.iterdir():
        if file.is_dir():
            new_dir = dest / file.name
            move_files(file, new_dir)
        try:
            shutil.copy(file, dest)
            print(f"{file} succesfully copied to {dest}")
        except FileNotFoundError:
            print("Source file doesn't exist")

def file_transfer(src: Path, dest: Path) -> None:
    move_files(src, dest)
    safe_delete(src)