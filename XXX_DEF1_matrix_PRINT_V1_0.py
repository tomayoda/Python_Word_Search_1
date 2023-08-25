# Create base Strings matrix and 8 sub-string matrix
# Manually enter the strings and words into a text file
# Create H1_ and reverse to create H2_
# Use H1 to create V1 and reverse to create V2
# Use H1 to create S1 S2 BS1 BS2

def h1_h2(m1):
    # print('\nReverse the letters in each word: h1-h2,v1-v2')
    m2 = []
    for row in m1:
        row = row[::-1]
        m2 += [row]
    return m2


# Transpose  H1 horizontal reversed into V1 vertical rows
def h1_v1(m1):
    # print('\nTranspose h1 to v1')
    vstring = []
    vrow01 = []
    vrow02 = []
    vrow03 = []
    vrow04 = []
    vrow05 = []
    vrow06 = []
    vrow07 = []
    vrow08 = []
    vrow09 = []
    vrow10 = []
    vrow11 = []
    vrow12 = []
    vrow13 = []
    vrow14 = []
    vrow15 = []
    for row in m1:  # this is H1 data in MATRIX
        vrow01 += row[14]  # 15 char accumulated in 15 lists, for 15 lines. 0-14.
        vrow02 += row[13]
        vrow03 += row[12]
        vrow04 += row[11]
        vrow05 += row[10]
        vrow06 += row[9]
        vrow07 += row[8]
        vrow08 += row[7]
        vrow09 += row[6]
        vrow10 += row[5]
        vrow11 += row[4]
        vrow12 += row[3]
        vrow13 += row[2]
        vrow14 += row[1]
        vrow15 += row[0]
    vs01 = ''.join(vrow01)
    vs02 = ''.join(vrow02)
    vs03 = ''.join(vrow03)
    vs04 = ''.join(vrow04)
    vs05 = ''.join(vrow05)
    vs06 = ''.join(vrow06)
    vs07 = ''.join(vrow07)
    vs08 = ''.join(vrow08)
    vs09 = ''.join(vrow09)
    vs10 = ''.join(vrow10)
    vs11 = ''.join(vrow11)
    vs12 = ''.join(vrow12)
    vs13 = ''.join(vrow13)
    vs14 = ''.join(vrow14)
    vs15 = ''.join(vrow15)
    vstrings = [vs15] + [vs14] + [vs13] + [vs12] + [vs11] + [vs10] + [vs09] + [vs08] + [vs07] + [vs06] + [vs05] + [
        vs04] + [vs03] + [vs02] + [vs01]
    for line in vstrings:
        v1strings = vstring[::-1]
    return vstrings


# ('Transpose  v1  reversed into v2 rows')
def v1_v2(m1):
    # print('\nReverse the letters in each word: v1-v2')
    m2 = []
    for row in m1:
        row = row[::-1]
        m2 += [row]
    return m2


def s1_s2(MATRIX):  # m1 is MATRIX
    # print('\n s1 -> s2 ')
    line01 = MATRIX[0]
    line02 = MATRIX[1]
    line03 = MATRIX[2]
    line04 = MATRIX[3]
    line05 = MATRIX[4]
    line06 = MATRIX[5]
    line07 = MATRIX[6]
    line08 = MATRIX[7]
    line09 = MATRIX[8]
    line10 = MATRIX[9]
    line11 = MATRIX[10]
    line12 = MATRIX[11]
    line13 = MATRIX[12]
    line14 = MATRIX[13]
    line15 = MATRIX[14]

    i = 1
    s1line01 = line01[i - 1]
    s2line01 = s1line01[::-1]
    i = 2
    s1line02 = line01[i - 1] + line02[i - 2]
    s2line02 = s1line02[::-1]
    i = 3
    s1line03 = line01[i - 1] + line02[i - 2] + line03[i - 3]
    s2line03 = s1line03[::-1]
    i = 4
    s1line04 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4]
    s2line04 = s1line04[::-1]
    i = 5
    s1line05 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5]
    s2line05 = s1line05[::-1]
    i = 6
    s1line06 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6]
    s2line06 = s1line06[::-1]
    i = 7
    s1line07 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7]
    s2line07 = s1line07[::-1]
    i = 8
    s1line08 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8]
    s2line08 = s1line08[::-1]
    i = 9
    s1line09 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9]
    s2line09 = s1line09[::-1]
    i = 10
    s1line10 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10]
    s2line10 = s1line10[::-1]
    i = 11
    s1line11 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10] \
               + line11[i - 11]
    s2line11 = s1line11[::-1]
    i = 12
    s1line12 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10] \
               + line11[i - 11] + line12[i - 12]
    s2line12 = s1line12[::-1]
    i = 13
    s1line13 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10] \
               + line11[i - 11] + line12[i - 12] + line13[i - 13]
    s2line13 = s1line13[::-1]
    i = 14
    s1line14 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10] \
               + line11[i - 11] + line12[i - 12] + line13[i - 13] + line14[i - 14]
    s2line14 = s1line14[::-1]
    i = 15
    s1line15 = line01[i - 1] + line02[i - 2] + line03[i - 3] + line04[i - 4] + line05[i - 5] \
               + line06[i - 6] + line07[i - 7] + line08[i - 8] + line09[i - 9] + line10[i - 10] \
               + line11[i - 11] + line12[i - 12] + line13[i - 13] + line14[i - 14] + line15[i - 15]
    s2line15 = s1line15[::-1]
    print('\tS1 MATRIX','\t'*9,'S2 MATRIX')
    j = 5
    k = 15
    i = 0
    i += 1
    print(i,'\t',s1line01,' '*(k),'\t'*j,i,'\t\t',s2line01)
    i+=1;k-=1
    print(i,'\t',s1line02,' '*(k),'\t'*j,i,'\t\t',s2line02)
    i+=1;k-=1
    print(i,'\t',s1line03,' '*(k),'\t'*j,i,'\t\t',s2line03)
    i+=1;k-=1
    print(i,'\t',s1line04,' '*(k),'\t'*j,i,'\t\t',s2line04)
    i+=1;k-=1
    print(i,'\t',s1line05,' '*(k),'\t'*j,i,'\t\t',s2line05)
    i+=1;k-=1
    print(i,'\t',s1line06,' '*(k),'\t'*j,i,'\t\t',s2line06)
    i+=1;k-=1
    print(i,'\t',s1line07,' '*(k),'\t'*j,i,'\t\t',s2line07)
    i+=1;k-=1
    print(i,'\t',s1line08,' '*(k),'\t'*j,i,'\t\t',s2line08)
    i+=1;k-=1
    print(i,'\t',s1line09,' '*(k),'\t'*j,i,'\t\t',s2line09)
    i+=1;k-=1
    print(i,'\t',s1line10,' '*(k),'\t'*j,i,'\t',s2line10)
    i+=1;k-=1
    print(i,'\t',s1line11,' '*(k),'\t'*j,i,'\t',s2line11)
    i+=1;k-=1
    print(i,'\t',s1line12,' '*(k),'\t'*j,i,'\t',s2line12)
    i+=1;k-=1
    print(i,'\t',s1line13,' '*(k),'\t'*j,i,'\t',s2line13)
    i+=1;k-=1
    print(i,'\t',s1line14,' '*(k),'\t'*j,i,'\t',s2line14)
    i+=1;k-=1
    print(i,'\t',s1line15,' '*(k),'\t'*j,i,'\t',s2line15)
    i = 0

    s1_1_15 = [s1line01] + [s1line02] + [s1line03] + [s1line04] + [s1line05] + [s1line06] + [s1line07] + [s1line08] + [
        s1line09] + [s1line10] + [s1line11] + [s1line12] + [s1line13] + [s1line14] + [s1line15]
    s2_1_15 = [s2line01] + [s2line02] + [s2line03] + [s2line04] + [s2line05] + [s2line06] + [s2line07] + [s2line08] + [
        s2line09] + [s2line10] + [s2line11] + [s2line12] + [s2line13] + [s2line14] + [s2line15]
    # print('---------------s1_1_15---s2_1_15------------')
    print(s1_1_15)
    print(s2_1_15)
    # -----------------------------------------------------------
    # print('\n s1 -> s2 ')
    # empty0 = MATRIX[0]
    line16 = MATRIX[1]
    line17 = MATRIX[2]
    line18 = MATRIX[3]
    line19 = MATRIX[4]
    line20 = MATRIX[5]
    line21 = MATRIX[6]
    line22 = MATRIX[7]
    line23 = MATRIX[8]
    line24 = MATRIX[9]
    line25 = MATRIX[10]
    line26 = MATRIX[11]
    line27 = MATRIX[12]
    line28 = MATRIX[13]
    line29 = MATRIX[14]

    i = 15
    s1line16 = line16[i - 1] + line17[i - 2] + line18[i - 3] + line19[i - 4] + line20[i - 5] \
               + line21[i - 6] + line22[i - 7] + line23[i - 8] + line24[i - 9] + line25[i - 10] \
               + line26[i - 11] + line27[i - 12] + line28[i - 13] + line29[i - 14]
    s2line16 = s1line16[::-1]
    i = 15
    s1line17 = line17[i - 1] + line18[i - 2] + line19[i - 3] + line20[i - 4] + line21[i - 5] \
               + line22[i - 6] + line23[i - 7] + line24[i - 8] + line25[i - 9] + line26[i - 10] \
               + line27[i - 11] + line28[i - 12] + line29[i - 13]
    s2line17 = s1line17[::-1]
    i = 15
    s1line18 = line18[i - 1] + line19[i - 2] + line20[i - 3] + line21[i - 4] + line22[i - 5] \
               + line23[i - 6] + line24[i - 7] + line25[i - 8] + line26[i - 9] + line27[i - 10] \
               + line28[i - 11] + line29[i - 12]
    s2line18 = s1line18[::-1]
    i = 15
    s1line19 = line19[i - 1] + line20[i - 2] + line21[i - 3] + line22[i - 4] + line23[i - 5] \
               + line24[i - 6] + line25[i - 7] + line26[i - 8] + line27[i - 9] + line28[i - 10] \
               + line29[i - 11]
    s2line19 = s1line19[::-1]
    i = 15
    s1line20 = line20[i - 1] + line21[i - 2] + line22[i - 3] + line23[i - 4] + line24[i - 5] \
               + line25[i - 6] + line26[i - 7] + line27[i - 8] + line28[i - 9] + line29[i - 10]
    s2line20 = s1line20[::-1]
    i = 15
    s1line21 = line21[i - 1] + line22[i - 2] + line23[i - 3] + line24[i - 4] + line25[i - 5] \
               + line26[i - 6] + line27[i - 7] + line28[i - 8] + line29[i - 9]
    s2line21 = s1line21[::-1]
    i = 15
    s1line22 = line22[i - 1] + line23[i - 2] + line24[i - 3] + line25[i - 4] + line26[i - 5] \
               + line27[i - 6] + line28[i - 7] + line29[i - 8]
    s2line22 = s1line22[::-1]
    i = 15
    s1line23 = line23[i - 1] + line24[i - 2] + line25[i - 3] + line26[i - 4] + line27[i - 5] \
               + line28[i - 6] + line29[i - 7]
    s2line23 = s1line23[::-1]
    i = 15
    s1line24 = line24[i - 1] + line25[i - 2] + line26[i - 3] + line27[i - 4] + line28[i - 5] \
               + line29[i - 6]
    s2line24 = s1line24[::-1]
    i = 15
    s1line25 = line25[i - 1] + line26[i - 2] + line27[i - 3] + line28[i - 4] + line29[i - 5]
    s2line25 = s1line25[::-1]
    i = 15
    s1line26 = line26[i - 1] + line27[i - 2] + line28[i - 3] + line29[i - 4]
    s2line26 = s1line26[::-1]
    i = 15
    s1line27 = line27[i - 1] + line28[i - 2] + line29[i - 3]
    s2line27 = s1line27[::-1]
    i = 15
    s1line28 = line28[i - 1] + line29[i - 2]
    s2line28 = s1line28[::-1]
    i = 15
    s1line29 = line29[i - 1]
    s2line29 = s1line29[::-1]

    j = 5
    k = -1
    i = 15
    i += 1;
    k += 1
    print(i,'\t',s1line16,' '*(k),'\t'*j,i,'\t',s2line16)
    i+=1;k+=1
    print(i,'\t',s1line17,' '*(k),'\t'*j,i,'\t',s2line17)
    i+=1;k+=1
    print(i,'\t',s1line18,' '*(k),'\t'*j,i,'\t',s2line18)
    i+=1;k+=1
    print(i,'\t',s1line19,' '*(k),'\t'*j,i,'\t',s2line19)
    i+=1;k+=1
    print(i,'\t',s1line20,' '*(k),'\t'*j,i,'\t',s2line20)
    i+=1;k+=1
    print(i,'\t',s1line21,' '*(k),'\t'*j,i,'\t',s2line21)
    i+=1;k+=1
    print(i,'\t',s1line22,' '*(k),'\t'*j,i,'\t',s2line22)
    i+=1;k+=1
    print(i,'\t',s1line23,' '*(k),'\t'*j,i,'\t',s2line23)
    i+=1;k+=1
    print(i,'\t',s1line24,' '*(k),'\t'*j,i,'\t',s2line24)
    i+=1;k+=1
    print(i,'\t',s1line25,' '*(k),'\t'*j,i,'\t',s2line25)
    i+=1;k+=1
    print(i,'\t',s1line26,' '*(k),'\t'*j,i,'\t',s2line26)
    i+=1;k+=1
    print(i,'\t',s1line27,' '*(k),'\t'*j,i,'\t',s2line27)
    i+=1;k+=1
    print(i,'\t',s1line28,' '*(k),'\t'*j,i,'\t',s2line28)
    i+=1;k+=1
    print(i,'\t',s1line29,' '*(k),'\t'*j,i,'\t',s2line29)

    i = 0;
    j = 0;
    k = 0

    s1_15_29 = [s1line16] + [s1line17] + [s1line18] + [s1line19] + [s1line20] + [s1line21] \
               + [s1line22] + [s1line23] + [s1line24] + [s1line25] + [s1line26] + [s1line27] \
               + [s1line28] + [s1line29]
    s2_15_29 = [s2line16] + [s2line17] + [s2line18] + [s2line19] + [s2line20] + [s2line21] \
               + [s2line22] + [s2line23] + [s2line24] + [s2line25] + [s2line26] + [s2line27] \
               + [s2line28] + [s2line29]
    s1 = s1_1_15 + s1_15_29
    s2 = s2_1_15 + s2_15_29
    print(s1_15_29)
    print(s2_15_29)
    return s1, s2


def bs1_bs2(MATRIX):  # MATRIX is original 15 lines of STRING.
    line01 = MATRIX[0]
    line02 = MATRIX[1]
    line03 = MATRIX[2]
    line04 = MATRIX[3]
    line05 = MATRIX[4]
    line06 = MATRIX[5]
    line07 = MATRIX[6]
    line08 = MATRIX[7]
    line09 = MATRIX[8]
    line10 = MATRIX[9]
    line11 = MATRIX[10]
    line12 = MATRIX[11]
    line13 = MATRIX[12]
    line14 = MATRIX[13]
    line15 = MATRIX[14]
    # -----------------------------------------------------------
    #   USING "s1" instead of refactor to "bs1" and "bs2"
    i = 15
    s1line01 = line01[i - 1]
    s2line01 = s1line01[::-1]
    i -= 1
    s1line02 = line01[i - 1] + line02[i + 0]
    s2line02 = s1line02[::-1]
    i -= 1
    s1line03 = line01[i - 1] + line02[i + 0] + line03[i + 1]
    s2line03 = s1line03[::-1]
    i -= 1
    s1line04 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2]
    s2line04 = s1line04[::-1]
    i -= 1
    s1line05 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3]
    s2line05 = s1line05[::-1]
    i -= 1
    s1line06 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4]
    s2line06 = s1line06[::-1]
    i -= 1
    s1line07 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5]
    s2line07 = s1line07[::-1]
    i -= 1
    s1line08 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6]
    s2line08 = s1line08[::-1]
    i -= 1
    s1line09 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7]
    s2line09 = s1line09[::-1]
    i -= 1
    s1line10 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8]
    s2line10 = s1line10[::-1]
    i -= 1
    s1line11 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8] \
               + line11[i + 9]
    s2line11 = s1line11[::-1]
    i -= 1
    s1line12 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8] \
               + line11[i + 9] + line12[i + 10]
    s2line12 = s1line12[::-1]
    i -= 1
    s1line13 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8] \
               + line11[i + 9] + line12[i + 10] + line13[i + 11]
    s2line13 = s1line13[::-1]
    i -= 1
    s1line14 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8] \
               + line11[i + 9] + line12[i + 10] + line13[i + 11] + line14[i + 12]
    s2line14 = s1line14[::-1]
    i -= 1
    s1line15 = line01[i - 1] + line02[i + 0] + line03[i + 1] + line04[i + 2] + line05[i + 3] \
               + line06[i + 4] + line07[i + 5] + line08[i + 6] + line09[i + 7] + line10[i + 8] \
               + line11[i + 9] + line12[i + 10] + line13[i + 11] + line14[i + 12] + line15[i + 13]
    s2line15 = s1line15[::-1]
    # -----------------------------------------------------------
    print('\tBS1 MATRIX','\t'*9,'BS2 MATRIX')
    j = 5
    k = 15
    i = 0
    i += 1
    print(i,'\t',s1line01,' '*(k),'\t'*j,i,'\t\t',s2line01)
    i+=1;k-=1
    print(i,'\t',s1line02,' '*(k),'\t'*j,i,'\t\t',s2line02)
    i+=1;k-=1
    print(i,'\t',s1line03,' '*(k),'\t'*j,i,'\t\t',s2line03)
    i+=1;k-=1
    print(i,'\t',s1line04,' '*(k),'\t'*j,i,'\t\t',s2line04)
    i+=1;k-=1
    print(i,'\t',s1line05,' '*(k),'\t'*j,i,'\t\t',s2line05)
    i+=1;k-=1
    print(i,'\t',s1line06,' '*(k),'\t'*j,i,'\t\t',s2line06)
    i+=1;k-=1
    print(i,'\t',s1line07,' '*(k),'\t'*j,i,'\t\t',s2line07)
    i+=1;k-=1
    print(i,'\t',s1line08,' '*(k),'\t'*j,i,'\t\t',s2line08)
    i+=1;k-=1
    print(i,'\t',s1line09,' '*(k),'\t'*j,i,'\t\t',s2line09)
    i+=1;k-=1
    print(i,'\t',s1line10,' '*(k),'\t'*j,i,'\t',s2line10)
    i+=1;k-=1
    print(i,'\t',s1line11,' '*(k),'\t'*j,i,'\t',s2line11)
    i+=1;k-=1
    print(i,'\t',s1line12,' '*(k),'\t'*j,i,'\t',s2line12)
    i+=1;k-=1
    print(i,'\t',s1line13,' '*(k),'\t'*j,i,'\t',s2line13)
    i+=1;k-=1
    print(i,'\t',s1line14,' '*(k),'\t'*j,i,'\t',s2line14)
    i+=1;k-=1
    print(i,'\t',s1line15,' '*(k),'\t'*j,i,'\t',s2line15)
    i = 0
    bs1_1_15 = [s1line01] + [s1line02] + [s1line03] + [s1line04] + [s1line05] + [s1line06] + \
               [s1line07] + [s1line08] + [s1line09] + [s1line10] + [s1line11] + [s1line12] + \
               [s1line13] + [s1line14] + [s1line15]
    bs2_1_15 = [s2line01] + [s2line02] + [s2line03] + [s2line04] + [s2line05] + [s2line06] + \
               [s2line07] + [s2line08] + [s2line09] + [s2line10] + [s2line11] + [s2line12] + \
               [s2line13] + [s2line14] + [s2line15]
    print(bs1_1_15)
    print(bs2_1_15)
    # -----------------------------------------------------------

    i = 1
    s1line16 = line02[i - 1] + line03[i + 0] + line04[i + 1] + line05[i + 2] + line06[i + 3] \
               + line07[i + 4] + line08[i + 5] + line09[i + 6] + line10[i + 7] + line11[i + 8] \
               + line12[i + 9] + line13[i + 10] + line14[i + 11] + line15[i + 12]
    s2line16 = s1line16[::-1]
    i = 1
    s1line17 = line03[i - 1] + line04[i + 0] + line05[i + 1] + line06[i + 2] + line07[i + 3] \
               + line08[i + 4] + line09[i + 5] + line10[i + 6] + line11[i + 7] + line12[i + 8] \
               + line13[i + 9] + line14[i + 10] + line15[i + 11]
    s2line17 = s1line17[::-1]
    i = 1
    s1line18 = line04[i - 1] + line05[i + 0] + line06[i + 1] + line07[i + 2] + line08[i + 3] \
               + line09[i + 4] + line10[i + 5] + line11[i + 6] + line12[i + 7] + line13[i + 8] \
               + line14[i + 9] + line15[i + 10]
    s2line18 = s1line18[::-1]
    i = 1
    s1line19 = line05[i - 1] + line06[i + 0] + line07[i + 1] + line08[i + 2] + line09[i + 3] \
               + line10[i + 4] + line11[i + 5] + line12[i + 6] + line13[i + 7] + line14[i + 8] \
               + line15[i + 9]
    s2line19 = s1line19[::-1]
    i = 1
    s1line20 = line06[i - 1] + line07[i + 0] + line08[i + 1] + line09[i + 2] + line10[i + 3] \
               + line11[i + 4] + line12[i + 5] + line13[i + 6] + line14[i + 7] + line15[i + 8]
    s2line20 = s1line20[::-1]
    i = 1
    s1line21 = line07[i - 1] + line08[i + 0] + line09[i + 1] + line10[i + 2] + line11[i + 3] \
               + line12[i + 4] + line13[i + 5] + line14[i + 6] + line15[i + 7]
    s2line21 = s1line21[::-1]
    i = 1
    s1line22 = line08[i - 1] + line09[i + 0] + line10[i + 1] + line11[i + 2] + line12[i + 3] \
               + line13[i + 4] + line14[i + 5] + line15[i + 6]
    s2line22 = s1line22[::-1]
    i = 1
    s1line23 = line09[i - 1] + line10[i + 0] + line11[i + 1] + line12[i + 2] + line13[i + 3] \
               + line14[i + 4] + line15[i + 5]
    s2line23 = s1line23[::-1]
    i = 1
    s1line24 = line10[i - 1] + line11[i + 0] + line12[i + 1] + line13[i + 2] + line14[i + 3] \
               + line15[i + 4]
    s2line24 = s1line24[::-1]
    i = 1
    s1line25 = line11[i - 1] + line12[i + 0] + line13[i + 1] + line14[i + 2] + line15[i + 3]
    s2line25 = s1line25[::-1]
    i = 1
    s1line26 = line12[i - 1] + line13[i + 0] + line14[i + 1] + line15[i + 2]
    s2line26 = s1line26[::-1]
    i = 1
    s1line27 = line13[i - 1] + line14[i + 0] + line15[i + 1]
    s2line27 = s1line27[::-1]
    i = 1
    s1line28 = line14[i - 1] + line15[i + 0]
    s2line28 = s1line28[::-1]
    i = 1
    s1line29 = line15[i - 1]
    s2line29 = s1line29[::-1]
    j = 5
    k = 0 - 1
    i = 15
    i += 1;
    k += 1
    print(i,'\t',s1line16,' '*(k),'\t'*j,i,'\t',s2line16)
    i+=1;k+=1
    print(i,'\t',s1line17,' '*(k),'\t'*j,i,'\t',s2line17)
    i+=1;k+=1
    print(i,'\t',s1line18,' '*(k),'\t'*j,i,'\t',s2line18)
    i+=1;k+=1
    print(i,'\t',s1line19,' '*(k),'\t'*j,i,'\t',s2line19)
    i+=1;k+=1
    print(i,'\t',s1line20,' '*(k),'\t'*j,i,'\t',s2line20)
    i+=1;k+=1
    print(i,'\t',s1line21,' '*(k),'\t'*j,i,'\t',s2line21)
    i+=1;k+=1
    print(i,'\t',s1line22,' '*(k),'\t'*j,i,'\t',s2line22)
    i+=1;k+=1
    print(i,'\t',s1line23,' '*(k),'\t'*j,i,'\t',s2line23)
    i+=1;k+=1
    print(i,'\t',s1line24,' '*(k),'\t'*j,i,'\t',s2line24)
    i+=1;k+=1
    print(i,'\t',s1line25,' '*(k),'\t'*j,i,'\t',s2line25)
    i+=1;k+=1
    print(i,'\t',s1line26,' '*(k),'\t'*j,i,'\t',s2line26)
    i+=1;k+=1
    print(i,'\t',s1line27,' '*(k),'\t'*j,i,'\t',s2line27)
    i+=1;k+=1
    print(i,'\t',s1line28,' '*(k),'\t'*j,i,'\t',s2line28)
    i+=1;k+=1
    print(i,'\t',s1line29,' '*(k),'\t'*j,i,'\t',s2line29)
    i = 0
    j = 0
    k = 0
    bs1_15_29 = [s1line16] + [s1line17] + [s1line18] + [s1line19] + [s1line20] + [s1line21] \
                + [s1line22] + [s1line23] + [s1line24] + [s1line25] + [s1line26] + [s1line27] \
                + [s1line28] + [s1line29]
    bs2_15_29 = [s2line16] + [s2line17] + [s2line18] + [s2line19] + [s2line20] + [s2line21] \
                + [s2line22] + [s2line23] + [s2line24] + [s2line25] + [s2line26] + [s2line27] \
                + [s2line28] + [s2line29]
    bs1 = bs1_1_15 + bs1_15_29
    bs2 = bs2_1_15 + bs2_15_29
    print(bs1_15_29)
    print(bs2_15_29)
    return bs1, bs2


def word_search(matrix, words, matrix_name):
    mn = matrix_name[0:3]
    solution = []
    # print(f"\t\t Searching {matrix_name} for words")
    ws_count = 0
    word_line = 0
    solu = []
    for line in matrix:
        word_line += 1
        for word in words:
            start_char = line.find(word)
            if start_char != -1:
                # print(f'Found {word}({len(word)})  in {mn}, in line no.->{word_line} {line}')
                # print(f'\t'*5,f'starting at ->{(start_char+1)} ending at {(start_char + (len(word)))}')
                ws_count += 1
                cnt=ws_count
                solu = [mn, word, word_line, line, start_char + 1, start_char + len(word)]
                solution += [solu]
    return ws_count, solution


def final_solution(mn, solution, dict, count, start):
    # print('- - - - - - - - - -FINAL SOLUTION - - - - - - - - - - - - - - - - - -')
    # SOLUTION  [matrix name,word,row found,string,index of found word,last place index of word]
    # index -->       0        1      2        3            4                5
    if count != 0:  # if no word match in string, skip to end
        start_search = start  # use previous ending to start with this dict
        end_search = start_search + count  # add hit count to start for creating end
        start = end_search
        file = dict()  # there are 8 dict H1 H2 V1 V2 S1 S2 BS1 BS2
        print(f'{mn[0:3]}    Start Index->{start_search}  End Index ->{end_search - 1}')
        # index 0-matrix,1-word,2-row_line,3-string 4-index of found word, 5-last char of word
        for i in range(start_search, end_search):  # solution has a line for each word found (hit)
            row = col = 0  # if 30 hits  range is 0,1,2,...29 rows of solution list
            row = solution[i][2]  # grab row found - which string line (could be 1-29)
            col = solution[i][4]  # grab col found - index of hit location in string
            # match the solution data with dict data.  if same, you have location
            for key, value in file.items():  # file is dict
                if key == row:
                    for val in value:
                        if col not in val or not solution[i][1].isalpha():
                            continue
                        if val == "":
                            continue
                        row, col = SPLIT_location(val[2])  # take row,col to create Excel location
                        x = 15 - len(solution[i][1]) - 1
                        print(f'{solution[i][0]} {solution[i][1]}', ' ' * x,
                              f'Row: {row} Col: {col}\tExcel= {val[2]}')
                        break
        print(f'{mn} Word count= {count}')
        print()
        return start
    print(f'{mn} Word count= {count}')
    print()
    return start


# GRAB EXCEL LOCATION AND SPLIT INTO ROW, COL
def SPLIT_location(location):
    # print('location = ',location)
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Z']
    beta = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    # length=len(location)
    # print('location is ',location)
    row = location[1:]
    col = location[0]
    # print('row=',row,'  col=',col)
    # print('switch places ',row,col)
    for i in range(15):
        if col == alph[i]:
            col = beta[i]
    return row, col



def strings_words_40(file_name_40):
    getfile = file_name_40
    # -----------------------------------------------------------
    count = 0
    wd_cnt = 0
    with open(getfile, 'r') as fileIn:
        lines = []
        words = []
        game_name = ''
        for line in fileIn:
            line = line.replace('\n', '')
            count += 1
            if count <= 15:
                lines.append(line)
            elif count == 16:
                lines.append(line)
            elif count == 17:
                lines.append(line)
            elif getfile == 'file12' or 'file13' or 'file14' or 'file15' or 'file16':
                word10 = line.split('\t')
                lines += word10
            else:
                if count >= 18:
                    lines.append(line)
        fileIn.close
        with open("strings_words_40.txt", 'w') as fileOut:
            for line in lines:
                line = line + '\n'
                fileOut.write(line)
        print()
        fileOut.close()
        return "strings_words_40.txt"



def display_matrix_40(name, matrix, word_count):
    print(f'Word Puzzle Name - {name}    word count={word_count}')
    r = 1
    print('\t  Excel->  A   B   C   D   E   F   G   H   I   J   K   L   M   N   Z')
    print('\t  Col  ->  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15', end='')
    for line in matrix:
        if r < 10:
            print('\nRow \t', r, '\t', end='')
            for char in line:
                print('  ', char, end='')
        else:
            print('\nRow \t', r, '', end='')
            for char in line:
                print('  ', char, end='')
        r += 1
    print()
    print('\t  Index->  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15')
    print()
    return


def show_words(words,word_count):              # Max words is 40
    show_words=words[:]
    add_words = int(40 - int(word_count))           # add blank words at end
    new_count=0
    if add_words != 0:
        for j in range(add_words):              # from 0 to 9 for adding 10 words
            wrd = ("word" + str(word_count + j+1))
            show_words += [wrd]
        new_count = len(show_words)
    for i in range(40):
        s = len(show_words[i])
        t = (15 - s)*' '
        show_words[i] +=t
    for i in range(10):
        print(f'\t{i + 1} {show_words[i]} '
              f'\t{i + 11} {show_words[i + 10]} '
              f'\t{i + 21} {show_words[i + 20]} '
              f'\t{i + 31} {show_words[i + 30]}')

    print()
    return


def get_excel_strings():
    # To install openpyxl, Pycharm, open File at top most left side corner
    # Click settings, click Python Interpreter, click + to add pkg
    # Way up left, to SEARCH Bar:  type openpy  to search for openpyxl
    # Find openpyxl in list, click, go down to INSTALL PKG, exit, exit.
    import openpyxl
    from openpyxl import load_workbook
    workbook = load_workbook("EXCEL_Strings_Words.xlsx")   # file must be in path location
    matrix = workbook["FirstSheet"]
    string_data = []            # "Axx" cell count   15+2+24=41   15+2+30=47     15+2+40=57
    line24 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
              'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
              'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41']
    line30 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
              'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
              'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45',
              'A46', 'A47']
    line40 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
              'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30',
              'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45',
              'A46', 'A47', 'A48', 'A49', 'A50', 'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57']
    cells=57            # openpyxl uses A1-A99.  Can be changed to B or C etc
    # assume 40 words to search for in 15 strings and 2-file name,word count
    m2 = []
    for i in range(1, cells+1):
        m2 += [("A" + str(i))]      # use m2 matrix as index to reading worksheet
    workbook.close
    # print('Axx count" = ',m2)             # did we create 57 cells A01-A57?
# this only prints out raw data from Excel file.
#     for i in range(1, 16):
#         print(i, matrix[m2[i - 1]].value)
#     print()
#     for j in range(16, 18):
#         print(j, (matrix[m2[j - 1]].value))
#     print()
#     for k in range(18, 58):
#         print(k, (matrix[m2[k - 1]].value))
#     print()
                                            # Don't write out empty cells at end of word list
    # cells = int(matrix[m2[16]].value)
    with open("EXCEL_s_w.txt", 'w') as file:
        words_in_file=int(matrix[m2[16]].value)     # fetch count of search words from Excel file
        empty_cells=57-(words_in_file+17)
        for i in range(57-empty_cells):                     #-empty_cells):
            line = str(matrix[m2[i]].value)
            line = line + '\n'
            file.write(line)
    print()
    string_data.clear()
    file.close()
    return "EXCEL_s_w.txt"


def begin_word_search():
    print()
    print('1 = STRINGS_Poker_Words.txt')
    print('2 = STRINGS_Meteor.txt')
    print('3 = STRINGS_StarWars_Words.txt')
    print('4 = STRINGS_Victorian_Writers.txt')
    print('5 = STRINGS_WW1_Nurse.txt')
    print('6 = EXCEL_s_w.txt')
    print('7 = STRINGS_MIL_SERVICE.txt')
    print('8 = STRINGS_zoo_animals.txt')
    print('9 = STRINGS_python.txt')
    print('10 = STRINGS_horizontal.txt')
    print('11 = STRINGS_WORDS_560.txt(Not yet ok')
    print('12 = strings_words_560A.txt')
    print('13 = strings_words_560B.txt')
    print('14 = strings_words_560N.txt')

    getfile = ''
    file1 = 'STRINGS_Poker_Words.txt'
    file2 = 'STRINGS_Meteor.txt'
    file3 = 'STRINGS_StarWars.txt'
    file4 = 'STRINGS_Victorian_Writers.txt'
    file5 = 'STRINGS_WW1_Nurse.txt'
    file6 = 'EXCEL_s_w.txt'
    file7 = 'STRINGS_MIL_SERVICE.txt'
    file8 = 'STRINGS_zoo_animals.txt'
    file9 = 'STRINGS_python.txt'
    file10 = 'STRINGS_horizontal.txt'
    file11 = 'STRINGS_WORDS_560.txt'
    file12 = 'strings_words_560A.txt'
    file13 = 'strings_words_560B.txt'
    file14 = 'strings_words_560N.txt'
    # -----------------------------------------------------------
    getfile = input("Enter (1 - 14 or q): ")
    if len(getfile) == 0 or getfile == '0' or getfile=='q':
        exit()
    elif getfile == '1':
        getfile = file1
    elif getfile == '2':
        getfile = file2
    elif getfile == '3':
        getfile = file3
    elif getfile == '4':
        getfile = file4
    elif getfile == '5':
        getfile = file5
    elif getfile == '6':
        file6=get_excel_strings()
        getfile = file6
    elif getfile == '7':
        getfile = file7
    elif getfile == 8:
        getfile = file8
    elif getfile == '9':
        getfile = file9
    elif getfile == '10':
        getfile = file10
    elif getfile == '11':
        getfile = file11
    elif getfile == '12':
        getfile = strings_words_40(file12)
    elif getfile == '13':
        getfile = strings_words_40(file13)
    elif getfile == '14':
        getfile = strings_words_40(file14)
    else:
        print(' Screeeeeech.....Next Time, Please Enter 0,1,2....14   dummy!')
        exit()
    # -----------------------------------------------------------
    count = 0
    wd_cnt = 0
    with open(getfile, 'r') as f:
        lines = []
        words = []
        game_name = ''
        for line in f:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            #  clean dirty strings
            #             line = line.replace('\t','')
            #             line = line.replace('|', 'I')
            #             line = line.replace('!', 'I')
            #             line = line.replace('1', 'I')
            #             line = line.replace('/', 'I')
            #             line = line.replace(',', '')
            #             line = line.replace('', '')
            #             line = line.replace('"', '')
            #             line = line.replace("'", '')
            #             line = line.replace('.', '')

            count += 1
            if count <= 15:
                lines.append(line)
            elif count == 16:
                game_name = getfile
            elif count == 17:
                word_count = int(line)
            elif getfile == 'STRINGS_words_560.txt':
                word10 = line.split('\t')
                words += word10
            else:
                if count >= 18:
                    words.append(line)
        f.close
        return lines, words, game_name, word_count

