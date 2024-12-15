from reflex.model import Model
from sqlalchemy import Column, Integer, String


class NotaModel(Model):
    __tablename__ = "NOTA"  # Los nombres de tablas suelen estar en minúsculas
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
