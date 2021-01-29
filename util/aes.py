
__module__     = 'aes.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.20.1314'


import os
import binascii
import struct
from Crypto.Cipher import AES


class AESUtil(object):
  '''
  AES wrapper class that handles padding.
  '''

  def __init__(self,key):
    '''
    :param key: 256bit/32byte AES key
    :type key:  str
    '''
    self.key = self.check_key(key)


  def check_key(self,key):
    '''
    Ensures given key is 32 characters

    :param key: 256bit/32byte AES key
    :type key:  str

    :returns:   sanitized key
    :rtype:     str

    :raises: custom exception
    '''
    try:
      if len(key) < 32:
        raise Exception('32 byte/256 bit key required')
      return key[:32]
    except:
      raise Exception('32 byte/256 bit key required')


  def encrypt(self,plaintext):
    '''
    Method to encrypt plaintext.

    :param plaintest:  data to be encrypted
    :type plaintext:   str

    :returns:  ciphertext
    :rtype:    str - base64 encrypted data
    '''
    if self.key == None:
      raise Exception('encrypt() with no key')
    iv = os.urandom(16)
    aes = AES.new(self.key,AES.MODE_CBC,iv)
    plaintext_size = len(plaintext)
    while( (len(plaintext)%16) != 0 ):
      plaintext = plaintext + b'0'
    dif = binascii.b2a_hex(struct.pack('H',(len(plaintext)-plaintext_size)))
    ciphertext = aes.encrypt(plaintext)
    return binascii.b2a_base64(dif+iv+ciphertext)


  def decrypt(self,ciphertext):
    '''
    Method to decrypt base64 ciphertext.

    :param ciphertext:  data to be decrypted
    :type ciphertext:   str - base64 encrypted data

    :returns:  decrypted plaintext
    :rtype:    str
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

