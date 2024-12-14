import json

from jira.jira_issue import JiraIssue


def simplified_issue_dict(data: dict) -> dict:
    # if data['fields']['issuelinks']:
    #     print(json.dumps(data['fields']['issuelinks'], indent=2))
    description = data['fields']['description']
    if description is None:
        description = ''
    if type(description) is dict:
        description = description['content'][0]['content'][0]['text']
    return {
        'key': data['key'],
        'summary': data['fields']['summary'],
        'description': description
    }

def simplified_project_dict(data: dict) -> dict:
    return {
        'key': data['key'],
        'name': data['name'],
        'description': data['description']
    }

def response_to_issues(response):
    issues = []
    for issue_dict in response['issues']:
        dict = simplified_issue_dict(issue_dict)
        issue = JiraIssue(**dict)
        issues.append(issue)
    return issues

def graph_issues_from_response(graph, response):
    for issue_dict in response['issues']:
        simplified = simplified_issue_dict(issue_dict)
        graph.add_node(simplified['key'], **simplified)
    return graph

def graph_links_from_response(graph, response):
    for issue_dict in response['issues']:
        issue_key = issue_dict['key']
        if 'issuelinks' in issue_dict['fields']:
            for issue_link in issue_dict['fields']['issuelinks']:
                if 'inwardIssue' in issue_link:
                    source_key = issue_link['inwardIssue']['key']
                    target_key = issue_key
                    link_type = issue_link['type']['inward']
                if 'outwardIssue' in issue_link:
                    source_key = issue_key
                    target_key = issue_link['outwardIssue']['key']
                    link_type = issue_link['type']['outward']
                if source_key is not None and target_key is not None:
                    graph.add_edge(source_key, target_key, link_type=link_type)
    return graph