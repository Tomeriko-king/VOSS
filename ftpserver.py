from ftplib import FTP

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from PIL import ImageGrab


def start_ftp_server():

    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()

    # Instantiate the authorizer (controls authentication)
    authorizer = DummyAuthorizer()

    # Add an anonymous user (no authentication required) or use a specific user
    # Format: authorizer.add_user(username, password, directory, perm)
    # perms: 'elradfmw' (read/write permissions)
    authorizer.add_user('user', 'password', 'C:\\ftp', perm='elradfmw')

    # Add anonymous user (optional) - uncomment the next line if needed
    # authorizer.add_anonymous('/path/to/ftp/folder', perm='elradfmw')

    # Instantiate the handler to handle FTP commands
    handler = FTPHandler
    handler.authorizer = authorizer

    # Instantiate the FTP server with a specified address and handler
    address = ('0.0.0.0', 21)  # '0.0.0.0' means all interfaces, port 21 is default FTP port
    print(f"")
    server = FTPServer(address, handler)

    # Start the server
    print("FTP server is running...")
    server.serve_forever()

    # Connect to the FTP server
    ftp = FTP(host='0.0.0.0')
    ftp.login('user', 'password')

    with open('screenshot.png', 'rb') as file:
        # Upload the file using storbinary (suitable for binary files like PNG)
        ftp.storbinary(f"STOR {'uploaded_image.png'}", file)