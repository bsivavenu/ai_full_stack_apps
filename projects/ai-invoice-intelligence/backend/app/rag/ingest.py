import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("invoices")

def add_invoice(text, invoice_id):
    collection.add(
        documents=[text],
        ids=[str(invoice_id)]
    )
