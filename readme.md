# PDF Merge

A small Python script that combines multiple PDF files into one PDF.

## What It Does

The script reads every `.pdf` file from the `pdfs` folder, sorts the files by name, and merges them into a single output file named `combined.pdf`.

## Project Structure

```text
pdf merge/
├── main.py
├── readme.md
└── pdfs/
    ├── first.pdf
    ├── second.pdf
    └── ...
```

## Requirements

- Python 3
- PyPDF2

Install the dependency with:

```bash
pip install PyPDF2
```

## Usage

1. Create a folder named `pdfs` in the project directory if it does not already exist.
2. Place the PDF files you want to merge inside the `pdfs` folder.
3. Name the files in the order you want them merged, for example:

```text
01-cover.pdf
02-report.pdf
03-appendix.pdf
```

4. Run the script:

```bash
python main.py
```

5. The merged file will be created as:

```text
combined.pdf
```

## Notes

- Files are merged in alphabetical filename order.
- Only files ending in `.pdf` are included.
- The output file is written to the project directory.
