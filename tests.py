# from subdirectory.filename import function_name
from functions.get_files_info import run_python_file


result = run_python_file("calculator", "main.py")
print(result)

result = run_python_file("calculator", "tests.py")
print(result)

result = run_python_file("calculator", "../main.py")
print(result)

result = run_python_file("calculator", "nonexistent.py")
print(result)
result = run_python_file("calculator", "prompts.py")
print(result)
result = run_python_file("calculator", "config.py")
print(result)
result = run_python_file("calculator", "config.py")
print(result)
result = run_python_file("calculator", "config.py")
print(result)
result = run_python_file("calculator", "config.py")
print(result)