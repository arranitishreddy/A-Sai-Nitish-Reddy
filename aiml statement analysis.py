#!/usr/bin/env python
# coding: utf-8

# In[4]:


s1="I am a human being"
s2="I am good"
s3="Good graders study well"
s4="Humans love graders"
s5="Every human does not study well"
opp_s5="Every human study well"#here neg_E is the negation of E


reminder=0
result=0


truth_values=[[1,1],[1,0],[0,0],[0,1]]


for value in truth_values:
    if value[0]==1:
        s3="T"
    else: 
        s3="F"
    if value[1]==1:
        s5="T"
    else:
        s5="F"
    if s5=="T":
        opp_s5="F"
    else:
        opp_s5="T"

    for i in (s3 and s5):
        if i=="T":
            reminder+=1

            
if reminder==len(truth_values):
    result="YES"
else:
    result="NO"
print("Is every human is a good grader? :   ",result)


# In[ ]:




