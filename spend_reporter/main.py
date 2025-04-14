from pathlib import Path
import fitz

RESOURCES = Path("spend_reporter/resources/")
CATEGORIES = {
    "Market": ["PINGO DOCE", "CONTINENTE", "EL CORTE", "MINIPREÇO", "LIDL", "ALDI", "INTERMARCHÉ", "AUCHAN", "MERCADONA"],
    "CTW": ["CRITICAL"],
    "Clothes": ["ZARA", "LEFTIES", "PRIMARK", "BERSHKA", "PULL&BEAR", "STRADIVARIUS", "TIFFOSI", "SPORT ZONE", "DECATHLON", "SEASIDE"],
    "Transport": ["BOLT", "UBER"]
}

# Scrap PDF to make list of lines
def extract_lines_from_pdf(pdf):
    lines = []
    with fitz.open(pdf) as doc:
        for page in doc:
            text = page.get_text()
            lines.extend(text.split('\n'))
    return lines

# Filter the list from the PDF, grouping it by description and grouping the values
def group_lines(lines):
    grouped_lines = {}
    for i, line in enumerate(lines):
        if line.startswith("COMPRA") and i + 1 < len(lines):
            if line not in grouped_lines:
                grouped_lines[line] = []
            grouped_lines[line].append(lines[i + 1].replace(" ", ""))
    return grouped_lines

# Sum the grouped values in each grouped line
def sum_values(grouped_lines):
    for key, values in grouped_lines.items():
        total = sum(float(value) for value in values)
        grouped_lines[key] = total

# Categorize the lines based on keywords
def categorize_lines(grouped_lines):
    category_totals = {}
    uncategorized_lines = []

    for description, value in grouped_lines.items():
        matched = False
        
        for category, keywords in CATEGORIES.items():
            if any(keyword.upper() in description.upper() for keyword in keywords):
                if category not in category_totals:
                    category_totals[category] = 0
                category_totals[category] += value
                matched = True
                break
        
        if not matched:
            uncategorized_lines.append((description, value))

    return dict(category_totals), dict(uncategorized_lines)

# Present the data
def present_data(category_totals, uncategorized_lines):
    print("\nCategory Totals:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")

    print("\nUncategorized Lines:")
    for description, value in uncategorized_lines.items():
        print(f"{description}: {value:.2f}")

# Group, sum and categorize the lines from the PDF
def process_pdf(pdf_file):
    print(f"\nProcessing: {pdf_file.name}\n")

    all_lines = extract_lines_from_pdf(pdf_file)
    grouped_lines = group_lines(all_lines)
    sum_values(grouped_lines)
    category_totals, uncategorized_lines = categorize_lines(grouped_lines)

    present_data(category_totals, uncategorized_lines)


# Process all PDF files in the resources directory
# for pdf_file in RESOURCES.glob("*.pdf"):
#     process_pdf(pdf_file)

process_pdf(RESOURCES / "2025-03_Card.pdf")

# TODO: Create a chart with the data
