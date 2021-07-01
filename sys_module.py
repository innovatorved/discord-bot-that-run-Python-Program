import sys
# module use for direct input with file and exit with returncode

# print(sys.argv)

if len(sys.argv) == 1:
	print("Please pass the arguments")
	sys.exit(1) # if no argument passed so program end with returncode1

else:
	print(len(sys.argv))
	print(sys.argv)
	sys.exit(0)

# Run in Bash
# python sys_module.py 1 2 3 4 5 6
# python sys_module.py
# Output : ['sys_module.py', '1', '2', '3', '4', '5', '6']

# check return code in bash : echo$?