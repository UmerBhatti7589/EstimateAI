from fastapi import APIRouter
from app.schemas.project import Project
from app.services.analyzer import analyze_requirement

router = APIRouter()


@router.post("/project")
def create_project(project: Project):

    analysis = analyze_requirement(project.description)

    return {
        "project_name": project.project_name,
        "client_name": project.client_name,
        "analysis": analysis
    }