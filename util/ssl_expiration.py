import ssl
import socket
import datetime


class SSLExpiration:
    def __init__(self, host):
        self.host = host
        self.expire_dt = self._get_expiration()
        self.expire_date = str(self.expire_dt).split()[0]

    def _get_expiration(self):
        context = ssl.create_default_context()
        con = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.host)
        con.settimeout(10.0)
        con.connect((self.host, 443))
        info = con.getpeercert()
        return datetime.datetime.strptime(info['notAfter'], '%b %d %H:%M:%S %Y %Z')

    def __str__(self):
        return f"{self.host} SSL certificate expires on {self.expire_date}"
