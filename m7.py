import random
import string

print('hello,welcome to password generator!')

length=int(input('\nEnter the length of the password:'))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower + upper +num +symbols

temp=random.sample(all,length)

password="".join(temp)

print(password)