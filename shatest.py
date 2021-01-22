from hashlib import sha256


print(sha256('testinghash'.encode('ascii')).hexdigest())
#this is 64 bit in terms of hexidecimal
