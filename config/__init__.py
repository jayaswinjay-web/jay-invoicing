# -*- coding: utf-8 -*-
"""
Configuration
"""

import os
import sys


def get_data_path():
    """Get application data directory"""
    if sys.platform == 'win32':
        base = os.environ.get('APPDATA', os.path.expanduser('~'))
    else:
        base = os.path.expanduser('~/.jay_invoice')
    
    path = os.path.join(base, 'JayInvoice')
    os.makedirs(path, exist_ok=True)
    return path


def get_db_path():
    """Get database path"""
    return os.path.join(get_data_path(), 'jay_invoice.db')


def get_backup_path():
    """Get backup directory"""
    return os.path.join(get_data_path(), 'backups')


def get_log_path():
    """Get log directory"""
    path = os.path.join(get_data_path(), 'logs')
    os.makedirs(path, exist_ok=True)
    return path