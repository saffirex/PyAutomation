#! python3
# multiclip.py: Multiple clipboard
text = {'agree': 'I agree. That sounds fine to me. Please keep me updated.'
        , 'busy': 'I am a little bit busy right now. I\'ll get back to you in a few hours.',
        'reject': 'I don\'t think I\'ll be able to work on this. Sorry, I\'m turning this down' 
        }

import sys, time
import pyperclip as pc

def correctform():
    print('Please enter an argument:\n Usage: python multiclip.py <agree/busy/reject>')
    print("==============================")
    print('\n')
if len(sys.argv) <2:
    correctform()
    sys.exit

if sys.argv[1] in text:
    pc.copy(text[sys.argv[1]])
    print("Text for "+ sys.argv[1]+ " has been copied")
else:
    print("Err: "+ sys.argv[1]+ "couldn't be found")
    correctform()
    
time.sleep(8)