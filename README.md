<div align="center">
  <h1>📄 Jay Invoicing</h1>
  <p><em>Automated invoicing system for small and medium businesses</em></p>

  <p>
    <img src="https://img.shields.io/badge/language-Python-3776AB?style=flat-square&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/UI-PyQt5-41CD52?style=flat-square&logo=qt" alt="PyQt5">
    <img src="https://img.shields.io/badge/database-SQLite-003B57?style=flat-square&logo=sqlite" alt="SQLite">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License">
  </p>
</div>

## Overview

Jay Invoicing is a desktop application for generating, managing, and tracking invoices. Built with Python and PyQt5, it provides a clean, professional interface for small and medium businesses to handle their billing needs.

Part of the JAY TECH SOLUTIONS product suite.

## Features

- **Invoice generation** — Create professional invoices with custom branding
- **Client management** — Store and manage client information
- **Payment tracking** — Track paid, pending, and overdue invoices
- **Report generation** — Generate business reports and summaries
- **Database storage** — SQLite-based persistent storage
- **Export options** — Export invoices as PDF
- **GST compliance** — Supports Indian GST tax structure

## Quick Start

### Prerequisites

- Python 3.8+
- PyQt5

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

### Build Standalone Executable

```bash
python build_minimal.py
```

Or using PyInstaller directly:

```bash
pyinstaller JayInvoice.spec
```

## Project Structure

```
jay-invoicing/
├── main.py                 # Application entry point
├── controllers/            # Business logic controllers
├── models/                 # Database models
├── ui/                     # PyQt5 user interface
├── utils/                  # Utility functions
├── assets/                 # Icons, templates, branding
├── config/                 # Application configuration
├── migrations/             # Database migrations
├── reports/                # Report templates
├── tests/                  # Unit tests
├── gst/                    # GST compliance modules
├── installer/              # Installer configuration
├── requirements.txt        # Python dependencies
└── JayInvoice.spec         # PyInstaller spec file
```

## About JAY TECH SOLUTIONS

Jay Invoicing is part of the [JAY TECH SOLUTIONS](https://jaytechsoln.in) product suite — a collection of business software products serving 50,000+ users across India.

## License

MIT License
