from orchestrator.graph import create_graph

# create the workflow
app = create_graph()

issue = "Login fails when password contains special characters"

repo_code = """
def login(password):
    if password == "":
        return False
"""

result = app.invoke({
    "issue": issue,
    "repo_code": repo_code
})

print("\nResearch Result:\n")
print(result["research_result"])

print("\n---------------------------------\n")

print("Generated Fix:\n")
print(result["fix"])

print("\n---------------------------------\n")

print("Generated Tests:\n")
print(result["tests"])