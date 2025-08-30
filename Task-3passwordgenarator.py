import random
import string
print("==="*20)
print("Welcome to password genarator 🔑 ")
print("==="*20)
digits_len=int(input("enter how many digits to be involved in genarated password:"))
letter_len=int(input("enter how many letters  to be involved in genarated password:"))
pun_len=int(input("enter how many punctuations  to be involved in genarated password:"))
letters=string.ascii_letters
digits=string.digits
punctuations=string.punctuation
password=""
dig_pss=""
letter_pass=""
pun_pass=""
for _ in range(digits_len):
    dig_pss+=random.choice(digits)
for _ in range (letter_len):
    letter_pass+=random.choice(letters)
for _ in range(pun_len):
    pun_pass+=random.choice(punctuations)
password=dig_pss+letter_pass+pun_pass
#password=''.join(random.sample(password,len(password)))
password=list(password)
random.shuffle(password)
password=''.join(password)
print("Genarated password as per your reqiuremet is:",password)
