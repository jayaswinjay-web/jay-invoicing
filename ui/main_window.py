# -*- coding: utf-8 -*-
"""
Main Window - Professional Design
"""

import sys
from datetime import datetime
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                           QPushButton, QFrame, QStackedWidget, QListWidget, 
                           QStatusBar, QMenuBar, QMenu, QMessageBox, QSplitter)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QFont, QIcon, QAction

# Import styles
from ui.style import AppColors, CSS, apply_button_style


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_company_id = 1
        self.init_ui()
        self.load_data()
        
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle("JAY INVOICE - Professional Invoicing")
        self.setMinimumSize(1280, 800)
        self.resize(1400, 900)
        
        # Central widget
        self.central = QWidget()
        self.setCentralWidget(self.central)
        
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.central.setLayout(main_layout)
        
        # Sidebar
        self.create_sidebar()
        main_layout.addWidget(self.sidebar, 0)
        
        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setStyleSheet("background-color: #E0E0E0; width: 1px;")
        main_layout.addWidget(divider, 0)
        
        # Content area
        self.create_content_area()
        main_layout.addWidget(self.content_area, 1)
        
        # Status bar
        self.create_status_bar()
        
        # Menu bar
        self.create_menu_bar()
        
    def create_sidebar(self):
        """Create professional sidebar"""
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(250)
        self.sidebar.setStyleSheet(f"""
            QFrame {{
                background-color: {AppColors.SIDEBAR_BG};
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.sidebar.setLayout(layout)
        
        # Logo area
        logo_frame = QFrame()
        logo_frame.setFixedHeight(100)
        logo_frame.setStyleSheet("background-color: #151E29;")
        logo_layout = QVBoxLayout()
        logo_frame.setLayout(logo_layout)
        
        logo = QLabel("JAY INVOICE")
        logo.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            padding-left: 20px;
        """)
        logo_layout.addWidget(logo)
        
        tagline = QLabel("Professional Billing Software")
        tagline.setStyleSheet("""
            font-size: 11px;
            color: #6B828E;
            padding-left: 20px;
        """)
        logo_layout.addWidget(tagline)
        
        layout.addWidget(logo_frame)
        
        # Company selector
        self.company_list = QListWidget()
        self.company_list.setFixedHeight(120)
        self.company_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                border: none;
                padding: 10px;
            }
            QListWidget::item {
                color: #AAB4BE;
                padding: 8px 12px;
                border-radius: 4px;
                margin: 2px 0;
            }
            QListWidget::item:selected {
                background-color: #2E7DD1;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #2A3A4A;
            }
        """)
        self.company_list.itemClicked.connect(self.on_company_changed)
        layout.addWidget(self.company_list)
        
        # Navigation
        nav_frame = QFrame()
        nav_layout = QVBoxLayout()
        nav_frame.setLayout(nav_layout)
        
        nav_items = [
            ("Dashboard", "dashboard"),
            ("Invoices", "invoices"),
            ("Sales", "sales"),
            ("Purchase", "purchase"),
            ("Parties", "parties"),
            ("Products", "products"),
            ("Accounts", "accounts"),
            ("GST", "gst"),
            ("Reports", "reports"),
            ("Settings", "settings"),
        ]
        
        self.nav_buttons = {}
        
        for name, code in nav_items:
            btn = QPushButton(name)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 0;
                    color: #AAB4BE;
                    font-size: 14px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: #2A3A4A;
                    color: white;
                }
                QPushButton:pressed, QPushButton[selected=true] {
                    background-color: #2E7DD1;
                    color: white;
                }
            """)
            btn.clicked.connect(lambda checked, c=code: self.navigate(c))
            self.nav_buttons[code] = btn
            nav_layout.addWidget(btn)
        
        layout.addWidget(nav_frame, 1)
        
        # Bottom actions
        bottom_frame = QFrame()
        bottom_frame.setFixedHeight(60)
        bottom_frame.setStyleSheet("background-color: #151E29;")
        bottom_layout = QHBoxLayout()
        bottom_frame.setLayout(bottom_layout)
        
        quick_add = QPushButton("+ New Invoice")
        quick_add.setStyleSheet("""
            QPushButton {
                background-color: #2E7DD1;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1A5CB0;
            }
        """)
        quick_add.clicked.connect(self.new_invoice)
        bottom_layout.addWidget(quick_add)
        
        layout.addWidget(bottom_frame)
        
    def create_content_area(self):
        """Create content area with pages"""
        self.content_area = QFrame()
        self.content_area.setStyleSheet(f"""
            background-color: {AppColors.BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        self.content_area.setLayout(layout)
        
        # Header
        header = QFrame()
        header.setFixedHeight(60)
        header_layout = QHBoxLayout()
        header.setLayout(header_layout)
        
        self.page_title = QLabel("Dashboard")
        self.page_title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #212121;
        """)
        header_layout.addWidget(self.page_title, 1)
        
        header_layout.addWidget(self.create_header_actions())
        
        layout.addWidget(header)
        
        # Pages stack
        self.pages = QStackedWidget()
        layout.addWidget(self.pages, 1)
        
        # Create pages
        self.create_dashboard_page()
        self.create_invoices_page()
        self.create_parties_page()
        self.create_products_page()
        self.create_settings_page()
        
    def create_header_actions(self):
        """Create header actions"""
        frame = QFrame()
        layout = QHBoxLayout()
        frame.setLayout(layout)
        layout.setSpacing(10)
        
        # Date range widgets placeholder
        today = QLabel(datetime.now().strftime("%d %B %Y"))
        today.setStyleSheet("color: #757575; padding: 8px;")
        layout.addWidget(today)
        
        refresh_btn = QPushButton("Refresh")
        apply_button_style(refresh_btn, "secondary")
        layout.addWidget(refresh_btn)
        
        return frame
        
    def create_dashboard_page(self):
        """Dashboard page"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # Stats cards
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(16)
        
        stats = [
            ("Today Sales", "₹0", "Sales today", AppColors.SUCCESS),
            ("Pending Receivables", "₹0", "Outstanding", AppColors.WARNING),
            ("Total Invoices", "0", "This month", AppColors.PRIMARY),
            ("Low Stock Items", "0", "Need attention", AppColors.DANGER),
        ]
        
        for title, value, subtitle, color in stats:
            card = self.create_stat_card(title, value, subtitle, color)
            stats_layout.addWidget(card, 1)
        
        layout.addLayout(stats_layout)
        
        # Recent transactions
        recent = QFrame()
        recent.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        recent_layout = QVBoxLayout()
        recent.setLayout(recent_layout)
        
        recent_title = QLabel("Recent Invoices")
        recent_title.setStyleSheet("font-size: 16px; font-weight: 600; padding: 16px;")
        recent_layout.addWidget(recent_title)
        
        # Table placeholder
        table = QFrame()
        table.setStyleSheet("border: none;")
        table_layout = QVBoxLayout()
        table.setLayout(table_layout)
        
        empty = QLabel("No recent invoices")
        empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet("color: #9E9E9E; padding: 40px;")
        table_layout.addWidget(empty)
        
        recent_layout.addWidget(table, 1)
        
        layout.addWidget(recent, 1)
        
        self.pages.addWidget(page)
        
    def create_stat_card(self, title, value, subtitle, color):
        """Create stat card"""
        card = QFrame()
        card.setStyleSheet(f"""
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            border-left: 4px solid {color};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)
        card.setLayout(layout)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 12px; color: #757575;")
        layout.addWidget(title_label)
        
        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {color};")
        layout.addWidget(value_label)
        
        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet("font-size: 11px; color: #9E9E9E;")
        layout.addWidget(sub_label)
        
        return card
        
    def create_invoices_page(self):
        """Invoices list page"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(16)
        page.setLayout(layout)
        
        # Toolbar
        toolbar = QHBoxLayout()
        
        new_btn = QPushButton("+ New Invoice")
        apply_button_style(new_btn, "primary")
        new_btn.clicked.connect(self.new_invoice)
        toolbar.addWidget(new_btn)
        
        # Invoice type buttons
        for inv_type in ["Sales", "Purchase", "Credit Note", "Debit Note"]:
            btn = QPushButton(inv_type)
            apply_button_style(btn, "secondary")
            toolbar.addWidget(btn)
        
        toolbar.addStretch()
        
        # Search
        search = QLabel("Search...")
        search.setStyleSheet("color: #9E9E9E; padding: 8px 12px;")
        toolbar.addWidget(search)
        
        layout.addLayout(toolbar)
        
        # Table
        table = QFrame()
        table.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        table_layout = QVBoxLayout()
        table.setLayout(table_layout)
        
        empty = QLabel("No invoices yet. Click '+ New Invoice' to create one.")
        empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet("color: #9E9E9E; padding: 60px;")
        table_layout.addWidget(empty)
        
        layout.addWidget(table, 1)
        
        self.pages.addWidget(page)
        
    def create_parties_page(self):
        """Parties page"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(16)
        page.setLayout(layout)
        
        toolbar = QHBoxLayout()
        
        add_btn = QPushButton("+ Add Party")
        apply_button_style(add_btn, "primary")
        add_btn.clicked.connect(self.add_party)
        toolbar.addWidget(add_btn)
        
        # Party type buttons
        for ptype in ["Customers", "Vendors"]:
            btn = QPushButton(ptype)
            apply_button_style(btn, "secondary")
            toolbar.addWidget(btn)
        
        toolbar.addStretch()
        layout.addLayout(toolbar)
        
        # Table
        table = QFrame()
        table.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        table_layout = QVBoxLayout()
        table.setLayout(table_layout)
        
        empty = QLabel("No parties yet. Add customers and vendors here.")
        empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet("color: #9E9E9E; padding: 60px;")
        table_layout.addWidget(empty)
        
        layout.addWidget(table, 1)
        
        self.pages.addWidget(page)
        
    def create_products_page(self):
        """Products page"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(16)
        page.setLayout(layout)
        
        toolbar = QHBoxLayout()
        
        add_btn = QPushButton("+ Add Product")
        apply_button_style(add_btn, "primary")
        add_btn.clicked.connect(self.add_product)
        toolbar.addWidget(add_btn)
        
        toolbar.addStretch()
        layout.addLayout(toolbar)
        
        table = QFrame()
        table.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        table_layout = QVBoxLayout()
        table.setLayout(table_layout)
        
        empty = QLabel("No products yet. Add items to your inventory.")
        empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet("color: #9E9E9E; padding: 60px;")
        table_layout.addWidget(empty)
        
        layout.addWidget(table, 1)
        
        self.pages.addWidget(page)
        
    def create_settings_page(self):
        """Settings page"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(16)
        page.setLayout(layout)
        
        # Company info card
        company_card = QFrame()
        company_card.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        card_layout = QVBoxLayout()
        company_card.setLayout(card_layout)
        
        title = QLabel("Company Information")
        title.setStyleSheet("font-size: 16px; font-weight: 600; padding: 16px;")
        card_layout.addWidget(title)
        
        info = QLabel("Company details and profile")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("color: #9E9E9E; padding: 40px;")
        card_layout.addWidget(info)
        
        layout.addWidget(company_card)
        
        # Other settings
        settings_grid = QHBoxLayout()
        
        # Users
        users_card = self.create_setting_card("User Management", "Manage users and permissions")
        settings_grid.addWidget(users_card, 1)
        
        # Backup
        backup_card = self.create_setting_card("Data Backup", "Backup and restore data")
        settings_grid.addWidget(backup_card, 1)
        
        # Print
        print_card = self.create_setting_card("Print Settings", "Configure invoices and printing")
        settings_grid.addWidget(print_card, 1)
        
        layout.addLayout(settings_grid)
        
        self.pages.addWidget(page)
        
    def create_setting_card(self, title, subtitle):
        """Create setting card"""
        card = QFrame()
        card.setStyleSheet("background-color: white; border: 1px solid #E0E0E0; border-radius: 8px;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        card.setLayout(layout)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 14px; font-weight: 600;")
        layout.addWidget(title_label)
        
        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet("font-size: 12px; color: #757575;")
        layout.addWidget(sub_label)
        
        return card
        
    def create_status_bar(self):
        """Status bar"""
        status = QStatusBar()
        status.setStyleSheet("""
            QStatusBar {
                background-color: white;
                border-top: 1px solid #E0E0E0;
                color: #757575;
                padding: 4px;
            }
        """)
        
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #757575;")
        status.addWidget(self.status_label)
        
        status.addPermanentWidget(QLabel("  |  "))
        
        self.time_label = QLabel(datetime.now().strftime("%d-%m-%Y %H:%M"))
        self.time_label.setStyleSheet("color: #757575;")
        status.addPermanentWidget(self.time_label)
        
        self.setStatusBar(status)
        
        # Timer for clock
        QTimer().singleShot(60000, self.update_time)
        
    def update_time(self):
        """Update status bar time"""
        self.time_label.setText(datetime.now().strftime("%d-%m-%Y %H:%M"))
        QTimer().singleShot(60000, self.update_time)
        
    def create_menu_bar(self):
        """Menu bar"""
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: white;
                border-bottom: 1px solid #E0E0E0;
                padding: 4px;
            }
            QMenuBar::item {
                padding: 6px 12px;
                color: #212121;
            }
            QMenuBar::item:selected {
                background-color: #E3F2FD;
            }
        """)
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        new_inv = QAction("New Invoice", self)
        new_inv.setShortcut("Ctrl+N")
        new_inv.triggered.connect(self.new_invoice)
        file_menu.addAction(new_inv)
        
        file_menu.addSeparator()
        
        backup = QAction("Backup Data", self)
        file_menu.addAction(backup)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Alt+F4")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Masters menu
        masters_menu = menubar.addMenu("Masters")
        masters_menu.addAction("Products", self.add_product)
        masters_menu.addAction("Customers", self.add_party)
        masters_menu.addAction("Vendors", self.add_party)
        
        # Reports menu
        reports_menu = menubar.addMenu("Reports")
        reports_menu.addAction("Sales Report")
        reports_menu.addAction("GST Reports")
        reports_menu.addAction("Party Statement")
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about = QAction("About", self)
        about.triggered.connect(self.show_about)
        help_menu.addAction(about)
        
    def navigate(self, page_code):
        """Navigate to page"""
        pages = {
            "dashboard": 0,
            "invoices": 1,
            "parties": 2,
            "products": 3,
            "settings": 4,
        }
        
        page = pages.get(page_code, 0)
        self.pages.setCurrentIndex(page)
        
        titles = {
            "dashboard": "Dashboard",
            "invoices": "Invoices",
            "parties": "Party Management",
            "products": "Product Master",
            "settings": "Settings",
        }
        
        self.page_title.setText(titles.get(page_code, "Dashboard"))
        
    def load_data(self):
        """Load data from database"""
        from models.db import fetch_all, execute
        
        # Load companies
        companies = fetch_all("SELECT * FROM companies WHERE is_active = 1")
        
        if not companies:
            # Insert sample company
            execute("""
                INSERT INTO companies (name, state, invoice_prefix)
                VALUES ('Demo Company', 'Maharashtra', 'INV')
            """)
            companies = fetch_all("SELECT * FROM companies")
        
        self.company_list.clear()
        for c in companies:
            self.company_list.addItem(c['name'])
            
        if companies:
            self.company_list.setCurrentRow(0)
            self.current_company_id = companies[0]['id']
            
    def on_company_changed(self, item):
        """Company changed"""
        self.current_company_id = item.data()
        
    def new_invoice(self):
        """New invoice"""
        from ui.forms.invoice_form import InvoiceEditor
        if self.current_company_id:
            dialog = InvoiceEditor(self.current_company_id)
            dialog.exec()
            
    def add_product(self):
        """Add product"""
        from ui.forms.product_form import ProductEditor
        if self.current_company_id:
            dialog = ProductEditor(self.current_company_id)
            dialog.exec()
            
    def add_party(self):
        """Add party"""
        from ui.forms.party_form import PartyEditor
        if self.current_company_id:
            dialog = PartyEditor(self.current_company_id)
            dialog.exec()
            
    def show_about(self):
        """About dialog"""
        QMessageBox.about(self, "About JAY INVOICE",
                        "JAY INVOICE v1.0.0\n\n"
                        "Professional Invoicing Software\n\n"
                        "Copyright 2026 JAY SOFTWARE")