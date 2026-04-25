from persistence.livro_repo import LivroRepository



class LivroController:
    @staticmethod
    def listar_livros(q: str = None):
        """
        Orquestra a lógica de negócio (US01):
        Se houver termo de busca, filtra. Se não, traz todos.
        """
        if q:
            # Chama o método de filtro da camada de Persistência
            return LivroRepository.filtrar_por_titulo(q)

        # Chama o método de listagem geral da camada de Persistência
        return LivroRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(livro_id: int):
        return LivroRepository.buscar_por_id(livro_id)