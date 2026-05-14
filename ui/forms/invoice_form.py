# -*- coding: utf-8 -*-
"""
Invoice Form - Create/Edit Invoices
"""

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel,
                           QLineEdit, QComboBox, QPushButton, QTableWidget,
                           QTableWidgetItem, QDateEdit, QTextEdit, QGroupBox,
                           QDoubleSpinBox, QMessageBox, QHeaderView, Qt)
from PyQt6.QtCore import Qt, QDate
from datetime import datetime


class InvoiceEditor(QDialog):
    def __init__(self, company_id, invoice_id=None, parent=None):
        super().__init__(parent)
        self.company_id = company_id
        self.invoice_id = invoice_id
        self.items = []
        
        if invoice_id:
            self.setWindowTitle("Edit Invoice")
        else:
            self.setWindowTitle("New Invoice")
        
        self.setMinimumSize(1000, 700)
        self.init_ui()
        
        if not invoice_id:
            self.set_defaults()
            
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout()
        layout.setSpacing(15)
        self.setLayout(layout)
        
        # Header
        header = QGridLayout()
        
        # Invoice type
        header.addWidget(QLabel("Invoice Type:"), 0, 0)
        self.inv_type = QComboBox()
        self.inv_type.addItems(["Sales Invoice", "Purchase Invoice", "Proforma", "Quotation", 
                           "Credit Note", "Debit Note", "Delivery Challan"])
        header.addWidget(self.inv_type, 0, 1)
        
        # Invoice number
        header.addWidget(QLabel("Invoice No:"), 0, 2)
        self.inv_no = QLineEdit()
        self.inv_no.setText("INV-0001")
        header.addWidget(self.inv_no, 0, 3)
        
        # Date
        header.addWidget(QLabel("Date:"), 0, 4)
        self.inv_date = QDateEdit()
        self.inv_date.setDate(QDate.currentDate())
        header.addWidget(self.inv_date, 0, 5)
        
        # Customer
        header.addWidget(QLabel("Customer:"), 1, 0)
        self.customer = QComboBox()
        self.customer.setEditable(True)
        self.customer.setPlaceholderText("Select or type customer name")
        header.addWidget(self.customer, 1, 1, 1, 2)
        
        # GSTIN
        header.addWidget(QLabel("GSTIN:"), 1, 3)
        self.gstin = QLineEdit()
        self.gstin.setPlaceholderText("15-digit GSTIN")
        header.addWidget(self.gstin, 1, 4, 1, 2)
        
        layout.addLayout(header)
        
        # Items table
        self.items_table = self.create_items_table()
        layout.addWidget(self.items_table, 1)
        
        # Summary
        summary = self.create_summary()
        layout.addWidget(summary)
        
        # Buttons
        buttons = QHBoxLayout()
        
        save = QPushButton("Save Invoice")
        save.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 24px;
                border-radius: 4px;
                font-weight: 600;
            }
        """)
        save.clicked.connect(self.save)
        
        print_btn = QPushButton("Print")
        print_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E7DD1;
                color: white;
                border: none;
                padding: 10px 24px;
                border-radius: 4px;
            }
        """)
        
        cancel = QPushButton("Cancel")
        cancel.setStyleSheet("""
            QPushButton {
                background-color: #F5F5F5;
                color: #212121;
                border: 1px solid #BDBDBD;
                padding: 10px 24px;
                border-radius: 4px;
            }
        """)
        cancel.clicked.connect(self.reject)
        
        buttons.addStretch()
        buttons.addWidget(save)
        buttons.addWidget(print_btn)
        buttons.addWidget(cancel)
        
        layout.addLayout(buttons)
        
    def create_items_table(self):
        """Create items table"""
        table = QTableWidget()
        table.setColumnCount(12)
        table.setHorizontalHeaderLabels([
            "Product", "HSN", "Unit", "Qty", "Rate", 
            "Disc %", "Disc Amt", "Taxable", "GST%", "GST Amt", "Total", ""
        ])
        
        # Add button column header
        table.horizontalHeader().setStretchLastSection(False)
        table.setColumnWidth(11, 50)
        
        table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #E0E0E0;
                border-radius: 4px;
                gridline-color: #EEEEEE;
            }
            QTableWidget::item {
                padding: 6px;
            }
            QHeaderView::section {
                background-color: #F5F5F5;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #2E7DD1;
                font-weight: 600;
                color: #212121;
            }
        """)
        
        # Add first row
        table.insertRow(0)
        
        return table
        
    def create_summary(self):
        """Create summary section"""
        group = QGroupBox("Summary")
        layout = QGridLayout()
        group.setLayout(layout)
        
        layout.addWidget(QLabel("Subtotal:"), 0, 0)
        self.subtotal = QLineEdit("0.00")
        self.subtotal.setReadOnly(True)
        self.subtotal.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.subtotal.setStyleSheet("background-color: #F5F5F5;")
        layout.addWidget(self.subtotal, 0, 1)
        
        layout.addWidget(QLabel("Discount:"), 0, 2)
        self.discount = QDoubleSpinBox()
        self.discount.setRange(0, 100)
        self.discount.setValue(0)
        self.discount.valueChanged.connect(self.calculate_totals)
        layout.addWidget(self.discount, 0, 3)
        
        layout.addWidget(QLabel("CGST:"), 1, 0)
        self.cgst = QLineEdit("0.00")
        self.cgst.setReadOnly(True)
        self.cgst.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.cgst.setStyleSheet("background-color: #F5F5F5;")
        layout.addWidget(self.cgst, 1, 1)
        
        layout.addWidget(QLabel("SGST:"), 1, 2)
        self.sgst = QLineEdit("0.00")
        self.sgst.setReadOnly(True)
        self.sgst.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sgst.setStyleSheet("background-color: #F5F5F5;")
        layout.addWidget(self.sgst, 1, 3)
        
        layout.addWidget(QLabel("IGST:"), 1, 4)
        self.igst = QLineEdit("0.00")
        self.igst.setReadOnly(True)
        self.igst.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.igst.setStyleSheet("background-color: #F5F5F5;")
        layout.addWidget(self.igst, 1, 5)
        
        layout.addWidget(QLabel("Grand Total:"), 2, 0)
        self.total = QLineEdit("0.00")
        self.total.setReadOnly(True)
        self.total.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.total.setStyleSheet("""
            background-color: #E3F2FD;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(self.total, 2, 1)
        
        layout.addWidget(QLabel("Terms:"), 3, 0)
        self.terms = QLineEdit("Payment due within 30 days")
        layout.addWidget(self.terms, 3, 1, 1, 5)
        
        return group
        
    def set_defaults(self):
        """Set default values"""
        # Load customers
        from models.db import fetch_all
        
        parties = fetch_all("""
            SELECT name, gstin FROM parties 
            WHERE company_id = ? AND party_type = 'customer' AND is_active = 1
            ORDER BY name
        """, (self.company_id,))
        
        self.customer.addItem("")
        for p in parties:
            self.customer.addItem(p['name'], p['gstin'])
            
    def calculate_totals(self):
        """Calculate totals"""
        subtotal = 0
        cgst_amt = 0
        sgst_amt = 0
        igst_amt = 0
        
        disc_pct = self.discount.value()
        
        for row in range(self.items_table.rowCount()):
            # Calculate row totals
            qty = 1
            rate = 0
            
            subtotal += qty * rate
        
        # Apply discount
        disc_amt = subtotal * (disc_pct / 100)
        subtotal -= disc_amt
        
        # Grand total
        grand = subtotal + cgst_amt + sgst_amt + igst_amt
        grand = round(grand)
        
        self.subtotal.setText(f"{subtotal:.2f}")
        self.cgst.setText(f"{cgst_amt:.2f}")
        self.sgst.setText(f"{sgst_amt:.2f}")
        self.igst.setText(f"{igst_amt:.2f}")
        self.total.setText(f"{grand:.2f}")
        
    def save(self):
        """Save invoice"""
        from models.db import execute
        
        customer_name = self.customer.currentText().strip()
        if not customer_name:
            QMessageBox.warning(self, "Error", "Please select a customer")
            return
            
        if not self.inv_no.text().strip():
            QMessageBox.warning(self, "Error", "Please enter invoice number")
            return
            
        inv_date = self.inv_date.date().toString("yyyy-MM-dd")
        
        try:
            execute("""
                INSERT INTO invoices (company_id, invoice_no, invoice_date, party_name, party_gstin, grand_total, narration)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                self.company_id,
                self.inv_no.text(),
                inv_date,
                customer_name,
                self.gstin.text(),
                float(self.total.text() or 0),
                self.terms.text()
            ))
            
            QMessageBox.information(self, "Success", "Invoice saved successfully")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))