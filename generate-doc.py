from docx import Document

def generate_invoice(template_path, output_path, data):
    """Replaces placeholders in a DOCX invoice template with actual values."""
    
   
    doc = Document(template_path)


    for para in doc.paragraphs:
        for key, value in data.items():
            if f"{{{{{key}}}}}" in para.text:
                para.text = para.text.replace(f"{{{{{key}}}}}", str(value))


    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for key, value in data.items():
                    if f"{{{{{key}}}}}" in cell.text:
                        cell.text = cell.text.replace(f"{{{{{key}}}}}", str(value))


    doc.save(output_path)
    print(f"Invoice saved as {output_path}")


invoice_data = {
    "invoice_date": "21 March 2025",
    "invoice_number": "INV-20250321",
    "client_name": "Jio BP",
    "client_company": "Reliance Jio",
    "client_address": "Mumbai, India",
    "item_1": "Software Subscription",
    "qty_1": "1",
    "price_1": "₹5,000",
    "total_1": "₹5,000",
    "item_2": "Cloud Storage",
    "qty_2": "2",
    "price_2": "₹2,500",
    "total_2": "₹5,000",
    "item_3": "Support Services",
    "qty_3": "1",
    "price_3": "₹3,000",
    "total_3": "₹3,000",
    "subtotal": "₹13,000",
    "tax_rate": "18",
    "tax_amount": "₹2,340",
    "grand_total": "₹15,340"
}

generate_invoice("invoice-template.docx", "invoice_filled.docx", invoice_data)
