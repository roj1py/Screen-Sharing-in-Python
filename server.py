from vidstream import StreamingServer
import threading

recive = StreamingServer("0.0.0.0", 9999)
thread = threading.Thread(target=recive.start_server)
thread.start()

while input('') != "exit":
    continue

recive.stop_server()