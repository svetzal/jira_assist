from typing import List

from pydantic import BaseModel, Field


class Objective(BaseModel):
    objective: str = Field(..., title="A statement of objective, suitable for a bullet point.")
    persona_name: str = Field(..., title="The persona who has the stated objective.")


class ListOfObjectives(BaseModel):
    list: List[Objective] = Field(..., title="List of objectives.")
