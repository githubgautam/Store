import requests
import json

URL = "https://dummyjson.com/products/1"

def get_product(product_id: int):
    response = requests.get(f"https://dummyjson.com/products/{product_id}")
    response.raise_for_status()
    return response.json()

def analyze_product(product: dict) -> dict:
    return {
        "product": product["title"],
        "category": product["category"],
        "price": product["price"],
        "rating": product["rating"],
        "stock": product["stock"],
        "is_high_value": product["price"] > 50,
        "is_popular": product["rating"] >= 4.0
    }

def format_output(data: dict) -> str:
    return (
        f"product: {data['product']}\n"
        f"category: {data['category']}\n"
        f"price: ${data['price']}\n"
        f"rating: {data['rating']}\n"
        f"stock: {data['stock']}\n"
        f"high_value: {data['is_high_value']}\n"
        f"popular: {data['is_popular']}"
    )

if __name__ == "__main__":
    product = get_product(1)
    analysis = analyze_product(product)
    
    # Write YAML format
    with open("sample_product.yaml", "w") as f:
        f.write(format_output(analysis))
    
    # Write JSON format
    with open("sample_product.json", "w") as f:
        json.dump(analysis, f, indent=2)
    
    print("Output written to sample_product.yaml and sample_product.json")
