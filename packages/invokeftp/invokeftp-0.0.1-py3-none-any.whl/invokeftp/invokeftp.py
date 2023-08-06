import ftplib
from ftplib import error_perm
import ipaddress
import os


# Function that evaluates whether a str is a valid IP or not
def valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


class InvokeFTP:
    # Instantiating an FTP_TLS() object from ftplib.
    def __init__(self):
        self.ftp = ftplib.FTP_TLS()

    # Closes our ftp stream
    def close(self):
        self.ftp.quit()

    # Creates a connection taking the host (in IP form), the FTP username, the FTP pass, and an optional argument for
    # the port
    def connect(self, host, username, password, port=21):

        ##  Begin Arg Checking  ##
        if not (valid_ip(host) == True):
            raise ValueError("Host was not a valid IP address.")
        if not isinstance(host, str):
            raise TypeError("Host was not equal to str type.")
        if not isinstance(port, int):
            raise TypeError("Port was not equal to type int.")
        if not isinstance(username, str):
            raise TypeError("Username was not equal to type str.")
        if not isinstance(password, str):
            raise TypeError("Password was not equal to type str.")
        ##   End Arg Checking   ##

        # Connect and login, call prot_p() to use TLS
        self.ftp.connect(host, port)
        self.ftp.login(username, password)
        self.ftp.prot_p()

    # This creates a session for uploading or downloading based on the argument 'mode'
    def create(self, local_path, remote_path, mode):

        ##   Input Checking   ##
        if not isinstance(local_path, str):
            raise TypeError("Local path was not equal to str type.")
        if not isinstance(remote_path, str):
            raise TypeError("Remote path was not equal to str type.")
        if not isinstance(mode, str):
            raise TypeError("Mode was not equal to str type.")
        if len(mode) > 1:
            raise ValueError("Mode was greater than one character. Use 'u' for uploading, and 'd' for downloading.")
        ## End of Input Checking ##

        if mode == 'u' or mode == 'U':
            if not os.path.exists(local_path):
                raise FileNotFoundError("The local file does not exist or an incorrect path was specified.")

            # Open a file for reading
            with open(local_path, 'rb') as f:
                # Upload the file to the server
                try:
                    self.ftp.storbinary('STOR ' + remote_path, f)
                except error_perm:
                    raise PermissionError("There was a permission error when creating the file/directory.")
            f.close()
        elif mode == 'd' or mode == 'D':
            # Open a file for writing
            try:
                with open(local_path, 'wb') as f:
                    # Download the file from the server
                    self.ftp.retrbinary('RETR ' + remote_path, f.write)
            except Exception as e:
                print(e)
            f.close()
