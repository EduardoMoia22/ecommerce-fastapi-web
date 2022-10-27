from typing import List, Optional
from fastapi import Request
from core.database import get_session
from sqlalchemy import select

class BaseCrudController:
  def __init__(self, baseModel: object, request: Request) -> None:
    self.model = baseModel
    self.request = request

  # Método genérico que recebe o id do objeto e o retorna com as
  # informações correspondentes
  async def getOneModelObject(self, objID: int) -> Optional[object]:
    async with get_session() as session:
      obj: self.model = await session.get(self.model, objID)

      return obj

  # Método que retorna uma lista de objetos com as informações que correspondem 
  # ao seu model 
  async def getAllModelObjects(self) -> Optional[List[object]]:
    async with get_session as session:
      query = select(self.model)
      result = await session.execute(query)

      return result.scalars().unique().all()

  # Método que recebe o id do objeto e o deleta
  async def delModelObject(self, objID: int) -> None:
    async with get_session() as session:
      obj: self.model = await session.get(self.model, objID)

      if obj:
        session.delete(obj)
        await session.commit()
      