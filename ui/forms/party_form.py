# -*- coding: utf-8 -*-
"""
Party Form - Customer/Vendor
"""

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit,
                           QComboBox, QPushButton, QDoubleSpinBox, QMessageBox)
from PyQt6.QtCore import Qt


class PartyEditor(QDialog):
    def __init__(self, company_id, party_id=None, parent=None):
        super().__init__(parent)
        self.company_id = company_id
        self.party_id = party_id
        
        if party_id:
            self.setWindowTitle("Edit Party")
        else:
            self.setWindowTitle("Add Party")
        
        self.setMinimumSize(550, 550)
        self.init_ui()
        
    def init_ui(self):
        """Init UI"""
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        grid = QGridLayout()
        layout.addLayout(grid)
        
        row = 0
        
        grid.addWidget(QLabel("Party Type:"), row, 0)
        self.party_type = QComboBox()
        self.party_type.addItems(["Customer", "Vendor"])
        grid.addWidget(self.party_type, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Name:"), row, 0)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Customer/Vendor name")
        grid.addWidget(self.name, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Code:"), row, 0)
        self.code = QLineEdit()
        self.code.setPlaceholderText("Party code")
        grid.addWidget(self.code, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Address:"), row, 0)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Full address")
        grid.addWidget(self.address, row, 1)
        
        row += 1
        grid.addWidget(QLabel("City:"), row, 0)
        self.city = QLineEdit()
        grid.addWidget(self.city, row, 1)
        
        row += 1
        grid.addWidget(QLabel("State:"), row, 0)
        self.state = QComboBox()
        self.state.addItems([
            "Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "Gujarat",
            "Uttar Pradesh", "West Bengal", "Rajasthan", "Madhya Pradesh",
            "Punjab", " Haryana", "Others"
        ])
        grid.addWidget(self.state, row, 1)
        
        row += 1
        grid.addWidget(QLabel("GSTIN:"), row, 0)
        self.gstin = QLineEdit()
        self.gstin.setPlaceholderText("15-digit GSTIN")
        grid.addWidget(self.gstin, row, 1)
        
        row += 1
        grid.addWidget(QLabel("PAN:"), row, 0)
        self.pan = QLineEdit()
        self.pan.setPlaceholderText("10-character PAN")
        grid.addWidget(self.pan, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Email:"), row, 0)
        self.email = QLineEdit()
        self.email.setPlaceholderText("email@example.com")
        grid.addWidget(self.email, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Phone:"), row, 0)
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone number")
        grid.addWidget(self.phone, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Contact Person:"), row, 0)
        self.contact = QLineEdit()
        grid.addWidget(self.contact, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Credit Limit:"), row, 0)
        self.credit_limit = QDoubleSpinBox()
        self.credit_limit.setRange(0, 99999999)
        self.credit_limit.setDecimals(2)
        grid.addWidget(self.credit_limit, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Payment Terms:"), row, 0)
        self.payment_terms = QComboBox()
        self.payment_terms.addItems(["Immediate", "7 Days", "15 Days", "30 Days", "45 Days", "60 Days"])
        self.payment_terms.setCurrentText("30 Days")
        grid.addWidget(self.payment_terms, row, 1)
        
        # Buttons
        btns = QVBoxLayout()
        
        save = QPushButton("Save Party")
        save.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 4px;
                font-weight: 600;
            }
        """)
        save.clicked.connect(self.save)
        
        cancel = QPushButton("Cancel")
        cancel.setStyleSheet("""
            QPushButton {
                background-color: #F5F5F5;
                color: #212121;
                border: 1px solid #BDBDBD;
                padding: 12px 24px;
                border-radius: 4px;
            }
        """)
        cancel.clicked.connect(self.reject)
        
        btns.addWidget(save)
        btns.addWidget(cancel)
        
        layout.addLayout(btns)
        
    def save(self):
        """Save party"""
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "Please enter party name")
            return
            
        from models.db import execute
        
        try:
            execute("""
                INSERT INTO parties (company_id, name, code, party_type, address, city, state, gstin, pan, email, phone, contact, credit_limit)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.company_id,
                self.name.text(),
                self.code.text(),
                self.party_type.currentText().lower(),
                self.address.text(),
                self.city.text(),
                self.state.currentText(),
                self.gstin.text(),
                self.pan.text(),
                self.email.text(),
                self.phone.text(),
                self.contact.text(),
                self.credit_limit.value()
            ))
            
            QMessageBox.information(self, "Success", "Party saved")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))