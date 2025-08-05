# import typer
# app = typer.Typer()

# @app.command()
# def main():
#     typer.echo("🎉 CLI works!")

import typer
from pubmed_fetcher.core.pubmed_client import search_pubmed, fetch_details
from pubmed_fetcher.core.affiliation_filter import extract_company_affiliations
from pubmed_fetcher.core.utils import export_to_csv

app = typer.Typer()

@app.command()
def main(
    query: str,
    file: str = typer.Option(None, "--file", "-f", help="Filename to export CSV."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output.")
):
    typer.echo(f"🔍 Searching PubMed for: {query}")
    pmids = search_pubmed(query)
    if debug:
        typer.echo(f"🧠 Found {len(pmids)} papers")

    data = fetch_details(pmids)
    final_data = []

    for paper in data:
        non_acad_authors, company_affils = extract_company_affiliations(
            paper.get("Affiliations", []),
            paper.get("Authors", [])
        )
        final_data.append({
            "PubmedID": paper.get("PubmedID"),
            "Title": paper.get("Title"),
            "Publication Date": paper.get("Publication Date"),
            "Non-academic Author(s)": ", ".join(non_acad_authors),
            "Company Affiliation(s)": ", ".join(company_affils),
            "Corresponding Author Email": "N/A"  # You can extract email if needed
        })

    if file:
        export_to_csv(final_data, file)
    else:
        for paper in final_data:
            typer.echo(paper)
