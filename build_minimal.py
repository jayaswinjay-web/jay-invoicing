# -*- mode: python ; coding: utf-8 -*-
import PyInstaller.__main__
import sys

# Minimal build script - only includes PyQt6 essentials
sys.argv = [
    'pyinstaller',
    '--name=JayInvoice',
    '--windowed',
    '--onefile',
    '--add-data=config;config',
    '--add-data=ui;ui',
    '--add-data=models;models',
    '--add-data=utils;utils',
    '--hidden-import=sqlite3',
    '--hidden-import=xml.etree.cElementTree',
    '--exclude-module=matplotlib',
    '--exclude-module=scipy', 
    '--exclude-module=numpy',
    '--exclude-module=pandas',
    '--exclude-module=pytest',
    '--exclude-module=IPython',
    'main.py'
]

if __name__ == '__main__':
    PyInstaller.__main__.run()