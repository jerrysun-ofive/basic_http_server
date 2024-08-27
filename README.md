## Simple HTTP/1.0 Server

---

# 👾 About
Using this to learn the fundamentals of http server request and response. The project implements a simple HTTP/1.0 server in Python. The server listens for incoming HTTP requests and serves static files based on the request. It demonstrates basic networking concepts using Python's 'socket' library

---

# Function
- Handles HTTP/1.o GET requests.
- Serves static files from the server's directory
- Returns an 'index.html' file when the root URL is accessed.
- Sends a '404 Not Found' response if the requested file does not exist/

---

# Running the server
- The server listens on '0.0.0.0:8000'
- On web browser, go to 'http://localhost:8000'
- Access other (non-root) static file by entering 'http://localhost:8000/hello.html' into web brower

---

# Known Limitations
- This server only supports HTTP/1.0
- Only 'GET' requestrs are handled
- The server does not support MIME types or dynamic content.

---

# Resources and Ackowledgement
- [Main tutorial followed](https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842)
- [Python3 Socket Manual Page](https://docs.python.org/3/library/socket.html)
- [Python 'socket' library AF-INET](https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it)
- [Webserver Concept](https://youtu.be/9J1nJOivdyw?si=0zGxg84g6Te5vzPc)
