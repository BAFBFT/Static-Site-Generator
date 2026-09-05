import re
from pathlib import Path

from markdown_to_html_node import markdown_to_html_node

HEADING_PATTERN = re.compile(r"#{1} .+")

def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()
    for line in lines:
        if HEADING_PATTERN.fullmatch(line):
            return line[2:].strip()
    raise ValueError("no h1 heading found")


def generate_page(from_path: Path, template_path: Path, dest_path: Path) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_path_str = from_path.read_text(encoding="utf-8")
    template_path_str = template_path.read_text(encoding="utf-8")

    from_path_html = markdown_to_html_node(from_path_str).to_html()

    page_title = extract_title(from_path_str)

    template_path_str = template_path_str.replace("{{ Title }}", page_title)
    template_path_str = template_path_str.replace("{{ Content }}", from_path_html)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(template_path_str, encoding="utf-8")
