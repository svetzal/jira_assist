import pytest
from domain.goal_tools import common_goals, missing_goals
from domain.objective import ListOfObjectives, Objective
from llm.llm_gateway import OLlamaGateway

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
    assert len(result.list) == 1

def test_missing_goals_from_list2(llm, list1, list2):
    result = missing_goals(llm, list1, list2)
    assert isinstance(result, ListOfObjectives)
    assert len(result.list) == 2

def test_missing_goals_from_list1(llm, list1, list2):
    result = missing_goals(llm, list2, list1)
    assert isinstance(result, ListOfObjectives)
    assert len(result.list) == 0
