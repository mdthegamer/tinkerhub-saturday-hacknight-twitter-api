import schedule
import time
from bot import update



schedule.every(5).minutes.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)