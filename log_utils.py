from datetime import datetime

def write_log(username, action, details):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{time}] [{username}] {action}: {details}\n")
