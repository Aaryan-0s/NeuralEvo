from src.crud.repository.repository import repo
from sqlalchemy.orm import Session

class CrudService:
    def __init__(self,db:Session):
        self.repo=repo(db)

    def get(self,index):
        msg=self.repo.get(index=index)
        return msg
    def getAll(self):
        msg=self.repo.getAll()
        return msg

    def add(self,data):
        return self.repo.add(item=data)
    
    def update(self,index,data):
        data1=self.repo.get(index=index)
       
        for key,value in data.items():
           setattr(data1,key,value)
        
        
        return self.repo.update(change=data1)
    
    def delete(self,index):
        return self.repo.delete(index=index)

    


service=CrudService