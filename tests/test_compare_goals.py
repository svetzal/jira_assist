import os

import pytest
from domain.goal_tools import common_goals, missing_goals
from domain.objective import ListOfObjectives, Objective
from llm.llm_gateway import OLlamaGateway, ChatGPTGateway

#
#
# A great example of how not to test a gen-ai system!
#
# This test uses an LLM to compare lists of personal goals. It does so through a prompt like this:
#             LLMMessage(role="user",
#                        content=f"List the goals that are in the first list but not in the second list.\n\n"
#                                f"First List: {goals1.model_dump_json()}\n\n"
#                                f"Second List: {goals2.model_dump_json()}")
#
# This requires the llm to do a bunch of correlation within its context in order to mimic logic (this but not that)
# and it will get "creative" every time, because it cannot logic. However it is useful because it can recognize similar
# meaning in differently phrased objectives.
#
# These pytests will fail nearly every time.
#
# What to do instead?
# Well, I'm not sure what path will yield me the best results right now, but the reason this whole project exists is
# to push my brain around building a semantic system around this objective alignment idea and exploring the boundaries
# of where an LLM can be useful, where I can explore simple vector similarity instead (like RAG would do in a chatbot),
# and any other techniques that strike me as I wander.
#
# "Not all who wander are lost." ∪ "Not until we are lost do we begin to understand ourselves."
#
#


@pytest.fixture(scope='session')
def llm():
    return OLlamaGateway()

@pytest.fixture
def list1():
    return ListOfObjectives(
        list=[
            Objective(objective="Increase user engagement", persona_name="Stacey"),
            Objective(objective="Increase user engagement", persona_name="Sharon"),
            Objective(objective="Improve user experience", persona_name="Stacey"),
        ]
    )

@pytest.fixture
def list2():
    return ListOfObjectives(
        list=[
            Objective(objective="Better engagement from users", persona_name="Stacey"),
        ]
    )

def test_common_goals(llm, list1, list2):
    result = common_goals(llm, list1, list2)
    assert isinstance(result, ListOfObjectives)
    assert len(result.list) == 1 # Should contain "Increase user engagement" due to similarity

def test_missing_goals_from_list2(llm, list1, list2):
    result = missing_goals(llm, list1, list2)
    assert isinstance(result, ListOfObjectives)
    assert len(result.list) == 2 # Should contain "Increase user engagement" (because Sharon doesn't share it in list2)
                                 # and "Improve user experience"

def test_missing_goals_from_list1(llm, list1, list2):
    result = missing_goals(llm, list2, list1)
    assert isinstance(result, ListOfObjectives)
    assert len(result.list) == 0 # Should contain no goals because list2 is a subset of list1
