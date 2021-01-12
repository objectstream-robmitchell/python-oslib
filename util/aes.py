
__module__      = 'aesutil.py'
__maintainer__  = 'rob.mitchell@objectstream.com'
__version__     = '0.4.0'
__status__      = 'development'

import os
import binascii
import struct
from Crypto.Cipher import AES

class AESUtil(object):
  '''
  AES wrapper class that handles padding.

  Args:
   key (str) 256bit/32byte AES key. 
  '''

  def __init__(self,key):
    self.key = self.check_key(key)


  def check_key(self,key):
    try:
      if len(key) < 32:
        raise Exception('32 byte/256 bit key required')
      return key[:32]
    except:
      raise Exception('32 byte/256 bit key required')


  def encrypt(self,plaintext):
    '''
    Method to encrypt plaintext.

    Args:
      plaintext (str) data to be encrypted.

    Returns:
      ciphertext (str) base64 AES encrypted data.
    '''

    if self.key == None:
      raise Exception('encrypt() with no key')
    iv = os.urandom(16)
    aes = AES.new(self.key,AES.MODE_CBC,iv)
    plaintext_size = len(plaintext)
    while( (len(plaintext)%16) != 0 ):
      plaintext = plaintext + '0'
    dif = binascii.b2a_hex(struct.pack('H',(len(plaintext)-plaintext_size)))
    ciphertext = aes.encrypt(plaintext)
    return binascii.b2a_base64(dif+iv+ciphertext)


  def decrypt(self,ciphertext):
    '''
    Method to decrypt plaintext.

    Args:
      ciphertext (str) base64 AES encrypted data.

    Returns:
      plaintext (str) decrypted plaintext.
    '''

    if self.key == None:
      raise Exception('decrypt() with no key')
    ciphertext = binascii.a2b_base64(ciphertext)
    (dif,iv,ciphertext) = (ciphertext[:4],ciphertext[4:20],ciphertext[20:]) 
    aes = AES.new(self.key,AES.MODE_CBC,iv)
    dif = binascii.a2b_hex(dif)
    dif = struct.unpack('H',dif)[0]
    plaintext = aes.decrypt(ciphertext)
    plaintext = plaintext[:len(plaintext)-dif]
    return plaintext

