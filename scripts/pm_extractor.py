#! python
# numberandemail: Extracting all the phone numbers and email addresses from the text in clipboard
# p220
import re
import pyperclip as pc
import sys
# run command should be like project phone/mail
# phone num sample 977-984-505-6452
phone_reg = re.compile(
    r'(?:\d{1,4}|\(\d{1,4}\))?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})')
mail_reg = re.compile(r'[a-zA-Z09._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,4}')

text = str(pc.paste())

def phone_finder():
    phone_list=[]
    for grps in phone_reg.findall(text):
        formatted_num = '-'.join([grps[1], grps[3], grps[5]])
        phone_list.append(formatted_num)
    return phone_list

def mail_finder():
    mail_list =[]
    for grps in mail_reg.findall(text):
        mail_list.append(grps) #0th element in findall's return is the full match
    return mail_list

def correctform():
    print("there was an error. Please specify p or m (phone num or mail).")

def copier(match_list):
    if len(match_list)>0:
        pc.copy('\n'.join(match_list))
        return 1
    else:
        return 0
try:
    run_argument= sys.argv[1]
except:
    correctform()
    sys.exit("Argument pathaudai pathainas")
else:
    if sys.argv[1]=='m':
        y= copier(mail_finder())
    elif sys.argv[1]=='p':
       y= copier(phone_finder())
    else:
        correctform()
finally:
    if y==0:
        print("There was nothing to copy")
    
    


