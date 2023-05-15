import time
from typing import Optional

import psycopg2
from fastapi import FastAPI, HTTPException, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


host = 'localhost'
database = 'fastapi'
user = 'postgres'
password = 'password'

while True:
    try:
        conn = psycopg2.connect(host=host, database=database, user=user,
                                password=password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("db conn was successfully")
        break
    except Exception as e:
        print("Db connection was failed")
        print("Error ", e)
        time.sleep(2)

my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1,
    },
    {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2,
    },
]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts;""")
    posts = cursor.fetchall()
    return posts


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s;""", (id,))
    post = cursor.fetchone()
    # post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} not found")
    else:
        return {"post_detail": post}


@app.post("/posts", status_code=201)
def create_posts(post: Post):
    # post_dict = post.dict()
    # post_dict["id"]= randrange(0, 100000000)
    # my_posts.append(post_dict)
    cursor.execute("""INSERT INTO posts (title, content, published) 
                      VALUES (%s, %s, %s) 
                      RETURNING *;""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""", (id,))
    deleted_post = cursor.fetchone()
    conn.commit()
    # index = find_index_post(id)
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} not found")
    # my_posts.pop(index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *;""",
                   (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    # index = find_index_post(id)
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id={id} not found")
    return {"data": updated_post}
