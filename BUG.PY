import ast

# Simple function to check for basic errors in code
def static_bug_detector(code):
    try:
        # Parse code to check for syntax errors
        parsed_code = ast.parse(code)
        print("Syntax looks good!")
        
        # Traverse AST to look for unused variables
        for node in ast.walk(parsed_code):
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                variable_name = node.targets[0].id
                print(f"Warning: Check if '{variable_name}' is used after assignment.")
        
    except SyntaxError as e:
        print(f"Syntax Error detected: {e}")

# Sample code to check
code_to_check = """
x = 10
y = 20
z = x + y
"""

static_bug_detector(code_to_check)
