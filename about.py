from domain.persona import Persona
from domain.scenario import Scenario
from domain.software_being_implemented import SoftwareBeingImplemented

product_owner = Persona(
    role="Product Owner",
    concerns=[
        "That the software being developed satisfies the needs of its users, and is profitable for its sponsors.",
        "That the most important features of the software are prioritized and delivered first.",
        "That the team implementing the software is focused on the most important work, understands the purpose of the actions they're taking and how they relate to the purpose of the software."
    ]
)

team_member = Persona(
    role="Team Member",
    concerns=[
        "That the software being developed is of high quality.",
        "That the software being developed is maintainable.",
        "That the software being developed is testable."
    ]
)

software = SoftwareBeingImplemented(
    name="JiraAssist",
    purpose="""
        Assist a team in managing their Jira project in order to stay focused on building the best possible software for
        its users with the least amount of effort.
    """,
    audience=[product_owner]
)

po_can_check_jira_project_description = Scenario(
    persona=product_owner,
    software=software,
    context="""
        The team has been working on the Jira project for a few weeks, and the project description is out of date.
        The team is starting to lose focus on what they're trying to achieve, and the product owner is concerned that
        the team is starting to work on tasks that aren't aligned with the purpose of the software.
    """,
    action="""
        The product owner uses JiraAssist to check that the Jira project description accurately reflects the current
        purpose of the software development efforts.
    """,
    expectation="""
        The product owner sees the current project description, along with an assessment from JiraAssist that shows how
        well the project description aligns with its understanding of the purpose of the software.
    """
)
