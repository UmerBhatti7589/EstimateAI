from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectRequest, ProjectUpdate
from app.services.analyzer import analyze_requirement

router = APIRouter()


# Create Project
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


# Get All Projects
@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


# Search Projects
@router.get("/projects/search")
def search_projects(
    keyword: str = Query(...),
    db: Session = Depends(get_db)
):

    projects = db.query(Project).filter(
        (Project.project_name.ilike(f"%{keyword}%")) |
        (Project.client_name.ilike(f"%{keyword}%")) |
        (Project.description.ilike(f"%{keyword}%"))
    ).all()

    return projects


# Get Single Project
@router.get("/project/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


# Update Project
@router.put("/project/{project_id}")
def update_project(
    project_id: int,
    updated_project: ProjectUpdate,
    db: Session = Depends(get_db)
):

    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    analysis = analyze_requirement(updated_project.description)

    project.project_name = updated_project.project_name
    project.client_name = updated_project.client_name
    project.description = updated_project.description
    project.detected_features = ", ".join(analysis["detected_features"])
    project.estimated_timeline = analysis["estimated_timeline"]
    project.estimated_cost = analysis["estimated_cost"]

    db.commit()
    db.refresh(project)

    return {
        "message": "Project updated successfully",
        "project": project
    }


# Delete Project
@router.delete("/project/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }