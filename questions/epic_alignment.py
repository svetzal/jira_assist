import os

from domain.goal_tools import extract_persona_goals, common_goals
from domain.objective import ListOfObjectives
from jira.jira_gateway import JiraGateway
from jira.jira_project import JiraProject
from jira.transformers import response_to_issues, simplified_project_dict
from llm.llm_gateway import OLlamaGateway, ChatGPTGateway

#
#
# Do my epics align with and reflect the goals of my project?
#
#

jira = JiraGateway("stacey@vetzal.com", os.environ['JIRA_API_KEY'])

# Choose the appropriate client
llm = ChatGPTGateway(api_key=os.environ["OPENAI_API_KEY"])
# llm = OLlamaGateway(model="llama3.1-instruct:8b-q6_k_l")
# llm = OLlamaGateway()

response = jira.retrieve_project('JA')
jira_project = JiraProject(**simplified_project_dict(response))

response = jira.search_issues('project = JA and status in ("To Do", "In Progress")')
issues = response_to_issues(response)

project_description = jira_project.model_dump_json(indent=2)
# project_description = "Some generic project description"
issues_json = [issue.model_dump_json(indent=2) for issue in issues]
# issues_json = "Some generic issues"

def print_goals(perspective: str, goals: ListOfObjectives):
    print(f"{perspective} goals:")
    for goal in goals.list:
        print(f"[{goal.persona_name}] {goal.objective}")

project_goals = extract_persona_goals(llm, "software project description", project_description)
print_goals("Project Description", project_goals)

issue_goals = extract_persona_goals(llm, "list of Jira issues", issues_json)
print_goals("Extracted from Issues", issue_goals)

common_goals = common_goals(llm, project_goals, issue_goals)
print_goals("Common Goals", common_goals)
