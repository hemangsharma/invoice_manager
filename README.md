# Invoice Manager

A Python desktop app for managing invoices, clients, and reports, featuring:
- Add/edit/delete/search invoices and clients
- Export to PDF and Excel
- Send invoices via email
- Modern Tkinter interface

## Project Structure

invoice_manager/
├── LICENSE
├── README.md
├── main.py
├── db/
│   └── database.py
├── ui/
│   └── main_window.py
├── utils/
│   ├── excel_tools.py
│   ├── pdf_tools.py
│   └── email_tools.py
├── requirements.txt

## Features

- CRUD for invoices and clients
- Advanced search (date, status, totals)
- PDF invoice export (with fpdf2)
- Excel report export (openpyxl/pandas)
- Email invoices to clients

## Setup
```bash
pip install -r requirements.txt
```