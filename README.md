# PubMed Pharma Paper Fetcher

A command-line tool to fetch and filter PubMed research papers with at least one non-academic (pharmaceutical or biotech) author. Built with Python and Poetry.

## 🔧 Features

- Search PubMed using any query
- Fetch title, publication date, authors, affiliations, and contact email
- Filters authors affiliated with pharmaceutical/biotech companies
- Outputs results to a CSV or prints to console
- CLI powered by Typer

## 🛠️ Installation

```bash
git clone https://github.com/your-username/pubmed-pharma-paper-fetcher.git
cd pubmed-pharma-paper-fetcher
poetry install
```

## 🚀 Usage

```bash
poetry run get-papers-list --query "cancer immunotherapy" --file results.csv
```

### CLI Options

- `--query`: PubMed search query
- `--file`: (optional) CSV output filename
- `--debug`: Print debug logs
- `--help`: Show help

## 📦 Project Structure

```
📁 pubmed-pharma-paper-fetcher/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .pytest_cache/
├── src/
│   └── pubmed_fetcher/
│       ├── __pycache__/
│       ├── cli/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── main.py
│       ├── core/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── affiliation_filter.py
│       │   ├── pubmed_client.py
│       │   └── utils.py
│       └── pubmed_fetcher_init.py
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   └── test_pubmed_client.py
├── .gitignore
├── LICENSE
├── poetry.lock
├── pyproject.toml
└── README.md

```


🔍 Example Output

| PubMed ID | Title         | Publication Date | Non-Academic Authors | Company Affiliations | Corresponding Author Email                        |
| --------- | ------------- | ---------------- | -------------------- | -------------------- | ------------------------------------------------- |
| 12345678  | Example Title | 2023-05-14       | John Doe             | Pfizer Inc.          | [john.doe@pfizer.com](mailto:john.doe@pfizer.com) |


## 🤖 Tools Used

- [Poetry](https://python-poetry.org/)
- [Typer](https://typer.tiangolo.com/)
- [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## 🧪 Tests

```bash
poetry run pytest
```

## 📜 License

MIT License
