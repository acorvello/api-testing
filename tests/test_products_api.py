import requests


def test_list_products_returns_items(base_url):
    response = requests.get(f"{base_url}/rest/products/search")

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert len(body["data"]) > 0


def test_search_products_by_term(base_url):
    response = requests.get(
        f"{base_url}/rest/products/search", params={"q": "apple"}
    )

    assert response.status_code == 200
    body = response.json()
    assert "data" in body


def test_get_single_product_by_id(base_url):
    search_response = requests.get(f"{base_url}/rest/products/search")
    first_product_id = search_response.json()["data"][0]["id"]

    product_response = requests.get(f"{base_url}/api/Products/{first_product_id}")

    assert product_response.status_code == 200
    assert product_response.json()["data"]["id"] == first_product_id


def test_get_product_with_invalid_id_returns_404(base_url):
    response = requests.get(f"{base_url}/api/Products/999999")

    assert response.status_code == 404
