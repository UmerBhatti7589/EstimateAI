from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectRequest
from app.services.analyzer import analyze_requirement

router = APIRouter()


@router.post("/project")
def create_project(project: ProjectRequest, db: Session = Depends(get_db)):

    analysis = analyze_requirement(project.description)

    db_project = Project(
        project_name=project.project_name,
        client_name=project.client_name,
        description=project.description,
        detected_features=", ".join(analysis["detected_features"]),
        estimated_timeline=analysis["estimated_timeline"],
        estimated_cost=analysis["estimated_cost"]
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return {
        "message": "Project saved successfully",
        "project_id": db_project.id,
        "analysis": analysis
    }
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    return projects
@router.get("/test")
def test():
    return {"message": "Router is working"}