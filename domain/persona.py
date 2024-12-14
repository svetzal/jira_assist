from typing import List

from pydantic import BaseModel, Field


class Persona(BaseModel):
    role: str = Field(..., description="What role the user plays.")
    concerns: List[str] = Field(..., description="The concerns of the user.")
    goals: List[str] = Field(..., description="The goals of the user.")
