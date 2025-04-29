"""
Requirements: pip install weasyprint jinja2
"""

from jinja2 import Template

from weasyprint import HTML


def get_pdf(data, fields, html_template_path):
    # Load HTML template as string
    with open(html_template_path) as f:
        html_template = f.read()

    # Render using Jinja2
    template = Template(html_template)
    context = {"data": data, "fields": fields}
    html_rendered = template.render(context)
    # Generate PDF
    HTML(string=html_rendered).write_pdf("pdf_generator/invoice.pdf")
    print("PDF generated successfully")

data = [
    {
        "customer_name": "Mossaddak",
        "invoice_number": "INV-001",
        "total": 200.00,
    },
    {
        "customer_name": "Friha",
        "invoice_number": "INV-002",
        "total": 300.00,
    },
]
fields = ["Invoice Id", "Customer Name", "Total"]
get_pdf(data, fields, "pdf_generator/invoice.html")
