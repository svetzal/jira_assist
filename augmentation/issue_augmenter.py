from augmentation.augmentor import Augmentor
from augmented_issue import AugmentedIssue
from jira.jira_issue import JiraIssue
from llm.llm_gateway import LLMGateway

class IssueAugmentor(Augmentor):

    def augment(self, issue: JiraIssue) -> AugmentedIssue:
        issue_json = issue.model_dump_json(indent=2)
        messages = [
            {
                "role": "user",
                "content": f"Augment the following Jira issue:\n{issue_json}"
            }
        ]
        response = self.llm.create_completion(messages, AugmentedIssue)
        return response