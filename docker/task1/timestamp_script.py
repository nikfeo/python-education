from datetime import datetime
from time import sleep
import sys

while True:
    sys.stderr.write(f"{datetime.today()}\n")
    sleep(1)
