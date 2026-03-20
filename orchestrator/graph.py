from langgraph.graph import StateGraph

from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.test_agent import test_agent


def research_node(state):
    issue = state["issue"]
    repo_code = state["repo_code"]

    research_result = research_agent(issue, repo_code)

    state["research_result"] = research_result
    return state


def coding_node(state):
    issue = state["issue"]
    research_result = state["research_result"]

    fix = coding_agent(issue, research_result)

    state["fix"] = fix
    return state


def test_node(state):
    fix = state["fix"]

    tests = test_agent(fix)

    state["tests"] = tests
    return state


def create_graph():

    builder = StateGraph(dict)

    builder.add_node("research", research_node)
    builder.add_node("coding", coding_node)
    builder.add_node("testing", test_node)

    builder.set_entry_point("research")

    builder.add_edge("research", "coding")
    builder.add_edge("coding", "testing")

    return builder.compile()