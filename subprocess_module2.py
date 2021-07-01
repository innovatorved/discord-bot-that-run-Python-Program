import subprocess

# we use subprocess module to run cmd commands

python_code = """
print("Program working Succesfully")
"""

# code is a list contain command each world seperated with ,
code = ["python3" , "-c" , """print("working subprocess_module.py")"""]
result = subprocess.run(
    code, capture_output=True, text=True
)
print("stdout:", result.stdout)	# command Output
print("stderr:", result.stderr)	# Error if occurs
