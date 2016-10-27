# markdown-toc

Script to generate a simple markdown TOC list.

- Lists all folder names as `# Headline` and all files as Markdown links in a bullet-list.
- Traverses all subfolders.
- skips `.idea`, `.git` and `.` folder as headline
- skips `.idea`, `.git` contents



## Usage


1. Copy `toc.py` to the root folder of your markdown notes
2. `chmod +x toc.py`
3. `./toc.py`


To persist the output simple pipe the output to a file.

```
./toc.py > README.md

```

Helpful if you have a markdown note structure and want to host them as some kind of wiki
in gitlab or github.
