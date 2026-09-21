from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
from app.db import Post, create_db_and_table, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_table
    yield

app = FastAPI(lifespan=lifespan)

posts = {
    1: {"title": "YouTube", "description": "YouTube thumbnail"},
    2: {"title": "Twitter", "description": "X tweet"},
    3: {"title": "TikTok", "description": "Short video"},
    4: {"title": "Instagram", "description": "Instagram post"},
    5: {"title": "Facebook", "description": "Facebook update"},
    6: {"title": "LinkedIn", "description": "Professional post"},
    7: {"title": "Reddit", "description": "Reddit discussion"},
    8: {"title": "Discord", "description": "Discord announcement"},
    9: {"title": "Pinterest", "description": "Pinterest pin"},
    10: {"title": "Blog", "description": "Blog article"},
    11: {"title": "Newsletter", "description": "Email newsletter"},
}


@app.get("/posts")
def get_all_posts(limit: int | None = None):
    if limit:
        return list(posts.values())[:limit]
    return posts


@app.get("/post/{id}")
def get_post_by_id(id: int):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.get(id)


@app.post("/post")
def create_post(post: PostCreate) -> PostCreate:
    new_post = {"title": post.title, "description": post.description}
    posts[max(posts.keys()) + 1] = new_post
    return new_post