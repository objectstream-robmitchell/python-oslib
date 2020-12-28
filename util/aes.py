
'''
 Objectstream AES utility. 
 Wrapper class that handles padding.
'''

__module__     = 'os_aes.py'
__contact__    = 'Rob Mitchell'
__email__      = 'rob.mitchell@objectstream.com'
__version__    = '1.0.0'
__status__     = 'production'


import binascii
import struct
from Crypto.Cipher import AES


class OSAES(object):
  def __init__(self,key):
    if len(key) < 32:
      raise Exception('32 byte/256 bit key required')
    self.key = key[:32]
    self.iv = key[:16]


  def encrypt(self,plaintext):
    aes = AES.new(self.key,AES.MODE_CBC,self.key[:16])
    plaintext_size = len(plaintext)
    while( (len(plaintext)%16) != 0 ):
      plaintext = plaintext + '0'
    dif = binascii.b2a_hex(struct.pack('H',(len(plaintext)-plaintext_size)))
    ciphertext = aes.encrypt(plaintext)
    ciphertext = binascii.b2a_base64(ciphertext).rstrip()

    return ciphertext+dif


  def decrypt(self,ciphertext):
    aes = AES.new(self.key,AES.MODE_CBC,self.key[:16])
    (ciphertext,dif) = (ciphertext[:-4],ciphertext[-4:])
    dif = binascii.a2b_hex(dif)
    dif = struct.unpack('H',dif)[0]
    ciphertext = binascii.a2b_base64(ciphertext)
    plaintext = aes.decrypt(ciphertext)
    plaintext = plaintext[:len(plaintext)-dif]

    return plaintext

