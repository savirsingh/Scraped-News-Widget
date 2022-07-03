import ping, socket
try:
    ping.verbose_ping('scrapednews.pythonanywhere.com', count=3)
    delay = ping.Ping('scrapednews.pythonanywhere.com', timeout=2000).do()
except socket.error(e):
    print ("Ping Error:", e)
