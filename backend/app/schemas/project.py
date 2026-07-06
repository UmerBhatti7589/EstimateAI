from pydantic import BaseModel

class Project(BaseModel):
    project_name: str
    client_name: str
    description: str