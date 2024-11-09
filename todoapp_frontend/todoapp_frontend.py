import reflex as rx

from todoapp_frontend.components.navbar import navbar


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(
            )
        )
    )


app = rx.App()
app.add_page(index)
