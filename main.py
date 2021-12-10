# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to access operating system control
import os

# assigning the appropriate port value
PORT = 8010
# this finds the name of the computer user
os.environ['USERPROFILE']

path_to_folder = input("PLease insert the absolute path for the shared folder \n")

# changing the directory to access the files desktop
# with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), path_to_folder)
os.chdir(desktop)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()

# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)


# Creating the HTTP request and serving the
# folder in the PORT 8010,and the pyqrcode is generated

# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("The server is listening at port", PORT)
    print(f"Click on the following link {IP} in order to see the shared folder")
    httpd.serve_forever()
