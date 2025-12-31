Product Analysis Automation Demo

Make.com + Python + JSON/YAML

Overview

This repository demonstrates a simple but complete automation workflow that integrates an external API, applies business logic, and produces structured output. The same logic is implemented using Make.com (low-code automation) and Python (code-based automation) to show flexibility across platforms.

The project is intentionally small and focused, suitable for rapid evaluation during technical screening.

What This Demo Does
Fetches product data from a public API (DummyJSON)
Extracts relevant fields (price, rating, stock, category)
Applies business rules:
High value → price > 50
Popular → rating ≥ 4.0

Produces:
Human-readable formatted output
Machine-friendly JSON
Configuration-style YAML

Make.com Workflow
The Make.com scenario includes:
HTTP module – Fetch product data from API
Set variable – Compute boolean flags (is_high_value, is_popular)
Text Aggregator – Format the output
Set variable (final) – Store execution result

The final output is visible in the execution history of the scenario.
This demonstrates:

API integration
Data mapping
Conditional logic
Proper scenario termination
Python Implementation

The Python script mirrors the Make.com logic exactly.

File
product_analysis.py
Key Features
Uses requests to call the API
Separates concerns (fetching, analysis, formatting)
Returns boolean flags for business rules
Produces readable output suitable for logs or APIs

To run:
python product_analysis.py

Sample JSON Output
{
  "product": "Essence Mascara Lash Princess",
  "category": "beauty",
  "price": 9.99,
  "rating": 2.56,
  "stock": 99,
  "is_high_value": false,
  "is_popular": false
}

Sample YAML Output
product: Essence Mascara Lash Princess
category: beauty
price: 9.99
rating: 2.56
stock: 99
flags:
  high_value: false
  popular: false

Use Cases
Low-code / no-code automation (Make.com, n8n)
API data validation
E-commerce product analysis
Business rule prototyping
Workflow demonstrations for clients

Why This Approach
Shows the same logic across automation tools and code
Easy to extend (multiple products, alerts, storage, webhooks)
Clear separation of data, logic, and output
Suitable for real-world production workflows

Author
Padmanabh Narayan Gautam
Software Consultant – Automation, APIs, Python, Make.com, n8n