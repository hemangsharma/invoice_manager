import pandas as pd

def export_invoices_to_excel(invoices, filename):
    df = pd.DataFrame(invoices, columns=["Invoice ID", "Client", "Date", "Total", "Status"])
    df.to_excel(filename, index=False)
