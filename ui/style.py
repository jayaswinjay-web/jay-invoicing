# -*- coding: utf-8 -*-
"""
JAY INVOICE - Professional Modern UI
Clean, business-focused design without emojis
"""

from PyQt6.QtCore import Qt, QSize, QPoint, QRect, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QColor, QPalette, QLinearGradient, QPainter, QBrush
from PyQt6.QtWidgets import QProxyStyle, QStyleFactory


# Color scheme - Professional business palette
class AppColors:
    PRIMARY = "#2E7DD1"          # Professional Blue
    PRIMARY_HOVER = "#1A5CB0"    # Darker blue
    PRIMARY_LIGHT = "#E3F2FD"     # Light blue background
    SECONDARY = "#5C6BC0"        # Indigo
    SUCCESS = "#4CAF50"         # Green
    SUCCESS_LIGHT = "#E8F5E9"  # Light green
    WARNING = "#FF9800"         # Orange
    WARNING_LIGHT = "#FFF3E0"    # Light orange
    DANGER = "#F44336"          # Red
    DANGER_LIGHT = "#FFEBEE"    # Light red
    
    TEXT_PRIMARY = "#212121"      # Near black
    TEXT_SECONDARY = "#757575"     # Gray
    TEXT_DISABLED = "#BDBDBD"     # Light gray
    
    BACKGROUND = "#FAFAFA"         # Off-white
    BACKGROUND_CARD = "#FFFFFF"   # White
    BACKGROUND_DARK = "#1E1E1E" # Dark mode
    
    BORDER = "#E0E0E0"         # Light border
    BORDER_DARK = "#424242"      # Dark border
    
    DIVIDER = "#EEEEEE"
    
    # Sidebar colors
    SIDEBAR_BG = "#1E2A38"
    SIDEBAR_ACTIVE = "#2E7DD1"
    SIDEBAR_TEXT = "#AAB4BE"
    SIDEBAR_TEXT_ACTIVE = "#FFFFFF"


# App Fonts
class AppFonts:
    @staticmethod
    def title():
        font = QFont()
        font.setPointSize(18)
        font.setWeight(QFont.Weight.Bold)
        return font
    
    @staticmethod
    def heading():
        font = QFont()
        font.setPointSize(16)
        font.setWeight(QFont.Weight.SemiBold)
        return font
    
    @staticmethod
    def subheading():
        font = QFont()
        font.setPointSize(14)
        font.setWeight(QFont.Weight.Medium)
        return font
    
    @staticmethod
    def body():
        font = QFont()
        font.setPointSize(13)
        font.setWeight(QFont.Weight.Normal)
        return font
    
    @staticmethod
    def caption():
        font = QFont()
        font.setPointSize(11)
        font.setWeight(QFont.Weight.Normal)
        return font
    
    @staticmethod
    def mono():
        font = QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        return font


# Professional Style Base
class ProfessionalStyle(QProxyStyle):
    def __init__(self):
        super().__init__("Fusion")
    
    def standardPalette(self):
        palette = QPalette()
        
        # Base colors
        palette.setColor(QPalette.ColorRole.Window, QColor(AppColors.BACKGROUND))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(AppColors.TEXT_PRIMARY))
        palette.setColor(QPalette.ColorRole.Base, QColor(AppColors.BACKGROUND_CARD))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#F5F5F5"))
        
        # Tooltip
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#2E2E2E"))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#FFFFFF"))
        
        # Text
        palette.setColor(QPalette.ColorRole.Text, QColor(AppColors.TEXT_PRIMARY))
        palette.setColor(QPalette.ColorRole.TextDisabled, QColor(AppColors.TEXT_DISABLED))
        
        # Buttons
        palette.setColor(QColor.Button, QColor("#E0E0E0"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(AppColors.TEXT_PRIMARY))
        palette.setColor(QPalette.ColorRole.ButtonTextDisabled, QColor(AppColors.TEXT_DISABLED))
        
        # Highlights
        palette.setColor(QPalette.ColorRole.Highlight, QColor(AppColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#FFFFFF"))
        palette.setColor(QPalette.ColorRole.Link, QColor(AppColors.PRIMARY))
        palette.setColor(QPalette.ColorRole.LinkVisited, QColor("#7B1FA2"))
        
        # Bright text
        palette.setColor(QPalette.ColorRole.BrightText, QColor("#FFFFFF"))
        
        return palette


# CSS Styles
CSS = {
    # Main window
    "window": """
        QMainWindow { background-color: #FAFAFA; }
        QWidget { font-family: 'Segoe UI', Arial; font-size: 13px; }
    """,
    
    # Push buttons
    "btn_primary": """
        QPushButton {
            background-color: #2E7DD1;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
            min-width: 80px;
        }
        QPushButton:hover { background-color: #1A5CB0; }
        QPushButton:pressed { background-color: #0D47A1; }
        QPushButton:disabled { background-color: #BDBDBD; color: #757575; }
    """,
    
    "btn_secondary": """
        QPushButton {
            background-color: #F5F5F5;
            color: #212121;
            border: 1px solid #BDBDBD;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
        }
        QPushButton:hover { background-color: #EEEEEE; }
        QPushButton:pressed { background-color: #E0E0E0; }
    """,
    
    "btn_success": """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
        }
        QPushButton:hover { background-color: #388E3C; }
        QPushButton:pressed { background-color: #2E7D32; }
    """,
    
    "btn_danger": """
        QPushButton {
            background-color: #F44336;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
        }
        QPushButton:hover { background-color: #D32F2F; }
        QPushButton:pressed { background-color: #C62828; }
    """,
    
    "btn_icon": """
        QPushButton {
            background-color: transparent;
            color: #757575;
            border: none;
            border-radius: 4px;
            padding: 8px;
        }
        QPushButton:hover { background-color: #F5F5F5; color: #212121; }
    """,
    
    # Line edits
    "input": """
        QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            padding: 8px 12px;
            color: #212121;
        }
        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #2E7DD1;
        }
        QLineEdit:disabled, QTextEdit:disabled {
            background-color: #F5F5F5;
            color: #9E9E9E;
        }
    """,
    
    # Combo boxes
    "combo": """
        QComboBox {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            padding: 8px 12px;
        }
        QComboBox:focus { border: 2px solid #2E7DD1; }
        QComboBox::drop-down { border: none; width: 24px; }
        QComboBox::down-arrow { image: none; border: 4px solid transparent; border-top-color: #757575; }
    """,
    
    # Tables
    "table": """
        QTableWidget {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            gridline-color: #EEEEEE;
        }
        QTableWidget::item {
            padding: 8px;
            border: none;
        }
        QTableWidget::item:selected {
            background-color: #E3F2FD;
            color: #212121;
        }
        QHeaderView::section {
            background-color: #F5F5F5;
            padding: 10px;
            border: none;
            border-bottom: 2px solid #2E7DD1;
            font-weight: 600;
            color: #212121;
        }
    """,
    
    # Cards
    "card": """
        QFrame {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
        }
    """,
    
    # Group boxes
    "group": """
        QGroupBox {
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            margin-top: 16px;
            padding-top: 16px;
            font-weight: 600;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 8px;
            color: #2E7DD1;
        }
    """,
    
    # Tabs
    "tabs": """
        QTabWidget::pane {
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            background-color: white;
        }
        QTabBar::tab {
            background-color: #F5F5F5;
            padding: 10px 20px;
            border: 1px solid #E0E0E0;
            border-bottom: none;
            color: #757575;
        }
        QTabBar::tab:selected {
            background-color: white;
            color: #2E7DD1;
            border-bottom: 2px solid #2E7DD1;
        }
        QTabBar::tab:hover:!selected {
            background-color: #EEEEEE;
        }
    """,
    
    # Menu
    "menu": """
        QMenuBar {
            background-color: white;
            border-bottom: 1px solid #E0E0E0;
        }
        QMenuBar::item {
            padding: 8px 16px;
            color: #212121;
        }
        QMenuBar::item:selected {
            background-color: #E3F2FD;
            color: #2E7DD1;
        }
        QMenu {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 4px;
        }
        QMenu::item {
            padding: 8px 32px 8px 16px;
            color: #212121;
        }
        QMenu::item:selected {
            background-color: #E3F2FD;
        }
    """,
    
    # Status bar
    "status": """
        QStatusBar {
            background-color: #F5F5F5;
            border-top: 1px solid #E0E0E0;
            color: #757575;
        }
    """,
    
    # Labels
    "label_title": """
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #212121;
        }
    """,
    
    "label_heading": """
        QLabel {
            font-size: 16px;
            font-weight: 600;
            color: #212121;
        }
    """,
    
    "label_sub": """
        QLabel {
            font-size: 14px;
            color: #757575;
        }
    """,
    
    "label_caption": """
        QLabel {
            font-size: 11px;
            color: #9E9E9E;
        }
    """,
    
    # Stat cards
    "stat_card": """
        QFrame {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 16px;
        }
    """,
}


def get_css(key):
    """Get CSS by key"""
    return CSS.get(key, "")


def apply_button_style(btn, style_type="primary"):
    """Apply button style"""
    styles = {
        "primary": CSS["btn_primary"],
        "secondary": CSS["btn_secondary"],
        "success": CSS["btn_success"],
        "danger": CSS["btn_danger"],
        "icon": CSS["btn_icon"],
    }
    btn.setStyleSheet(styles.get(style_type, CSS["btn_primary"]))


def apply_input_style(widget):
    """Apply input style"""
    if hasattr(widget, "setStyleSheet"):
        widget.setStyleSheet(CSS["input"])


def apply_combo_style(widget):
    """Apply combo style"""
    if hasattr(widget, "setStyleSheet"):
        widget.setStyleSheet(CSS["combo"])


def apply_table_style(table):
    """Apply table style"""
    table.setStyleSheet(CSS["table"])
    table.setAlternatingRowColors(True)
    table.setShowGrid(True)
    table.setGridStyle(Qt.PenStyle.SolidLine)
    table.horizontalHeader().setStretchLastSection(True)
    table.verticalHeader().setVisible(False)


def apply_card_style(frame):
    """Apply card style"""
    frame.setStyleSheet(CSS["card"])
    frame.setFrameShape(QFrame.Shape.StyledPanel)


def create_title_label(text):
    """Create title label"""
    label = QLabel(text)
    label.setStyleSheet(CSS["label_title"])
    return label


def create_heading_label(text):
    """Create heading label"""
    label = QLabel(text)
    label.setStyleSheet(CSS["label_heading"])
    return label


def create_caption_label(text):
    """Create caption label"""
    label = QLabel(text)
    label.setStyleSheet(CSS["label_caption"])
    return label


# Animation helpers
def fade_in(widget, duration=200):
    """Fade in animation"""
    widget.setWindowOpacity(0)
    anim = QPropertyAnimation(widget, b"windowOpacity")
    anim.setDuration(duration)
    anim.setStartValue(0)
    anim.setEndValue(1)
    anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
    anim.start()


def slide_in(widget, direction="left", duration=300):
    """Slide in animation"""
    if direction == "left":
        start = QPoint(-widget.width(), 0)
        end = QPoint(0, 0)
    elif direction == "right":
        start = QPoint(widget.width(), 0)
        end = QPoint(0, 0)
    elif direction == "up":
        start = QPoint(0, widget.height())
        end = QPoint(0, 0)
    else:
        start = QPoint(0, -widget.height())
        end = QPoint(0, 0)
    
    widget.move(start)
    widget.setVisible(True)
    
    anim = QPropertyAnimation(widget, b"pos")
    anim.setDuration(duration)
    anim.setStartValue(start)
    anim.setEndValue(end)
    anim.setEasingCurve(QEasingCurve.Type.OutCubic)
    anim.start()