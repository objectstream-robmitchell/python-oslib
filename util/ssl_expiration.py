import ssl
import socket
import datetime


__module__     = 'ssl_expiration.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.5.2'
__version__    = '2021.02.10.1605'


class SSLExpiration:
    def __init__(self, host: str):
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

    def expires(self):
        return self.expire_date

    def __str__(self):
        return f"{self.host} SSL certificate expires on {self.expire_date}"
