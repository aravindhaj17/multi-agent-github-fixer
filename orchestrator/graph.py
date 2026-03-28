from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.test_agent import test_agent


def create_graph():

    def run(state: dict):

        # Step 1 — Research
        issue = state.get("issue")
        repo_code = state.get("repo_code")

        research_result = research_agent(issue, repo_code)
        state["research_result"] = research_result

        # Step 2 — Coding
        fix = coding_agent(issue, research_result)
        state["fix"] = fix

        # Step 3 — Testing
        tests = test_agent(fix)
        state["tests"] = tests

        return state

    return run