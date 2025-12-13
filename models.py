from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Task(Base):
    """
    Define a tabela 'tasks' no banco de dados.
    """
    __tablename__ = "tasks"

    # Coluna 1: Chave primária, autoincrementável
    id = Column(Integer, primary_key=True, index=True) 
    
    # Coluna 2: O título da tarefa (ex: 'Comprar pão')
    title = Column(String, index=True)
    
    # Coluna 3: O status da tarefa (True = Concluída, False = Pendente)
    is_done = Column(Boolean, default=False)
    
    # Método para representação amigável ao imprimir o objeto
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', is_done={self.is_done})>"