from vidstream import ScreenShareClient
import threading
send = ScreenShareClient("41.100.82.200", 9999)
thread = threading.Thread(target=send.start_stream)
thread.start()

while input('') != "exit":
    continue

send.stop_stream()