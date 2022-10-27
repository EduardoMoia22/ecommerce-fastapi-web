from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
from core.config import settings

class Produto(settings.DBBaseModel):
  __tablename__: str = 'produtos'

  id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
  nome: str = Column(String)
  descricao: str = Column(String)
  preco: float = Column(Float)
  quantidade: int = Column(Integer)
  usuarioID: int = Column(Integer, ForeignKey('usuarios.id'))