from pydantic import BaseModel, Field


class JiraProject(BaseModel):
    key: str = Field(..., description="Key of the Jira project.")
    name: str = Field(..., description="Name of the Jira project.")
    description: str = Field(..., description="Description of the Jira project.")

    class Config:
        frozen = True
