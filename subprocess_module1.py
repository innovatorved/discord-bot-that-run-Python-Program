import subprocess
import sys

# we use subprocess and sys module to run python programs
python_code = """
print("Program working Succesfully")
"""
result = subprocess.run(
    [sys.executable, "-c", python_code ], capture_output=True, text=True
)
print("stdout:", result.stdout)	# command Output
print("stderr:", result.stderr)	# Error if occurs
