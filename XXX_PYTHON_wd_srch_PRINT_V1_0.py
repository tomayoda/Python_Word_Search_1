# MOST print statements are active in this version. Some duplicate print in App and Def.
# Use the other app (which prints only answers): PYTHON_Word_Search_V1_0.py
# Do NOT delete what may appear to be useless.  Backup Copy everything before using!!!
# Be careful, if you are a Python beginner.  Code is vunerable and NOT bulletproof.
# Python 3.11 program to solve 15x15 matrix 24,30,40 words 082323'
print()
# ---------------------------------------------------------------------------
from XXX_DEF1_matrix_PRINT_V1_0 import *
from XXX_DEF2_char_dict_PRINT_V1_0 import *
found_words_count = 0
hits = 0
# ---------------------------------------------------------------------------
print("-----------Welcome to Word_Search V1.0 - Python 3.11 ---------------")
# ---------------------------------------------------------------------------
H1_MATRIX,THE_WORDS, NAME, WORD_COUNT = begin_word_search()
print(f'MATRIX= {len(H1_MATRIX)}   {H1_MATRIX}')
print(f'WORDS=  {WORD_COUNT}   {THE_WORDS}')
print(f'FileName =   {NAME}\n')
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# display_matrix_40(NAME, H1_MATRIX, WORD_COUNT)
# show_words(THE_WORDS, WORD_COUNT)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('H1_MATRIX')
for i,word in enumerate(H1_MATRIX):
    print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = "H1_MATRIX"[0:3]
h1_count, h1_solution = word_search(H1_MATRIX, THE_WORDS, matrix_name)
if h1_count >=1:
    print(f"Found {h1_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += h1_count
print(f"Words found {matrix_name} {h1_count}\n")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('H2_MATRIX')
H2_MATRIX = h1_h2(H1_MATRIX)
for i,word in enumerate(H2_MATRIX):
    print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = 'H2_MATRIX'
h2_count, h2_solution = word_search(H2_MATRIX, THE_WORDS, matrix_name)
if h2_count >=1:
    print(f"Found {h2_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += h2_count
print(f"words found {matrix_name} {h2_count}\n")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# print('V1_MATRIX')
V1_MATRIX = h1_v1(H1_MATRIX)
for i,word in enumerate(V1_MATRIX):
    print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = 'V1_MATRIX'[0:3]
v1_count, v1_solution = word_search(V1_MATRIX, THE_WORDS, matrix_name)
if v1_count >=1:
    print(f"Found {v1_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += v1_count
print(f"words found {matrix_name} {v1_count}\n")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# print('V2_MATRIX')
V2_MATRIX = v1_v2(V1_MATRIX)
for i,word in enumerate(V2_MATRIX):
    print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = 'V2_MATRIX'[0:3]
v2_count, v2_solution = word_search(V2_MATRIX, THE_WORDS, matrix_name)
if v2_count >=1:
    print(f"Found {v2_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += v2_count
print(f"words found {matrix_name} {v2_count}\n")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# print('S1_MATRIX')
S1_MATRIX, S2_MATRIX = s1_s2(H1_MATRIX)
# for i,word in enumerate(S1_MATRIX):
#     print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = 'S1_MATRIX'[0:3]
s1_count, s1_solution = word_search(S1_MATRIX, THE_WORDS, matrix_name)
if s1_count >=1:
    print(f"Found {s1_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += s1_count
print(f"words found {matrix_name} {s1_count}\n")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# print('S2_MATRIX')
# for i,word in enumerate(S2_MATRIX):
#     print (i+1,'\t',word)
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
matrix_name = 'S2_MATRIX'[0:3]
s2_count, s2_solution = word_search(S2_MATRIX, THE_WORDS, matrix_name)
if s2_count >=1:
    print(f"Found {s2_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += s2_count
print(f"words found {matrix_name} {s2_count}\n")
## ==================================================================
# print('BS1_MATRIX')
BS1_MATRIX, BS2_MATRIX = bs1_bs2(H1_MATRIX)
# for i,word in enumerate(BS1_MATRIX):
#     print (i+1,'\t',word)
## ==================================================================
matrix_name = 'BS1_MATRIX'[0:3]
bs1_count, bs1_solution = word_search(BS1_MATRIX, THE_WORDS, matrix_name)
if bs1_count >=1:
    print(f"Found {bs1_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += bs1_count
print(f"words found {matrix_name} {bs1_count}\n")
## ==================================================================
print('BS2_MATRIX')
# for i,word in enumerate(BS2_MATRIX):
#     print (i+1,'\t',word)
## ==================================================================
matrix_name = 'BS2_MATRIX'[0:3]
bs2_count, bs2_solution = word_search(BS2_MATRIX, THE_WORDS, matrix_name)
if bs2_count >=1:
    print(f"Found {bs2_count} words in matrix {matrix_name} ")
else:
    print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += bs2_count
print(f"words found {matrix_name} {bs2_count}\n")
## ==================================================================
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print(f'Total words found {found_words_count}')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

# words_found = h1_count + h2_count + v1_count + v2_count\
#               + s1_count + s2_count + bs1_count + bs2_count

print('- - - - - - - display-PRE-SOLUTION dictionary- - - - - - - - - - - - - - - - -\n')
solution = h1_solution + h2_solution + v1_solution + v2_solution + \
           s1_solution + s2_solution + bs1_solution + bs2_solution

print(' H,V,S,BS    Word         Row    String        Index TO Index\n')
## ==================================================================
k=0
for i,sol in enumerate(solution):
    x=15-len(sol[1])
    y=15-len(sol[3])
    print(i+1,'\t',sol[0],sol[1],' '*x,sol[2],'\t',sol[3],' '*y,sol[4],'  ',sol[5])
## ==================================================================
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n')

print('\n\n----------------------FINAL SOLUTION------------------------------\n')
start = final_solution('H1_', solution, h1_char_dict, h1_count, 0)
start = final_solution('H2_', solution, h2_char_dict, h2_count, start)
start = final_solution('V1_', solution, v1_char_dict, v1_count, start)
start = final_solution('V2_', solution, v2_char_dict, v2_count, start)
start = final_solution('S1_', solution, s1_char_dict, s1_count, start)
start = final_solution('S2_', solution, s2_char_dict, s2_count, start)
start = final_solution('BS1_', solution, bs1_char_dict, bs1_count, start)
start = final_solution('BS2_', solution, bs2_char_dict, bs2_count, start)
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print(f'Total words found {found_words_count}\n')
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
display_matrix_40(NAME, H1_MATRIX, WORD_COUNT)
show_words(THE_WORDS, WORD_COUNT)
# ---------------------------------------------------------------------------
# print('\n*********************************************************************')
# print('\t\t\t\t\tTotal words found = ',found_words_count)
# print('***********************************************************************')
print('********************** THE END *****************************************')
