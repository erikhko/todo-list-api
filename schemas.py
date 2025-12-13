from pydantic import BaseModel

# 1. Schema para CRIAR Tarefa (Dados de entrada)
class TaskCreate(BaseModel):
    """
    Define a estrutura dos dados esperados ao criar uma nova tarefa.
    Apenas o 'title' é necessário na entrada.
    """
    title: str

# 2. Schema para LER/RETORNAR Tarefa (Dados de saída)
class TaskResponse(BaseModel):
    """
    Define a estrutura completa dos dados de uma tarefa que será retornada.
    """
    id: int
    title: str
    is_done: bool
    
    # A classe Config permite que o modelo Pydantic funcione com ORMs (como o SQLAlchemy)
    class Config:
        from_attributes = True # ou 'orm_mode = True' dependendo da versão (from_attributes é mais moderno)