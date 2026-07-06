from pydantic import BaseModel


class ProjectRequest(BaseModel):
    project_name: str
    client_name: str
    description: str