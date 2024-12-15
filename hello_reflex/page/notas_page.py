import reflex as rx

from hello_reflex.state.notas_state import NotasState


def notas_page():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Título",
                    name="title",
                ),
                rx.text_area(
                    placeholder="Contenido",
                    name="content",
                ),
                rx.button(
                    "Añadir a la lista",
                    type="submit"
                ),
                rx.text(NotasState.message)
            ),
            on_submit=NotasState.save_note
        )
    )
