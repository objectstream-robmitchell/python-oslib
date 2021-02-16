
__module__     = 'mysql_interface.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__updated__    = '2021.02.16.1457'


import MySQLdb


class MySQLIface:
    def __init__(self,creds):
        self.con = MySQLdb.connect(host=creds['hostname'],user=creds['username'],
                                   passwd=creds['password'],db=creds['database'])

    def fetchall(self,sql):
        result = []
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            result.append(row)
        cur.close()
        return result

    def fetchone(self,sql):
      cur = self.con.cursor()
      cur.execute(sql)
      result = cur.fetchone()
      cur.close()
      return result

    def execute(self,sql):
      cur = self.con.cursor()
      cur.execute(sql)
      self.con.commit()
      cur.close()

    def close(self):
      self.con.close()

