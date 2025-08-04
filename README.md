# Screen-Sharing-in-Python
🖥️ Python Screen Sharing App
A lightweight and ready-to-use screen sharing application built using the vidstream Python library. This project allows real-time screen streaming from a client to a server over a network.

🔧 About
This project is built using the vidstream library, a pre-built Python module that simplifies screen sharing, video/audio streaming, and peer-to-peer communication. All logic is handled by the library, making this setup clean and beginner-friendly.

📦 Files
server.py: Starts a StreamingServer to receive and display shared screen from clients.

client.py: Launches a ScreenShareClient to capture and stream the screen to the server.

🚀 Usage
1. Install the Library
bash
Copy
Edit
pip install vidstream
2. Run the Server (Receiver)
bash
Copy
Edit
python server.py
The server will start listening for incoming streams on port 9999.

3. Run the Client (Sender)
Update the IP in client.py to the receiver’s IP address, then run:

bash
Copy
Edit
python client.py
Press Enter and type exit to stop the stream and terminate cleanly.

🌐 Example Network Setup
Component	IP Address	Role
Server	192.168.1.10	Receiver
Client	192.168.1.20	Sender

📚 Notes
Ensure both client and server are on the same network or use port forwarding/VPN.

Firewall must allow TCP traffic on port 9999.

Works best on LAN for low latency.

🛠 Built With
vidstream library – GitHub

Python 3.x

threading module

⚠️ Disclaimer
This project is for educational purposes only. Use responsibly and do not stream screens without permission.
