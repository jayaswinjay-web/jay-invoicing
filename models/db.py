# -*- coding: utf-8 -*-
"""
Database Manager - SQLite
"""

import sqlite3
import os
from config import get_db_path

_thread_local = sqlite3.connect


def get_connection():
    """Get database connection"""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Initialize database with full schema"""
    conn = get_connection()
    c = conn.cursor()
    
    c.executescript('''
    -- Companies
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT DEFAULT '',
        city TEXT DEFAULT '',
        state TEXT DEFAULT 'Maharashtra',
        pincode TEXT DEFAULT '',
        gstin TEXT DEFAULT '',
        pan TEXT DEFAULT '',
        cin TEXT DEFAULT '',
        email TEXT DEFAULT '',
        phone TEXT DEFAULT '',
        website TEXT DEFAULT '',
        logo_path TEXT DEFAULT '',
        signature_path TEXT DEFAULT '',
        bank_name TEXT DEFAULT '',
        bank_branch TEXT DEFAULT '',
        bank_account_no TEXT DEFAULT '',
        bank_ifsc TEXT DEFAULT '',
        invoice_prefix TEXT DEFAULT 'INV',
        current_invoice_no INTEGER DEFAULT 0,
        fy_start TEXT DEFAULT '04',
        fy_end TEXT DEFAULT '03',
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );

    -- Users
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        user_type TEXT DEFAULT 'user',
        company_id INTEGER,
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Godowns
    CREATE TABLE IF NOT EXISTS godowns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        address TEXT DEFAULT '',
        manager_name TEXT DEFAULT '',
        phone TEXT DEFAULT '',
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Categories
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        parent_id INTEGER DEFAULT 0,
        hsn_code TEXT DEFAULT '',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Products
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        code TEXT DEFAULT '',
        hsn_code TEXT DEFAULT '',
        category_id INTEGER DEFAULT 0,
        unit TEXT DEFAULT 'PCS',
        gst_rate REAL DEFAULT 18,
        purchase_rate REAL DEFAULT 0,
        sale_rate REAL DEFAULT 0,
        mrp REAL DEFAULT 0,
        min_stock INTEGER DEFAULT 0,
        is_active INTEGER DEFAULT 1,
        is_inventory INTEGER DEFAULT 1,
        open_stock INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );

    -- Parties (Customers/Vendors)
    CREATE TABLE IF NOT EXISTS parties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        code TEXT DEFAULT '',
        party_type TEXT DEFAULT 'customer',
        address TEXT DEFAULT '',
        city TEXT DEFAULT '',
        state TEXT DEFAULT '',
        pincode TEXT DEFAULT '',
        gstin TEXT DEFAULT '',
        pan TEXT DEFAULT '',
        email TEXT DEFAULT '',
        phone TEXT DEFAULT '',
        contact TEXT DEFAULT '',
        credit_limit REAL DEFAULT 0,
        payment_terms INTEGER DEFAULT 30,
        opening_balance REAL DEFAULT 0,
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Invoices
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        invoice_type TEXT DEFAULT 'sales',
        invoice_no TEXT NOT NULL,
        invoice_date TEXT NOT NULL,
        party_id INTEGER DEFAULT 0,
        party_name TEXT DEFAULT '',
        party_gstin TEXT DEFAULT '',
        party_address TEXT DEFAULT '',
        subtotal REAL DEFAULT 0,
        discount_amt REAL DEFAULT 0,
        cgst_amt REAL DEFAULT 0,
        sgst_amt REAL DEFAULT 0,
        igst_amt REAL DEFAULT 0,
        round_off REAL DEFAULT 0,
        grand_total REAL DEFAULT 0,
        paid_amount REAL DEFAULT 0,
        narration TEXT DEFAULT '',
        terms TEXT DEFAULT '',
        is_cancel INTEGER DEFAULT 0,
        created_by TEXT DEFAULT '',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id),
        FOREIGN KEY (party_id) REFERENCES parties(id)
    );

    -- Invoice Items
    CREATE TABLE IF NOT EXISTS invoice_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER NOT NULL,
        product_id INTEGER DEFAULT 0,
        product_name TEXT DEFAULT '',
        hsn_code TEXT DEFAULT '',
        unit TEXT DEFAULT 'PCS',
        quantity REAL DEFAULT 0,
        rate REAL DEFAULT 0,
        discount REAL DEFAULT 0,
        taxable REAL DEFAULT 0,
        gst_rate REAL DEFAULT 0,
        gst_amt REAL DEFAULT 0,
        total REAL DEFAULT 0,
        FOREIGN KEY (invoice_id) REFERENCES invoices(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    );

    -- Receipts
    CREATE TABLE IF NOT EXISTS receipts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        receipt_type TEXT DEFAULT 'receipt',
        voucher_no TEXT NOT NULL,
        voucher_date TEXT NOT NULL,
        party_id INTEGER DEFAULT 0,
        party_name TEXT DEFAULT '',
        amount REAL DEFAULT 0,
        mode TEXT DEFAULT 'cash',
        ref_no TEXT DEFAULT '',
        narration TEXT DEFAULT '',
        is_cancel INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id),
        FOREIGN KEY (party_id) REFERENCES parties(id)
    );

    -- Banks
    CREATE TABLE IF NOT EXISTS banks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        account_no TEXT DEFAULT '',
        ifsc_code TEXT DEFAULT '',
        branch TEXT DEFAULT '',
        opening_balance REAL DEFAULT 0,
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Settings
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        setting_key TEXT NOT NULL,
        setting_value TEXT DEFAULT '',
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    -- Indexes
    CREATE INDEX IF NOT EXISTS idx_invoices_company ON invoices(company_id);
    CREATE INDEX IF NOT EXISTS idx_invoices_date ON invoices(invoice_date);
    CREATE INDEX IF NOT EXISTS idx_invoices_party ON invoices(party_id);
    CREATE INDEX IF NOT EXISTS idx_products_company ON products(company_id);
    CREATE INDEX IF NOT EXISTS idx_parties_company ON parties(company_id);
    ''')
    
    conn.commit()
    
    # Add default admin user
    c.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if c.fetchone()[0] == 0:
        c.execute("""
            INSERT INTO users (username, password, user_type, company_id)
            VALUES ('admin', 'admin123', 'admin', NULL)
        """)
        conn.commit()
    
    conn.close()
    print("Database initialized")


def execute(query, params=None):
    """Execute query"""
    conn = get_connection()
    c = conn.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    conn.commit()
    return c


def fetch_one(query, params=None):
    """Fetch one row"""
    conn = get_connection()
    c = conn.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    return c.fetchone()


def fetch_all(query, params=None):
    """Fetch all rows"""
    conn = get_connection()
    c = conn.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    return c.fetchall()


def get_last_id():
    """Get last insert ID"""
    return fetch_one("SELECT last_insert_rowid() as id")['id']