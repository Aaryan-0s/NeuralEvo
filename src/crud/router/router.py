from fastapi import APIRouter,status
from src.crud.service.service import service
from src.crud.model.model import User

crud=APIRouter(prefix="/api/v1/crud",tags=["CRUD"])



@crud.get("/get",status_code=status.HTTP_200_OK)
async def crud_get(index:int):
    
    return service().get(index=index)
@crud.get("/getAll",status_code=status.HTTP_200_OK)
async def crud_getAll():
    
    return service().getAll()

@crud.post("/add",status_code=status.HTTP_200_OK)
async def crud_post(data:User):
    return service().add(data=data)


@crud.put("/update",status_code=status.HTTP_200_OK)
async def crud_put(index:int,data:User):
    updateUser=data.model_dump(exclude_unset=True)
           
    return service().update(index=index,data=updateUser)


@crud.delete("/delete",status_code=status.HTTP_200_OK)
async def crud_delete(index:int):
    return service().delete(index=index)