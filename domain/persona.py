from typing import List

from pydantic import BaseModel, Field


class Persona(BaseModel):
    role: str = Field(..., description="What role the persona plays in using the system.")
    concerns: List[str] = Field(..., description="The concerns that the persona has with which they expect the software to help.")
