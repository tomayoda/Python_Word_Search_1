#  A different approach.  Using cell number instead of row,col for locating word
#  if a hit is found at 113, just get key=113 to find the row,col
from DEF2_char_dict_V1_0 import *
print('-----------create 1 to 225----------------------')
j=0
k=[]
for i in range(225):
    j+=1
    k+=[j]
print('k list = ',k)
print('========end of creating 1 to 225================')
print('--------------------display H1------------------')
H1=h1_char_dict()
H1N={}
z=15
for key,val in H1.items():
    print(z,key,len(val),val)
    z+=15
print()
print('------------add numeric cell to H1N----------------')

m=0
for key,val in H1.items():
    for i in range(15):
        for j in range(15):
            if m>224: continue
            H1[i+1][j].extend([k[m]])
            m+=1
H1N=H1
print(len(H1N),H1N)
print('===================end of H1N==========================\n')
# print('--------------------display H2------------------')
H2=h2_char_dict()
H2N={}
z=15
for key,val in H2.items():
    print(z,key,len(val),val)
    z+=15
print()
print(len(H2),H2)
print('====================================================')
# print(H[1][2])
# if H[1][2] in H2[1][0]:
#     H2[1][0].extend([a[0]])
#     print(H2[1][0])
print('====================================================')
print('====[1]->row [2]->list element 1of15   [3] -> index 0-4 in list ===')
print('row 1,list 2, 2nd index 0thru4' )
print(H1N[1])
print('H1N[1][2][2]  ',H1N[1][5],'\t',H1N[1][5][2])
print('H1N1][3][2]  ',H1N[1][8],'\t',H1N[1][8][2])
print('H1N[1][14][2] ',H1N[14][14],'\t',H1N[14][14][2])
print('------------add numeric cell to H1N----------------')
# a=[98]
# print(H1N[1][3],H1N[1][4],H1N[1][5],H1N[1][6])
# print('\t\t',H1N[1][3][2],'\t\t\t',H1N[1][4][2],'\t\t\t',H1N[1][5][2],'\t\t\t',H1N[1][6][2])
# if "D1" in H1N[1][3]:
#     print("yes")
#     H1N[1][3].extend([88,99])
#     print(H1N[1][3])
#     print()
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')
for i in range(15):
    for j in range(15):
        print(H1N[1][0][2],H2[1][14][2])
        if H1N[1][0][2] in H2[1][14]:
            print('yes')
            H2[1][0].extend(H1N[1][1][2:])
            print(H2[1][0])
            break
        break