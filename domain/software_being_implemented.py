from typing import List

from pydantic import BaseModel, Field

from domain.persona import Persona


class SoftwareBeingImplemented(BaseModel):
    name: str = Field(..., description="Name of the software being implemented.")
    purpose: str = Field(..., description="Purpose of the software being implemented.")
    audience: List[Persona] = Field(..., description="Who will use the software being implemented.")
