from pydantic import BaseModel, Field


class AugmentedProject(BaseModel):
    key: str = Field(..., description="Key of the Jira project.")
    name: str = Field(..., description="Name of the Jira project.")
    description: str = Field(..., description="Description of the Jira project.")

    assessment: str = Field(..., description="Assessment of how well the Jira project description matches the context provided.")
    suggestion: str = Field(..., description="Suggested improved project description based the current description and the context provided.")

    class Config:
        frozen = True