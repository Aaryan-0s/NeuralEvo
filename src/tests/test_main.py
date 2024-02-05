import sys
sys.path.append('D:\\jib\\crud')
from fastapi.testclient import TestClient   
from src.entrypoint.main import app
client=TestClient(app)
def test_blog():
    response=client.get("/api/v1/blog/get?blog_id=2")
    assert response.status_code==200
    assert response.json()=={
  "publication_date": "2024-02-05",
  "title": "string",
  "id": 2,
  "date_updated": "2024-02-05T18:23:16",
  "author": "string",
  "tags": [
    "string"
  ],
  "content": "stringstri",
  "date_created": "2024-02-05T18:23:16"
}
    
# def test_blog_getall():
#     response=client.get("/api/v1/blog/getall")
#     assert response.status_code==200
#     assert response.json()==[]

    
def test_blog_add():
    response=client.post("/api/v1/blog/add",json={"title": "string",
  "content": "stringstri",
  "author": "string",
  "publication_date": "2024-02-05",
  "tags": [
    "string"
  ]})
    assert response.status_code==200
    assert response.json()=={"title":"Test","content":"Test Content"}