from initialstate import workflow, initial_state

print("Starting Code Analysis & Optimization Workflow...\n")
result = workflow.invoke(initial_state)

print("=" * 60)
print("                   FINAL EXECUTION RESULT                   ")
print("=" * 60)

print(f"\n[ Status ]")
print(f"  • Code Perfect     : {result['codeperfect']}")
print(f"  • Total Iterations : {result['itterations']}")

print(f"\n[ Time Complexity Analysis ]")
print(f"  • Current Complexity  : {result['Timecomplexity']}")
print(f"  • Optimal Complexity  : {result['possibletime']}")

print(f"\n[ Errors Found ]")
if result['errors']:
    for idx, err in enumerate(result['errors'], 1):
        print(f"  {idx}. {err}")
else:
    print("  • No errors found.")

print(f"\n[ Suggestions ]")
if result['suggestions']:
    for idx, sug in enumerate(result['suggestions'], 1):
        print(f"  {idx}. {sug}")
else:
    print("  • No additional suggestions.")

print(f"\n[ Final Corrected Code ]")
print("-" * 60)
print(result["code"])
print("-" * 60)