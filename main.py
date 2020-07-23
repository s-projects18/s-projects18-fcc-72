# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main
import replit
replit.clear() # clear output in console

#print(add_time("11:06 PM", "2:02"))
print(1, add_time("3:30 PM", "2:12")) # "5:42 PM"

# Run unit tests automatically
main(module='test_module', exit=False)