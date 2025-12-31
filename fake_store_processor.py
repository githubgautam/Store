import json

def process_product(product):
    """
    Validates and transforms product data from Fake Store API
    """

    required_fields = ["id", "title", "price", "category", "rating"]

    for field in required_fields:
        if field not in product:
            raise ValueError(f"Missing required field: {field}")

    rating = product.get("rating", {})
    rate = rating.get("rate", 0)
    count = rating.get("count", 0)

    processed = {
        "product_id": product["id"],
        "title": product["title"].strip(),
        "category": product["category"],
        "price_usd": round(float(product["price"]), 2),
        "rating_score": rate,
        "rating_count": count,
        "is_high_value": product["price"] > 100,
        "is_popular": count > 200
    }

    return processed


if __name__ == "__main__":
    # Example usage for local testing
    with open("sample_product.json") as f:
        product_data = json.load(f)

    result = process_product(product_data)
    print(json.dumps(result, indent=2))
