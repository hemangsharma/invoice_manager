import tkinter as tk
from tkinter import ttk, messagebox
from db.database import Database
from utils.excel_tools import export_invoices_to_excel
from utils.pdf_tools import export_invoice_to_pdf

class InvoiceManagerApp:
    def __init__(self, master):
        self.db = Database()
        self.master = master
        master.title("Invoice Manager")
        master.geometry("900x600")

        # Upper button panel
        btn_panel = tk.Frame(master)
        btn_panel.pack(fill=tk.X, pady=10)

        tk.Button(btn_panel, text="New Invoice", command=self.new_invoice).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_panel, text="Edit Invoice", command=self.edit_invoice).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_panel, text="Delete Invoice", command=self.delete_invoice).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_panel, text="Export to Excel", command=self.export_excel).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_panel, text="Export to PDF", command=self.export_pdf).pack(side=tk.LEFT, padx=6)

        # Invoice Table
        self.tree = ttk.Treeview(master,
                                 columns=("Invoice ID", "Client", "Date", "Total", "Status"),
                                 show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_invoices()

    def load_invoices(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for invoice in self.db.fetch_invoices():
            self.tree.insert("", tk.END, values=invoice)

    def new_invoice(self):
        # Implement Add Invoice dialog and logic
        messagebox.showinfo("Info", "Add invoice functionality not yet implemented.")

    def edit_invoice(self):
        # Implement Edit Invoice logic
        messagebox.showinfo("Info", "Edit invoice functionality not yet implemented.")

    def delete_invoice(self):
        # Implement Delete logic
        messagebox.showinfo("Info", "Delete invoice functionality not yet implemented.")

    def export_excel(self):
        export_invoices_to_excel(self.db.fetch_invoices(), "invoices.xlsx")
        messagebox.showinfo("Export", "Invoices exported to invoices.xlsx.")

    def export_pdf(self):
        # Implement selection and PDF export
        messagebox.showinfo("Export", "PDF export not yet implemented.")
