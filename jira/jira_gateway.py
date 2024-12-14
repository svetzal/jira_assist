import os

import requests
from requests.auth import HTTPBasicAuth

from jira.transformers import simplified_issue_dict


class JiraGateway:
    def __init__(self, username, auth_token):
        self.auth = HTTPBasicAuth(username, auth_token)

    @property
    def headers(self):
        return {
            "Accept": "application/json"
        }

    @property
    def server(self):
        return "https://svetzal.atlassian.net"

    def get(self, path, params):
        return requests.request(
            "GET",
            f"{self.server}{path}",
            headers=self.headers,
            params=params,
            auth=self.auth
        ).json()

    def search_issues(self, query):
        return self.get("/rest/api/3/search", {'jql': query})

    def retrieve_project(self, project_key):
        return self.get(f"/rest/api/3/project/{project_key}", {})

    def update_project_description(self, key, description):
        return requests.request(
            "PUT",
            f"{self.server}/rest/api/3/project/{key}",
            headers=self.headers,
            json={"description": description},
            auth=self.auth
        ).json()
