from typing import List, Dict
import requests
import xml.etree.ElementTree as ET
import time

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, retmax: int = 100) -> List[str]:
    """Search PubMed and return list of PMIDs."""
    response = requests.get(BASE_URL + "esearch.fcgi", params={
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    })
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_details(pmid_list: List[str]) -> List[Dict]:
    """Fetch paper metadata from PubMed using PMIDs."""
    results = []
    for pmid in pmid_list:
        response = requests.get(BASE_URL + "efetch.fcgi", params={
            "db": "pubmed",
            "id": pmid,
            "retmode": "xml"
        })
        response.raise_for_status()
        root = ET.fromstring(response.text)
        paper = {"PubmedID": pmid}

        try:
            article = root.find(".//ArticleTitle")
            paper["Title"] = article.text if article is not None else "N/A"

            pub_date = root.find(".//PubDate/Year")
            paper["Publication Date"] = pub_date.text if pub_date is not None else "N/A"

            authors = []
            affiliations = []
            for author in root.findall(".//Author"):
                name = author.find("LastName")
                affiliation_info = author.find("AffiliationInfo/Affiliation")
                if name is not None and affiliation_info is not None:
                    authors.append(name.text)
                    affiliations.append(affiliation_info.text)

            paper["Authors"] = authors
            paper["Affiliations"] = affiliations
        except Exception as e:
            paper["Title"] = "Parse Error"
            paper["Authors"] = []
            paper["Affiliations"] = []
        results.append(paper)
        time.sleep(0.34)  # prevent overloading NCBI
    return results
