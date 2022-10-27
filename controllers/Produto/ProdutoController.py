from core.database import get_session
from fastapi import Request
from controllers.Base.BaseCrudController import BaseCrudController
from models.ProdutoModel import Produto


class ProdutoController(BaseCrudController):
  def __init__(self, request: Request) -> None:
      super().__init__(Produto, request)


  # Método que cria um novo objeto produto e salva no banco de dados
  async def createProduto(self) -> None:
    formWithRequestInformation = await self.request.form()

    nome: str = formWithRequestInformation.get('nome')
    descricao: str = formWithRequestInformation.get('descricao')
    preco: str = formWithRequestInformation.get('preco')
    quantidade: str = formWithRequestInformation.get('quantidade')
    usuarioID: int = self.request.path_params['usuarioID']

    newProdutoInstance: Produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade, usuarioID=usuarioID)

    async with get_session() as session:
      session.add(newProdutoInstance)
      await session.commit()

