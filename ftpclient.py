from ftplib import FTP
from PIL import ImageGrab


def send_png_via_ftp(ftp_host, ftp_user, ftp_password, image_path, remote_path, local_image):

    print("starting ftp")
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()

    # Connect to the FTP server
    ftp = FTP(host=ftp_host)
    ftp.login(ftp_user, ftp_password)

    with open(local_image, 'wb') as local_file:
        # Use RETR to retrieve the file and store it locally
        ftp.retrbinary(f"RETR {remote_path}", local_file.write)

    # Close the FTP connection
    ftp.quit()
    print(f"PNG image '{image_path}' uploaded to {remote_path} successfully!")


def clientdt():
    # FTP server details
    ftp_host = '127.0.0.1'  # Replace with the FTP server address
    ftp_user = 'user'  # Replace with the FTP username
    ftp_password = 'password'  # Replace with the FTP password

    # PNG image file details
    image_path = 'screenshot.png'  # Replace with the local PNG image file path
    remote_path = 'uploaded_image.png'  # The desired name/path on the FTP server

    local_image = 'download.png'

    send_png_via_ftp(ftp_host, ftp_user, ftp_password, image_path, remote_path, local_image)