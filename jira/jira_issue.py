from typing import Optional

from pydantic import BaseModel, Field


class JiraIssue(BaseModel):
    key: str = Field(..., description="Key of the Jira issue.")
    summary: str = Field(..., description="Summary of the Jira issue.")
    description: Optional[str] = Field(..., description="Description of the Jira issue.")

    class Config:
        frozen = True
