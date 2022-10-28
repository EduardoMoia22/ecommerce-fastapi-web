from datetime import datetime
from typing import List, Optional

from fastapi import HTTPException, status
from core.config import settings

class BaseCrudView:
  def __init__(self, templateBase: str) -> None:
    self.templateBase = templateBase

  # Método que renderiza a página com uma lista de todos os objetos condezentes ao seu controller
  async def renderPageWithlistOfAllObjects(self, objectController: object) -> Optional[List[object]]:
    listOfAllObjects = await objectController.getListOfAllObjects()

    context = {
      "request": objectController.request,
      "ano": datetime.now().year,
      "data": listOfAllObjects
    }

    return settings.TEMPLATES.TemplateResponse(f'admin/{self.templateBase}/listagem.html', context=context)

  # Método que renderiza a página com apenas um objeto referente ao id que foi passado
  async def renderPageWithOnlyOneOfObjects(self, objectController, objectID: int) -> Optional[object]:
    Object = await objectController.getOnlyOneOfObjects(objectID=objectID)

    if not Object:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    context = {
      "request": objectController.request,
      "ano": datetime.now().year,
      "data": Object
    }

    if 'detalhes' in str(objectController.request.url):
      return settings.TEMPLATES.TemplateResponse(f'admin/{self.templateBase}/detalhes.html', context=context)
    elif 'editar' in str(objectController.request.url):
      return settings.TEMPLATES.TemplateResponse(f'admin/{self.templateBase}/editar.html', context=context)
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
      