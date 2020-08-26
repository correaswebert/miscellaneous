# Chrome URL visited logger
# Note: Logging not done in real time as DB is locked when Chrome is open

import time
import sqlite3
import os


time.sleep(60)
now = int(time.time())

def dbHandler():
    # path to user's history database (Chrome)
    chrome_history_db = os.path.expanduser('~') + \
        r"\AppData\Local\Google\Chrome\User Data\Default\History"

    # querying the db
    c = sqlite3.connect(chrome_history_db)
    cursor = c.cursor()
    select_statement = f"""SELECT urls.url FROM urls 
                        WHERE urls.last_visit_time/1000000-11644473600 >= {now}"""
    cursor.execute(select_statement)
    results = cursor.fetchall()  # list of tuples of form -> (url,)

    return results


def formatter(urls):
    log = time.strftime('%d.%m.%Y') + '\n\n'
    for url in urls:
        log += '* ' + url[0] + '\n'
    log += '\n' + '=' * 80 + '\n'    
    return log


def logger(log, filename=None):
    # if log is empty, just header and footer in string
    if len(log) == 94:
        print('No Logs')
        return
    if filename is None:
        print(log)
    else:
        with open(filename, 'w') as f:
            f.write(log)
    print("Logged successfully!")


# checks if Chrome closed, every 10 mins., then logs history
while True:
    try:
        history = dbHandler()
        logs = formatter(history)
        logger(logs, 'ChromeLogs.txt')
        break
    except:
        # wait for 5 minutes
        for i in range(4):
            print(f"Logging in {5-i} minutes.")
            time.sleep(60)
        print("Logging in 1 minute.")
        time.sleep(50)
        for i in range(10):
            print(f"Logging in {10-i} seconds")
            time.sleep(1)
            os.system("cls")
        os.system("cls")

wait = input("Press ENTER to exit...")

