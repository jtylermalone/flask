from datetime import datetime

def log_msg(msg):
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = open("log.txt", "a")
    file.write(dt + "    " + msg + "\n")
    file.close()
