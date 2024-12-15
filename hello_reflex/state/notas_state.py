import reflex as rx

from hello_reflex.model.nota_model import NotaModel


# "State" es como los viewmodels de android. A ojos de la UI son singleton
class NotasState(rx.State):
    message = ""
    # Si queremos persistirlo en la base de datos debemos hacerlo aquí.
    def save_note(self, data: dict):
        print("tratando de guardar en BBDD -> " + str(data))
        with rx.session() as db:
            title = data["title"]
            content = data["content"]
            print("title: " + title)
            print("content: " + content)
            new_note: NotaModel = NotaModel(title=title, content=content)
            db.add(new_note)
            db.commit()
            NotasState.message = "Nota guardada exitosamente."
