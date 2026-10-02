def test_list_products_returns_200_with_data(api_client):
    response = api_client.get("/rest/products")

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


def test_product_item_has_expected_fields(api_client):
    response = api_client.get("/rest/products")
    product = response.json()["data"][0]

    for field in ("id", "name", "price", "description"):
        assert field in product


def test_search_returns_matching_products(api_client):
    response = api_client.get("/rest/products/search", params={"q": "apple"})

    assert response.status_code == 200
    results = response.json()["data"]
    assert len(results) > 0
    assert any("apple" in item["name"].lower() for item in results)


def test_search_with_no_match_returns_empty_list(api_client):
    response = api_client.get(
        "/rest/products/search", params={"q": "termo-que-nao-deve-existir-xyz"}
    )

    assert response.status_code == 200
    assert response.json()["data"] == []
