from fastapi import APIRouter, Query
from controllers.livro_controller import LivroController

router = APIRouter()

@router.get("/livros")
def get_livros(q: str = Query(None)):
    return LivroController.listar_livros(q)

@router.get("/livros/{livro_id}")
def get_livro_por_id(livro_id: int):
    return LivroController.buscar_por_id(livro_id)