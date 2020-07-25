# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main
import replit
replit.clear() # clear output in console

print(1, add_time("11:59 PM", "24:05"))

# Run unit tests automatically
main(module='test_module', exit=False)