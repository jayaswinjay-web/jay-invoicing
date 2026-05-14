# -*- coding: utf-8 -*-
"""
Product Form
"""

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit,
                           QComboBox, QPushButton, QDoubleSpinBox, QMessageBox)
from PyQt6.QtCore import Qt


class ProductEditor(QDialog):
    def __init__(self, company_id, product_id=None, parent=None):
        super().__init__(parent)
        self.company_id = company_id
        self.product_id = product_id
        
        if product_id:
            self.setWindowTitle("Edit Product")
        else:
            self.setWindowTitle("Add Product")
        
        self.setMinimumSize(500, 500)
        self.init_ui()
        
    def init_ui(self):
        """Init UI"""
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        grid = QGridLayout()
        layout.addLayout(grid)
        
        row = 0
        
        grid.addWidget(QLabel("Product Name:"), row, 0)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter product name")
        grid.addWidget(self.name, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Code:"), row, 0)
        self.code = QLineEdit()
        self.code.setPlaceholderText("Product code/SKU")
        grid.addWidget(self.code, row, 1)
        
        row += 1
        grid.addWidget(QLabel("HSN Code:"), row, 0)
        self.hsn = QLineEdit()
        self.hsn.setPlaceholderText("HSN/SAC code")
        grid.addWidget(self.hsn, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Category:"), row, 0)
        self.category = QComboBox()
        self.category.addItems(["General", "Electronics", "Clothing", "Food", "Other"])
        grid.addWidget(self.category, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Unit:"), row, 0)
        self.unit = QComboBox()
        self.unit.addItems(["PCS", "KG", "LTR", "MTR", "BOX", "SET"])
        grid.addWidget(self.unit, row, 1)
        
        row += 1
        grid.addWidget(QLabel("GST Rate (%):"), row, 0)
        self.gst_rate = QComboBox()
        self.gst_rate.addItems(["0", "5", "12", "18", "28"])
        self.gst_rate.setCurrentText("18")
        grid.addWidget(self.gst_rate, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Sale Rate:"), row, 0)
        self.sale_rate = QDoubleSpinBox()
        self.sale_rate.setRange(0, 9999999)
        self.sale_rate.setDecimals(2)
        grid.addWidget(self.sale_rate, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Purchase Rate:"), row, 0)
        self.purchase_rate = QDoubleSpinBox()
        self.purchase_rate.setRange(0, 9999999)
        self.purchase_rate.setDecimals(2)
        grid.addWidget(self.purchase_rate, row, 1)
        
        row += 1
        grid.addWidget(QLabel("MRP:"), row, 0)
        self.mrp = QDoubleSpinBox()
        self.mrp.setRange(0, 9999999)
        self.mrp.setDecimals(2)
        grid.addWidget(self.mrp, row, 1)
        
        row += 1
        grid.addWidget(QLabel("Min Stock:"), row, 0)
        self.min_stock = QDoubleSpinBox()
        self.min_stock.setRange(0, 999999)
        self.min_stock.setDecimals(0)
        grid.addWidget(self.min_stock, row, 1)
        
        # Buttons
        btns = QPushButton("Save Product")
        btns.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 4px;
                font-weight: 600;
            }
        """)
        btns.clicked.connect(self.save)
        
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
        
        btn_layout = QVBoxLayout()
        btn_layout.addWidget(btns)
        btn_layout.addWidget(cancel)
        
        layout.addLayout(btn_layout)
        
    def save(self):
        """Save product"""
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "Please enter product name")
            return
            
        from models.db import execute
        
        try:
            execute("""
                INSERT INTO products (company_id, name, code, hsn_code, unit, gst_rate, sale_rate, purchase_rate, mrp, min_stock)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.company_id,
                self.name.text(),
                self.code.text(),
                self.hsn.text(),
                self.unit.currentText(),
                float(self.gst_rate.currentText()),
                self.sale_rate.value(),
                self.purchase_rate.value(),
                self.mrp.value(),
                self.min_stock.value()
            ))
            
            QMessageBox.information(self, "Success", "Product saved")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))