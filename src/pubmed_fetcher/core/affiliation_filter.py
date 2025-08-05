from typing import List, Tuple
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_company_affiliations(affiliations: List[str], authors: List[str]) -> Tuple[List[str], List[str]]:
    non_acad_authors = []
    companies = set()
    for aff, author in zip(affiliations, authors):
        if is_non_academic(aff):
            non_acad_authors.append(author)
            companies.add(aff)
    return non_acad_authors, list(companies)
