def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split('\n\n')
    final_blocks = []
    for block in blocks:
        if not block.strip():
            continue
        final_blocks.append(block.strip())
    return final_blocks
