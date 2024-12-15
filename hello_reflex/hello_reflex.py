import reflex as rx

from hello_reflex.page.notas_page import notas_page


def index() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Mi primera web en reflex!!!",
            font_size="2em",
        ),
        rx.link(
            "Ejemplo manejo notas BBDD",
            href="/notas"
        ),
    )


# Crear la aplicación y registrar el estado
app = rx.App()
app.add_page(index)
app.add_page(notas_page, route="/notas")
