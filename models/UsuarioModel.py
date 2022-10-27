from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from core.config import settings

class Usuario(settings.DBBaseModel):
  __tablename__: str = 'usuarios'

  id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
  nome: str = Column(String)
  email: str = Column(String)
  senha: str = Column(String)
  produto: int = relationship("Produto")