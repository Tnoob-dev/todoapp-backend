import reflex as rx

from todoapp_frontend.styles.styles import Size



def navbar() -> rx.Component:
    return rx.box(
        rx.stack(
            rx.text(
                "Todo App",
                font_size= Size.MEDIUM.value,
                color = "red"
            )
        ),
        position = "sticky",
        padding_x = Size.SMALL.value,
        padding_y = Size.SMALL.value,
        z_index = "999",
        top = "0"
    ) 