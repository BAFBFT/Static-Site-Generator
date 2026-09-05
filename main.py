import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from copy_static_to_public import file_transfer
from generate_page import generate_page

PUBLIC_PATH = Path("public")
STATIC_PATH = Path("static")
FROM_PATH = Path("content/index.md")
TEMPLATE_PATH = Path("template.html")
DEST_PATH = Path("public/index.html")

def main():
    file_transfer(STATIC_PATH, PUBLIC_PATH)
    generate_page(FROM_PATH, TEMPLATE_PATH, DEST_PATH)

if __name__ == '__main__':
    main()
