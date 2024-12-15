from about import product_owner, team_member
from domain.objective import ListOfObjectives
from llm.llm_message import llm_messages_adapter, LLMMessage

available_personas_message = LLMMessage(
    role="user",
    content=f"""
Available personas:
- {product_owner.model_dump_json()}
- {team_member.model_dump_json()}
""".strip()
)


def extract_persona_goals(llm, source, content):
    return llm.complete(
        llm_messages_adapter([
            available_personas_message,
            LLMMessage(role="user",
                       content=f"Extract the persona goals from this {source}: \"{content}\"")
        ]),
        ListOfObjectives
    )


def common_goals(llm, goals1: ListOfObjectives, goals2: ListOfObjectives):
    return llm.complete(
        llm_messages_adapter([
            available_personas_message,
            LLMMessage(role="user",
                       content=f"List the goals that are common between these two lists.\n\n"
                               f"First List: {goals1.model_dump_json()}\n\n"
                               f"Second List: {goals2.model_dump_json()}")
        ]),
        ListOfObjectives
    )


def missing_goals(llm, goals1: ListOfObjectives, goals2: ListOfObjectives):
    return llm.complete(
        llm_messages_adapter([
            available_personas_message,
            LLMMessage(role="user",
                       content=f"List the goals that are in the first list but not in the second list.\n\n"
                               f"First List: {goals1.model_dump_json()}\n\n"
                               f"Second List: {goals2.model_dump_json()}")
        ]),
        ListOfObjectives
    )
