def log_message(msg):
    with open("log/data.log","a") as logfile:
     logfile.write("{0}\n".format(msg))
    