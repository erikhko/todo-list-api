from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

# 1. Cria a engine e as tabelas (se não existirem)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Função de dependência para obter a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de teste
@app.get("/")
def read_root():
    return {"message": "API de Tarefas funcionando!"}

# 2. Endpoint: Criar Nova Tarefa (POST)
@app.post("/tasks/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa no banco de dados.
    """
    # Cria uma nova instância do modelo Task
    db_task = models.Task(title=task.title)
    
    # Adiciona e salva a nova tarefa no banco de dados
    db.add(db_task)
    db.commit()
    db.refresh(db_task) # Atualiza o objeto para obter o ID gerado
    
    return db_task

# 3. Endpoint: Listar Todas as Tarefas (GET)
@app.get("/tasks/", response_model=list[schemas.TaskResponse])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna uma lista de tarefas, com paginação opcional (skip/limit).
    """
    # Consulta o banco de dados
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    
    return tasks

# 4. Endpoint: Buscar Tarefa por ID (GET)
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma única tarefa pelo seu ID.
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

# 5. Endpoint: Atualizar Tarefa (PATCH)
@app.patch("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskResponse, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente uma tarefa existente (ex: mudar o título ou o status is_done).
    """
    # 1. Busca a tarefa existente
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    # 2. Verifica se a tarefa existe
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # 3. Atualiza os campos se eles forem fornecidos na requisição
    # Verifica se o título foi fornecido e o atualiza
    if task.title:
        db_task.title = task.title
    
    # Verifica se o status is_done foi fornecido e o atualiza
    if task.is_done is not None:
        db_task.is_done = task.is_done

    # 4. Salva as alterações no banco de dados
    db.commit()
    db.refresh(db_task)
    
    return db_task

# 6. Endpoint: Excluir Tarefa (DELETE)
@app.delete("/tasks/{task_id}", status_code=204) # Retorna 204 (No Content) em caso de sucesso
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Exclui uma tarefa pelo seu ID.
    """
    # 1. Busca a tarefa
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    # 2. Verifica se a tarefa existe
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    # 3. Exclui a tarefa
    db.delete(db_task)
    db.commit()
    
    # Retorna uma resposta vazia com status 204 (No Content)
    return