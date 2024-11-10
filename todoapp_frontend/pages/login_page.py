import reflex as rx
from todoapp_frontend.views.login import login_view


def login_page() -> rx.Component:
    return login_view()