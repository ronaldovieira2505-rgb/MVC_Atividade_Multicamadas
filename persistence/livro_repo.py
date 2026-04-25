from models.livro_model import Livro

# Banco simulado "turbinado" com 20 livros
_dados = [
    Livro(1, "O Senhor dos Anéis", 89.90, "Uma jornada épica para destruir o Um Anel."),
    Livro(2, "1984", 45.50, "Um futuro distópico onde o Estado controla tudo."),
    Livro(3, "O Guia do Mochileiro das Galáxias", 39.90, "Aventuras espaciais com toques de humor britânico."),
    Livro(4, "Código Limpo", 95.00, "Habilidades práticas para escrever códigos melhores e mais limpos."),
    Livro(5, "Dom Casmurro", 29.90, "O clássico de Machado de Assis sobre dúvida e ciúme."),
    Livro(6, "Harry Potter e a Pedra Filosofal", 55.00, "O início da saga do bruxo mais famoso do mundo."),
    Livro(7, "O Pequeno Príncipe", 19.90, "Uma fábula atemporal sobre amizade e valores."),
    Livro(8, "Sapiens: Uma Breve História da Humanidade", 68.00, "Uma investigação sobre o papel dos humanos no planeta."),
    Livro(9, "Sherlock Holmes: Um Estudo em Vermelho", 34.50, "O primeiro mistério desvendado pelo detetive Sherlock Holmes."),
    Livro(10, "Admirável Mundo Novo", 42.00, "Uma sociedade organizada por castas e felicidade artificial."),
    Livro(11, "O Hobbit", 49.90, "A aventura de Bilbo Bolseiro antes de O Senhor dos Anéis."),
    Livro(12, "Fahrenheit 451", 48.00, "Um mundo onde livros são proibidos e queimados."),
    Livro(13, "Algoritmos: Teoria e Prática", 180.00, "A 'bíblia' dos algoritmos para estudantes de engenharia."),
    Livro(14, "Orgulho e Preconceito", 35.00, "O romance clássico de Jane Austen sobre sociedade e amor."),
    Livro(15, "Crime e Castigo", 59.00, "Um mergulho na psicologia de um crime e sua redenção."),
    Livro(16, "Cem Anos de Solidão", 64.00, "A história multigeracional da família Buendía em Macondo."),
    Livro(17, "O Alquimista", 32.00, "A jornada de um pastor em busca de sua Lenda Pessoal."),
    Livro(18, "O Sol é Para Todos", 46.00, "Um olhar sobre o preconceito racial no sul dos EUA."),
    Livro(19, "Arquitetura Limpa", 92.00, "O guia do artesão para estrutura e design de software."),
    Livro(20, "O Retrato de Dorian Gray", 38.00, "Um pacto para manter a juventude eterna a qualquer custo.")
]

class LivroRepository:
    @staticmethod
    def buscar_todos():
        return _dados

    @staticmethod
    def filtrar_por_titulo(termo: str):
        termo = termo.lower()
        return [livro for livro in _dados if termo in livro.titulo.lower()]

    @staticmethod
    def buscar_por_id(livro_id: int):
        for livro in _dados:
            if livro.id == livro_id:
                return livro
        return None