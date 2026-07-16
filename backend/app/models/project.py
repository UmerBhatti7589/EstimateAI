from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_name = Column(String)

    client_name = Column(String)

    description = Column(String)

    detected_features = Column(String)

    estimated_timeline = Column(String)

    estimated_cost = Column(String)

    # Owner of Project
    user_id = Column(Integer, ForeignKey("users.id"))