#! pytest /tmp/pytest_2.py -v
import subprocess
subprocess.call(["pytest", "pytest_2.py", "-v"])