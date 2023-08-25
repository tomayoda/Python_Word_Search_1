
def read_560_words():
    getfile = ''
    file1 = 'STRINGS_WORDS_560.TXT'
#-----------------------------------------------------------
    getfile = input("Enter 1 to read 560 words plus STRING ")
    if getfile !='1':
        exit()
    elif getfile != '1':
        getfile = file1
    else:
        getfile = file1
      # -----------------------------------------------------------
    with open(getfile, 'r') as f:
        count = 0
        wd_cnt = 0
        lines = []
        words = []
        game_name = ''
        for line in f:
        # for line in f:
            line = line.replace('\n', '')
            line = line.replace('\t','')
            # print('length of each line',len(line))
        #     line = line.replace(' ', '')
#  clean dirty strings
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
            if count == 16:
                game_name=getfile
            if count == 17:
                word_count=int(line)
            if count >= 18:
                words.append(line[0]+line[1]+line[2])
                words.append(line[3]+line[4]+line[5])
                words.append(line[6]+line[7]+line[8])
                words.append(line[9]+line[10]+line[11])
                words.append(line[12]+line[13]+line[14])
                words.append(line[15]+line[16]+line[17])
                words.append(line[18]+line[19]+line[20])
                words.append(line[21]+line[22]+line[23])
                words.append(line[24]+line[25]+line[26])
                words.append(line[27]+line[28]+line[29])
    return lines, words, game_name, word_count

lines,words,game_name,word_count = read_560_words()
print(len(lines),lines)
print()
print(len(words),words)