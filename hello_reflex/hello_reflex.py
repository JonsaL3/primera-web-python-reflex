"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex import color

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


class SumarEntero:
    suma: int = 0
    def sumar_entero(self, x:int, y: int):
        self.suma = x + y




def index() -> rx.Component:
    sumarEntero = SumarEntero()
    return rx.container(
        rx.vstack(
            rx.text(
                "HOLA SOY UN TEXTO PACO SANZ " + str(sumarEntero.suma),
                size="9"
            ),
            rx.button(
                "Hola soy un botón en python",
                size="1",
                color_scheme="red",
                on_click=sumarEntero.sumar_entero(12, 12)
            )
        ),
    )


app = rx.App()
app.add_page(index)
