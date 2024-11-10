import reflex as rx
from enum import Enum

# Global constants
MAX_WIDTH = "1600px"

# Enum for sizes
class Size(Enum):
    SMALL = "0.5rem"
    MEDIUM = "0.75rem"
    DEFAULT = "1rem"
    LARGE = "1.5rem"
    EXTRA_LARGE = "2rem"
    ICON = "1.25rem"
    ICON_LARGE = "4rem"
    CARD_WIDTH = "28rem"
    CARD_HEIGHT = "auto"
    BUTTON_HEIGHT = "2.5rem"

# Enum for colors
class Color(Enum):
    BACKGROUND = "#1e1e1e"
    CONTAINER = "#252525"
    INPUT = "#2a2a2a"
    BUTTON = "#3a3a3a"
    BUTTON_HOVER = "#4a4a4a"
    BORDER = "#4b5563"
    ICON = "#9ca3af"

# Enum for text colors
class TextColor(Enum):
    PRIMARY = "#ffffff"
    SECONDARY = "#d1d5db"
    PLACEHOLDER = "#6b7280"

# Enum for fonts
class Font(Enum):
    DEFAULT = "Inter, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    SIZE_SMALL = "0.875rem"
    SIZE_DEFAULT = "1rem"
    SIZE_LARGE = "1.25rem"
    SIZE_TITLE = "2.25rem"
    WEIGHT_NORMAL = "400"
    WEIGHT_MEDIUM = "500"
    WEIGHT_BOLD = "700"


BASE_STYLE = {
    rx.card: {
        "background_color": Color.CONTAINER.value,
        "border_radius": Size.MEDIUM.value,
        "border_color": Color.BORDER.value,
        "border_width": "1px",
        "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        "padding": Size.EXTRA_LARGE.value,
        "text_align": "center",
    },
    rx.button: {
        "background_color": Color.BUTTON.value,
        "color": TextColor.PRIMARY.value,
        "border_radius": Size.SMALL.value,
        "padding": f"{Size.DEFAULT.value} {Size.EXTRA_LARGE.value}",
        "height": Size.BUTTON_HEIGHT.value,
        "width": "100%",
        "_hover": {"background_color": Color.BUTTON_HOVER.value},
    },
    rx.input: {
        "background_color": Color.INPUT.value,
        "border_color": Color.BORDER.value,
        "border_width": "1px",
        "border_radius": Size.SMALL.value,
        "color": TextColor.PRIMARY.value,
        "padding": f"{Size.SMALL.value} {Size.DEFAULT.value}",
        "height": "3rem",  # Aumentamos la altura
        "width": "100%",
        "_placeholder": {"color": TextColor.PLACEHOLDER.value},
        "padding_left": Size.LARGE.value,
        "active": {
            "border_color": Color.BORDER.value,
            "box_shadow": "0 0 0 0.25rem rgba(100, 100, 100, 0.25)",
        }
    },
    "background_color": Color.BACKGROUND.value,
    "max_width": MAX_WIDTH,
    "height": "100vh",
}