<div align="center">
  <img src="https://raw.githubusercontent.com/jayaswinjay-web/shared-assets/main/screenshots/jay-invoicing-demo.svg" width="100%" alt="Jay Invoicing Screenshot">
</div>

<br>

<div align="center">

[![License](https://img.shields.io/github/license/jayaswinjay-web/jay-invoicing?style=flat&color=1a8a7a)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/jayaswinjay-web/jay-invoicing?style=flat&color=1a8a7a)](https://github.com/jayaswinjay-web/jay-invoicing/commits)
[![CI](https://github.com/jayaswinjay-web/jay-invoicing/actions/workflows/ci.yml/badge.svg)](https://github.com/jayaswinjay-web/jay-invoicing/actions)
[![Repo Size](https://img.shields.io/github/repo-size/jayaswinjay-web/jay-invoicing?style=flat&color=1a8a7a)](https://github.com/jayaswinjay-web/jay-invoicing)
[![Stars](https://img.shields.io/github/stars/jayaswinjay-web/jay-invoicing?style=social)](https://github.com/jayaswinjay-web/jay-invoicing)

---

### ⭐ Support This Project — [Star on GitHub](https://github.com/jayaswinjay-web/jay-invoicing) ⭐

---

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

## Show Your Support

- ⭐ **Star this repo** — helps others discover it
- 🐛 **Report issues** — I respond within 24 hours
- 📬 **Share feedback** — contact@jaytechsoln.in
- ☕ **Buy me a coffee** — [Sponsor](https://github.com/sponsors/jayaswinjay-web)

Made with ❤️ by [Aswin Jay](https://github.com/Aswinajay) — part of [JAY TECH SOLUTIONS](https://jaytechsoln.in)

## License

MIT License
