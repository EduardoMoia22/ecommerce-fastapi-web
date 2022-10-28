from datetime import datetime

from fastapi.routing import APIRouter
from fastapi.requests import Request

from core.config import settings
from views.Produto.ProdutoView import produtoView

router = APIRouter(prefix='/admin')
router.include_router(produtoView.router, prefix='/admin')

@router.get('/', name='AdminIndex')
async def adminIndex(request: Request):
    context = {
        "request": request,
        "ano": datetime.now().year
    }

    return settings.TEMPLATES.TemplateResponse('admin/index.html', context=context)