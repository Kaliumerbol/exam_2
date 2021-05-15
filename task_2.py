text = "Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."

kol_s = 0
kol_t = 0
text_s = text.split()
for words in text_s:
    for i in words:
        if i.lower() == 's':
            kol_s += 1
        if i.lower() == 't':
            kol_t += 1
print(kol_s)
print(kol_t)

text_s = text.split()
for word in text_s:
    if 'advert' in word.lower():
        print(word.upper())



# f = open('air.txt', 'r')
# simv = (".,?!")
# new_list = []
# for line in f:
#     # print(line)
#     sf = line.split()
# for word in sf:
#     # print(word)
#     for i in word:
#         if i not in simv:
#             new_list.append(i.lower())
# # list_i = set(new_list)
# # # print(list_i) 
# u = {ju: ju.get for ju in new_list}
# print(u)
# # for j in list_i.lower()

# f = open('air.txt', 'r')
# text = f.read()
# a = text.split()
# b = ''.join(a).lower().replace(' ', '').replace
# print(b)