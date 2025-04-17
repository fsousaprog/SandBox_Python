from pathlib import Path
import fitz

RESOURCES = Path("spend_reporter/resources/")
UNCATEGORIZED = "Uncategorized"
TOTAL = "Total"
CATEGORIES = {
    "Market": ["PINGO DOCE", "CONTINENTE", "EL CORTE", "NORMALAS", "MINIPREÇO", "LIDL", "ALDI", "INTERMARCHÉ", "AUCHAN", "MERCADONA", "MARKET", "SUPERMERCADO", "SUPERMARKET", "CARREFOUR", "HYPERMERCADO", "HYPERMARKET"],
    "CTW": ["CRITICAL", "CRISTAL"],
    "Clothes": ["ZARA", "LEFTIES", "PRIMARK", "BERSHKA", "PULL&BEAR", "STRADIVARIUS", "TIFFOSI", "SPORT ZONE", "DECATHLON", "SEASIDE", "SKETCHERS", "VANS", "NIKE", "ADIDAS"],
    "Transport": ["TALLINN", "OLAIAS LISBOA", "TRANSPORT"],
    "Food": ["TGTG", "UBER EATS", "GLOVO", "VIIMSI", "MCDONALDS", "BK", "H3", "PIZZA", "MONTADITOS", "KFC", "SUBWAY", "DOMINOS", "BURGER", "BURGUER", "PASTEL", "PASTEIS", "CAFE", "LINDT"],
    "Health": ["PHARMACY", "FARMACIA", "WELLS", "HOSPITAL", "CLINIC", "DENTIST"],
    "Sports": ["LEMON FIT", "GYM", "FITNESS"],
    "Online Shopping": ["AMAZON", "TEMU", "ALIBABA", "EBAY", "WISH", "ALIEXPRESS", "FNAC"],
    "Travel": ["FLIXBUS", "ALSA", "RENTAL", "CAR", "FLIGHT", "HOTEL", "HOSTEL", "AIRBNB", "BOOKING", "APARTMENT"]
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
        if (line.startswith("COMPRA") or line.startswith("MBW")) and i + 1 < len(lines):
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
    category_totals[TOTAL] = 0
    category_totals[UNCATEGORIZED] = 0
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
            category_totals[UNCATEGORIZED] += value
            uncategorized_lines.append((description, value))

        category_totals[TOTAL] += value

    return dict(category_totals), dict(uncategorized_lines)

# Present the data
def present_data(category_totals, uncategorized_lines):
    print("\nReport:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")

    print("\nUncategorized Lines: ")
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
for pdf_file in RESOURCES.glob("*.pdf"):
    process_pdf(pdf_file)

# process_pdf(RESOURCES / "2025-03_Card.pdf")

# TODO: Create a chart with the data
