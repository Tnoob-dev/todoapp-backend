import reflex as rx

from todoapp_frontend.styles.styles import Color
from todoapp_frontend.styles.styles import TextColor
from todoapp_frontend.styles.styles import Size


def login_view() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.icon(
                            tag="circle-check",
                            size=64,
                            color=Color.ICON.value
                        )
                    )
                ),
                rx.box(
                    rx.center(
                        rx.vstack(
                            rx.heading(
                                "Todo APP",
                                color=TextColor.PRIMARY.value
                            ),
                            rx.text(
                                "Organiza tus tareas de manera eficiente",
                                color=TextColor.SECONDARY.value
                            ),
                            align="center",
                            spacing="1"
                        ),
                    ),
                ),
                rx.vstack(
                    rx.input(
                        rx.input.slot(
                            rx.icon(
                                tag="mail",
                                color=Color.ICON.value
                            )
                        ),
                        placeholder="Correo electrónico",
                        width="100%"
                    ),
                    rx.input(
                        rx.input.slot(
                            rx.icon(
                                tag="lock",
                                color=Color.ICON.value
                            )
                        ),
                        placeholder="Contraseña",
                        type="password",
                        width="100%"
                    ),
                    rx.button(
                        "Iniciar Sesión",
                        width="100%"
                    ),
                    width="100%",
                    spacing=Size.DEFAULT.value,
                    padding=Size.SMALL.value,
                ),
                spacing=Size.LARGE.value,
                align="center",
                width="100%"
            ),
            height=Size.CARD_HEIGHT.value,
            width=Size.CARD_WIDTH.value,
            border_radius=Size.MEDIUM.value,
            padding=Size.EXTRA_LARGE.value,
        )
    )