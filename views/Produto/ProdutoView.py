from fastapi import Response
from fastapi.requests import Request
from controllers.Produto.ProdutoController import ProdutoController
from views.Base.BaseCrudView import BaseCrudView
from starlette.routing import Route
from fastapi.routing import APIRouter


class ProdutoView(BaseCrudView):
  def __init__(self) -> None:
      self.router = APIRouter()

      self.router.routes.append(Route(path='/produto/listagem', endpoint=self.renderPageWithlistOfAllObjects, methods=["GET"], name='ListOfAllObjects'))
      self.router.routes.append(Route(path='/produto/detalhes/{produtoID:int}', endpoint=self.renderPageWithOnlyOneOfObjects, methods=["GET"], name='OnlyOneOfObjects'))
      
      super().__init__('produto')
 
  async def renderPageWithOnlyOneOfObjects(self, request: Request) -> Response:
    InstanceOfProdutoController: ProdutoController = ProdutoController(request)
    
    produtoIDFromRequestUrl = request.path_params['produtoID']
    
    return await super().renderPageWithOnlyOneOfObjects(objectController=InstanceOfProdutoController, objectID=produtoIDFromRequestUrl)

  async def renderPageWithlistOfAllObjects(self, request: Request) -> Response:
    InstaceOfProdutoController: ProdutoController = ProdutoController(request)

    return await super().renderPageWithlistOfAllObjects(objectController=InstaceOfProdutoController)

produtoView: ProdutoView = ProdutoView()