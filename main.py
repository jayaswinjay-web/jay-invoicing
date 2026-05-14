# -*- coding: utf-8 -*-
"""
JAY INVOICE - Main Entry Point
"""

import sys
import os

# Add project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from config import get_data_path
from models.db import init_database

def main():
    """Main entry"""
    # Initialize data directory
    os.makedirs(get_data_path(), exist_ok=True)
    
    # Initialize database
    init_database()
    
    # Run application
    from PyQt6.QtWidgets import QApplication
    from ui.main_window import MainWindow
    
    app = QApplication(sys.argv)
    app.setApplicationName("JAY INVOICE")
    app.setOrganizationName("JayInvoice")
    
    window = MainWindow()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())