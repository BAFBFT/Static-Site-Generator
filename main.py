from pathlib import Path

from src.copy_static_to_public import file_transfer

PUBLIC_DIR = Path("public")
STATIC_DIR = Path("static")

def main():
    file_transfer(STATIC_DIR, PUBLIC_DIR)

if __name__ == '__main__':
    main()