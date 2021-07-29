from wxpy import *
bot = Bot()
myself = bot.self
allname=[]
sendname=[]
no=[]
for i in bot.friends():
    allname.append(i.name)
for j in allname:
    if '1' in j:
        no.append(j)
    else:
        sendname.append(j.strip().split('(')[0])
print('no'*10)
print(no)
print('a'*10)
print(sendname)
for k in sendname:
    my_friend = bot.friends().search(str(k))[0]
    print(my_friend)
    my_friend.send(str(k) + '，中秋节快乐 😁')
