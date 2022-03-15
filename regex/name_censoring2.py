import re

text = """
Doctor Sara Amity met agent Binod Rastogi on 12th March 1999. 
Agent smike smith and doctor amy wills along with agent Tom edwards were also in the secret meeting.
"""
title = 'Doctor'

ptrn = re.compile(f'{title} (\w)\w* (\w)\w*',re.IGNORECASE)

def replfunc(matchobj):
    grps = matchobj.groups()
    return f'{title} {grps[0].upper()}. {grps[1].upper()}.'

res = ptrn.sub(replfunc,text,count=0)
print(res)