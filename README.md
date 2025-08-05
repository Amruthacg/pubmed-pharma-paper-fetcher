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

🚀 Usage

poetry run get-papers-list --query "cancer immunotherapy" --file results.csv

CLI Options

--query: PubMed search query

--file: (optional) CSV output filename

--debug: Print debug logs

--help: Show help

📦 Project Structure

🤖 Tools Used

Poetry
Typer
PubMed API
BeautifulSoup