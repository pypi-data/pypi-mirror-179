from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from dstack.backend import load_backend
from dstack.repo import RepoAddress

router = APIRouter(prefix="/api/tags", tags=["tags"])


class ArtifactHeadItem(BaseModel):
    job_id: str
    artifact_path: str


class TagHeadItem(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str
    tag_name: str
    run_name: str
    workflow_name: Optional[str]
    provider_name: Optional[str]
    created_at: int
    artifacts: Optional[List[ArtifactHeadItem]]


class TagItem(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str
    repo_branch: str
    repo_hash: str
    repo_diff: str
    tag_name: str
    run_name: str
    workflow_name: Optional[str]
    provider_name: Optional[str]
    created_at: int
    artifacts: Optional[List[ArtifactHeadItem]]


class QueryTagsResponse(BaseModel):
    tags: List[TagHeadItem]


class DeleteTagRequest(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str
    tag_name: str


class AddTagRequest(BaseModel):
    repo_host_name: str
    repo_port: Optional[int]
    repo_user_name: str
    repo_name: str
    run_name: str
    tag_name: str


class GetTagResponse(BaseModel):
    tag: TagItem


@router.get("/query", response_model=QueryTagsResponse)
async def query(repo_host_name: str, repo_port: Optional[int], repo_user_name: str,
                repo_name: str) -> QueryTagsResponse:
    backend = load_backend()
    repo_address = RepoAddress(repo_host_name, repo_port, repo_user_name, repo_name)
    tag_heads = backend.list_tag_heads(repo_address)
    return QueryTagsResponse(
        tags=[TagHeadItem(repo_host_name=t.repo_address.repo_host_name,
                          repo_port=t.repo_address.repo_port,
                          repo_user_name=t.repo_address.repo_user_name,
                          repo_name=t.repo_address.repo_name,
                          tag_name=t.tag_name,
                          run_name=t.run_name,
                          workflow_name=t.workflow_name,
                          provider_name=t.provider_name,
                          created_at=t.created_at,
                          artifacts=[
                              ArtifactHeadItem(job_id=a.job_id, artifact_path=a.artifact_path)
                              for a in t.artifact_heads
                          ] if t.artifact_heads else None) for t in tag_heads])


@router.get("/get", response_model=GetTagResponse)
async def query(repo_host_name: str, repo_port: Optional[int], repo_user_name: str, repo_name: str,
                tag_name: str) -> GetTagResponse:
    backend = load_backend()
    repo_address = RepoAddress(repo_host_name, repo_port, repo_user_name, repo_name)
    t = backend.get_tag_head(repo_address, tag_name)
    if t:
        j = backend.list_jobs(repo_address, t.run_name)[0]
        return GetTagResponse(
            tag=TagItem(repo_host_name = t.repo_address.repo_host_name,
                        repo_port = t.repo_address.repo_port,
                        repo_user_name=t.repo_address.repo_user_name,
                        repo_name=t.repo_address.repo_name,
                        repo_branch=j.repo_data.repo_branch,
                        repo_hash=j.repo_data.repo_hash,
                        repo_diff=j.repo_data.repo_diff,
                        tag_name=t.tag_name,
                        run_name=t.run_name,
                        workflow_name=t.workflow_name,
                        provider_name=t.provider_name,
                        created_at=t.created_at,
                        artifacts=[
                            ArtifactHeadItem(job_id=a.job_id, artifact_path=a.artifact_path)
                            for a in t.artifact_heads
                        ] if t.artifact_heads else None))
    else:
        raise HTTPException(status_code=404, detail="Tag not found")


@router.post("/delete")
async def delete(request: DeleteTagRequest):
    backend = load_backend()
    repo_address = RepoAddress(request.repo_host_name, request.repo_port, request.repo_user_name, request.repo_name)
    tag_head = backend.get_tag_head(repo_address, request.tag_name)
    if tag_head:
        backend.delete_tag_head(repo_address, tag_head)
    else:
        raise HTTPException(status_code=404, detail="Tag not found")


@router.post("/add")
async def delete(request: AddTagRequest):
    backend = load_backend()
    repo_address = RepoAddress(request.repo_host_name, request.repo_port, request.repo_user_name, request.repo_name)
    backend.add_tag_from_run(repo_address, request.tag_name, request.run_name, run_jobs=None)
