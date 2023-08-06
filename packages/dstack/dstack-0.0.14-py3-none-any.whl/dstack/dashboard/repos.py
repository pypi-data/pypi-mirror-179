from typing import Optional, List

from fastapi import APIRouter
from pydantic import BaseModel

from dstack.backend import load_backend
from dstack.repo import RepoAddress

router = APIRouter(prefix="/api/repos", tags=["repos"])


class RepoItem(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str
    last_run_at: Optional[int]
    tags_count: int


class QueryReposRequest(BaseModel):
    repos: List[RepoItem]


class DeleteRepoRequest(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str


@router.get("/query", response_model=QueryReposRequest)
async def query() -> QueryReposRequest:
    backend = load_backend()
    repo_heads = backend.list_repo_heads()
    return QueryReposRequest(
        repos=[RepoItem(repo_host_name=r.repo_host_name,
                        repo_port=r.repo_port,
                        repo_user_name=r.repo_user_name,
                        repo_name=r.repo_name,
                        last_run_at=r.last_run_at,
                        tags_count=r.tags_count) for r in repo_heads])


@router.post("/delete")
async def delete(request: DeleteRepoRequest):
    backend = load_backend()
    backend.delete_repo(RepoAddress(request.repo_host_name, request.repo_port, request.repo_user_name,
                                    request.repo_name))
