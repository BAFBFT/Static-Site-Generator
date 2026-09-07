# Static Site Generator

A static site generator in Python with no third-party dependencies. It converts a
tree of Markdown files into HTML pages using a single template, copies static
assets alongside them, and writes the result to `docs/` for GitHub Pages.

Built as a solution to the Boot.dev "Build a Static Site Generator" course.

## Usage

Build and serve locally:

```sh
./main.sh
```

Build for deployment under a subpath (e.g. GitHub Pages project site):

```sh
./build.sh
```

`build.sh` passes a base path that is prefixed to every root-relative `href` and
`src` in the output.

Run the tests:

```sh
./test.sh
```

## Layout

```
content/       Markdown source, mirrored into the output tree
static/        CSS and images, copied verbatim into the output
template.html  Page shell with {{ Title }} and {{ Content }} placeholders
docs/          Generated site (wiped and rebuilt on each run)
src/           Generator modules and unit tests
main.py        Entry point
```

Each `content/**/*.md` file becomes the matching `docs/**/*.html` file. The page
title is taken from the first `# ` heading in the Markdown; a file without one
raises an error.

## Supported Markdown

Block level: headings (`#` through `######`), fenced code blocks, blockquotes,
unordered lists (`- `), ordered lists (numbered from 1 with no gaps), and
paragraphs.

Inline: `**bold**`, `_italic_`, `` `code` ``, `[links](url)`, and
`![images](url)`.

## How it works

1. `static/` is copied into `docs/`, which is emptied first.
2. Each Markdown file is split into blocks, and each block is classified by type.
3. Blocks become `HTMLNode` trees; inline text is tokenized into `TextNode`s
   (delimiters first, then images, then links) and converted to leaf nodes.
4. The tree is rendered to a string and injected into `template.html`.
