'''
ex 11.6 Implement RSA algorithm, public and private keys are generated , given message is encrypted using public key
and the cipher is decrypted using the private key

'''
from random import randint
def is_prime(num):
  for factor in xrange(2,num/2 + 1):
    if num % factor == 0:
      return False 
  return True
#computes product of chosen primes and the totient
def compute_nphi():
  while True:
    p=randint(100,1000)
    q=randint(100,1000)
    t=(p-1) * (q-1)
    if is_prime(p) and is_prime(q) and p != q and t != 2 :
      return p*q,t 
#chooses e such that 1<e<totient ,e is a coprime of totient t
def choose_e(t):
  while True:
    e=randint(2,t)
    if is_prime(e) and t%e != 0 :
      return e  
#computes the multiplicative inverse of e mod t, which is the private key
def mod_mul_inv(e,t):  
    for i in range(1,t):
      if (i * e) % t == 1:
        return i

def encrypt(msg,pub):
  cipher = (msg ** pub[1]) % pub[0]
  return cipher
        
def decrypt(cipher,priv):
  msg = (cipher ** priv[1]) % priv[0]
  return msg

def repeat():
  while True:
    prod,phi_n=compute_nphi()
    e = choose_e(phi_n)
    print 'public key:',
    pub_key= prod,e 
    print pub_key
    priv_key =prod,mod_mul_inv(e,phi_n)
    print 'private key:',priv_key
    msg=int(raw_input('enter the message :'))
    cipher=encrypt(msg,pub_key)
    print 'the cipher text:',cipher
    print 'the original message:',decrypt(cipher,priv_key)
    choice=raw_input('Continue? y:yes / n:no :')
    if choice in ('n','no'):
      print 'Bye!'
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*50
  main()
  print '*'*50  
