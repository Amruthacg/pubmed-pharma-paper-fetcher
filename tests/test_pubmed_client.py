from pubmed_fetcher.core.pubmed_client import search_pubmed

def test_pubmed_search():
    pmids = search_pubmed("diabetes")
    assert isinstance(pmids, list)
    assert len(pmids) > 0
