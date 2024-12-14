from typing import Optional

from pydantic import BaseModel, Field


class AugmentedIssue(BaseModel):
    key: str = Field(..., description="Key of the Jira issue.")
    summary: str = Field(..., description="Summary of the Jira issue.")
    description: Optional[str] = Field(..., description="Description of the Jira issue.")

    form: str = Field(..., description="Whether the issue represents a user story or a task to perform.")

    subject: str = Field(..., description="The person about whom the issue is written.")
    action: str = Field(..., description="The action the person takes that the story describes.")
    goal: str = Field(..., description="The goal that the story helps the person achieve.")

    class Config:
        frozen = True