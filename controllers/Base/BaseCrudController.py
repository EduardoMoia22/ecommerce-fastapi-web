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
  async def getOnlyOneOfObjects(self, objectID: int) -> Optional[object]:
    async with get_session() as session:
      Object: self.model = await session.get(self.model, objectID)

      return Object

  # Método que retorna uma lista de objetos com as informações que correspondem 
  # ao seu model 
  async def getListOfAllObjects(self) -> Optional[List[object]]:
    async with get_session as session:
      query = select(self.model)
      listOfAllObjects = await session.execute(query)

      return listOfAllObjects.scalars().unique().all()

  # Método que recebe o id do objeto e o deleta
  async def delModelObject(self, objectID: int) -> None:
    async with get_session() as session:
      Object: self.model = await session.get(self.model, objectID)

      if Object:
        session.delete(Object)
        await session.commit()
      