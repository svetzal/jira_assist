from typing import List

from augmentation.augmented_project import AugmentedProject
from augmentation.augmentor import Augmentor
from domain.persona import Persona
from domain.scenario import Scenario
from domain.software_being_implemented import SoftwareBeingImplemented
from jira.jira_project import JiraProject


class ProjectAugmentor(Augmentor):

    def augment(self, project: JiraProject, software: SoftwareBeingImplemented, personas: List[Persona]) -> AugmentedProject:
        messages = [
            {
                "role": "user",
                "content": f"""
                    This is a Jira project description:
                    {project.model_dump_json(indent=2)}
                    
                    This is the software being implemented:
                    {software.model_dump_json(indent=2)}
                    
                    These are the people using the software:
                    {[persona.model_dump_json() for persona in personas]}
                    
                    Assess and suggest improvements.
                """
            }
        ]
        response = self.llm.create_completion(messages, AugmentedProject)
        return response