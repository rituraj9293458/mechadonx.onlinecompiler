from initialstate import workflow, initial_state

result = workflow.invoke(initial_state)

print("\n========== FINAL RESULT ==========\n")

print("Final Code:")
print(result["code"])

print("\nErrors:")
print(result["errors"])

print("\nSuggestions:")
print(result["suggestions"])

print("\nTime Complexity:")
print(result["Timecomplexity"])

print("\nPossible Time Complexity:")
print(result["possibletime"])

print("\nIterations:")
print(result["itterations"])

print("\nCode Perfect:")
print(result["codeperfect"])