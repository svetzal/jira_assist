from pydantic import BaseModel, Field

from domain.persona import Persona
from domain.software_being_implemented import SoftwareBeingImplemented


class Scenario(BaseModel):
    # Given [context], as a [persona], I want to [action] with [software] so that [expectation].
    persona: Persona = Field(..., description="The primary actor within the scenario.")
    software: SoftwareBeingImplemented = Field(..., description="The software that the actor is using.")
    context: str = Field(..., description="The context in which the scenario takes place.")
    action: str = Field(..., description="The action the actor takes.")
    expectation: str = Field(..., description="The expectation the actor has after taking the action.")
