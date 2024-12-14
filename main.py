import os

from about import software, product_owner
from augmentation.project_augmentor import ProjectAugmentor
from jira.jira_gateway import JiraGateway
from jira.jira_project import JiraProject
from jira.transformers import simplified_project_dict
from llm.llm_gateway import OLlamaGateway

jira = JiraGateway("stacey@vetzal.com", os.environ['JIRA_API_KEY'])

# Choose the appropriate client
# client = ChatGPTGateway(api_key=os.environ["OPENAI_API_KEY"])
llm = OLlamaGateway()
augmentor = ProjectAugmentor(llm)

response = jira.retrieve_project('DEMO')
jira_project = JiraProject(**simplified_project_dict(response))

print("Existing project description:")
print(jira_project.description)
print("")

augmented_project = augmentor.augment(jira_project, software, [product_owner])

print("Assessment:")
print(augmented_project.assessment)
print("")
print("Suggested project description:")
print(augmented_project.suggestion)

proceed = input("Would you like to update the project description? (y/n): ")
if proceed.lower() == 'y':
    jira.update_project_description(jira_project.key, description=augmented_project.suggestion)
    print("Project description updated.")
