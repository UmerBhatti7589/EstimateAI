from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.database.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectRequest, ProjectUpdate
from app.services.analyzer import analyze_requirement
from app.services.security import get_current_user

router = APIRouter()


# Create Project
@router.post("/project")
def create_project(
    project: ProjectRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    analysis = analyze_requirement(project.description)

    db_project = Project(
        project_name=project.project_name,
        client_name=project.client_name,
        description=project.description,
        detected_features=", ".join(analysis["detected_features"]),
        estimated_timeline=analysis["estimated_timeline"],
        estimated_cost=analysis["estimated_cost"],
        user_id=current_user.id
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return {
        "message": "Project saved successfully",
        "project_id": db_project.id,
        "analysis": analysis
    }


# Get All Projects (Only Current User)
@router.get("/projects")
def get_projects(
    search: str = Query(None),
    client: str = Query(None),
    sort: str = Query("latest"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    query = db.query(Project).filter(
        Project.user_id == current_user.id
    )

    if search:
        query = query.filter(Project.project_name.contains(search))

    if client:
        query = query.filter(Project.client_name.contains(client))

    if sort == "oldest":
        query = query.order_by(asc(Project.id))
    else:
        query = query.order_by(desc(Project.id))

    projects = query.all()

    return {
        "total_projects": len(projects),
        "projects": projects
    }


# Get Single Project
@router.get("/project/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

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
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

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
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

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
    # Dashboard Statistics
@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    projects = db.query(Project).filter(
        Project.user_id == current_user.id
    ).all()

    total = len(projects)

    simple = len([
        project for project in projects
        if project.estimated_timeline == "1 Week"
    ])

    medium = len([
        project for project in projects
        if project.estimated_timeline == "2 Weeks"
    ])

    complex_projects = len([
        project for project in projects
        if project.estimated_timeline == "1 Month"
    ])

    return {
        "total_projects": total,
        "simple_projects": simple,
        "medium_projects": medium,
        "complex_projects": complex_projects
    }