import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from copy_static_to_public import file_transfer
from generate_page import generate_pages_recursive

DOCS_PATH = Path("docs")
STATIC_PATH = Path("static")
FROM_PATH = Path("content")
TEMPLATE_PATH = Path("template.html")
BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():

    file_transfer(STATIC_PATH, DOCS_PATH)
    generate_pages_recursive(FROM_PATH, TEMPLATE_PATH, DOCS_PATH, BASE_PATH)

if __name__ == '__main__':
    main()
