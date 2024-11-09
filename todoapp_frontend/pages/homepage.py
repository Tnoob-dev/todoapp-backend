import reflex as rx

from todoapp_frontend.components.navbar import navbar



def homepage() -> rx.Component:
    rx.box(
        rx.vstack(
            navbar(),
            rx.box(

            )
        )
    )