# MOST print statements in this app are # commented.  There are 2 sets of this app.
# Please use XXX_PYTHON_word_search_V1_0.py to see extreme detailed steps
# Do NOT delete what may appear to be useless or comments.  Backup everything before using!!!
# Be careful, if you are a Python beginner.  Code is vunerable and NOT bulletproof.
# Python 3.11 program to solve 15x15 matrix 24,30,40 words 082323'
print()
# ---------------------------------------------------------------------------
from DEF1_matrix_V1_0 import *
from DEF2_char_dict_V1_0 import *
found_words_count = 0
hits = 0
# ---------------------------------------------------------------------------
print("-----------Welcome to Word_Search V1.0 - Python 3.11 ---------------")
# ---------------------------------------------------------------------------
H1_MATRIX = []
WORDS = []
NAME = ''
H1_MATRIX, WORDS, NAME, WORD_COUNT = begin_word_search()
# print(f'MATRIX= {len(H1_MATRIX)}   {H1_MATRIX}')
# print(f'WORDS=  {WORD_COUNT}   {WORDS}')
# print(f'FileName =   {NAME}\n')
# ---------------------------------------------------------------------------
# display_matrix_40(NAME, H1_MATRIX, WORD_COUNT)
# show_words(WORDS, WORD_COUNT)
# ---------------------------------------------------------------------------
matrix_name = "H1_MATRIX"
# for i,word in enumerate(H1_MATRIX):
#     print (i+1,'\t',word)
# h1_count=0
cnt = 0
solution = []
h1_count, h1_solution = word_search(H1_MATRIX, WORDS, matrix_name)
# print('h1 solution = ',h1_solution)
h1_hits = h1_count
# if h1_count >=1:
#     print(f"Found {h1_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += h1_count
# print(f"Words found {matrix_name} {h1_count}")
# ---------------------------------------------------------------------------
H2_MATRIX = h1_h2(H1_MATRIX)
# for i,word in enumerate(H2_MATRIX):
#     print (i+1,'\t',word)
matrix_name = 'H2_MATRIX'
# matrix = H2_MATRIX[:]
# h2_count=0
h2_count, h2_solution = word_search(H2_MATRIX, WORDS, matrix_name)
h2_hits = h2_count
# if h2_count >=1:
#     print(f"Found {h2_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += h2_count
# print(f"words found {matrix_name} {h2_count}")
# ---------------------------------------------------------------------------
V1_MATRIX = h1_v1(H1_MATRIX)
# for i,word in enumerate(V1_MATRIX):
#     print (i+1,'\t',word)
# ---------------------------------------------------------------------------
matrix_name = 'V1_MATRIX'[0:3]
matrix = V1_MATRIX[:]
v1_count = 0
v1_count, v1_solution = word_search(V1_MATRIX, WORDS, matrix_name)
v1_hits = v1_count
# if v1_count >=1:
#     print(f"Found {v1_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += v1_count
# print(f"words found {matrix_name} {v1_count}")
# ---------------------------------------------------------------------------
V2_MATRIX = v1_v2(V1_MATRIX)
# for i,word in enumerate(V2_MATRIX):
#     print (i+1,'\t',word)
matrix_name = 'V2_MATRIX'[0:3]
matrix = V2_MATRIX[:]
v2_count = 0
v2_count, v2_solution = word_search(V2_MATRIX, WORDS, matrix_name)
v2_hits = v2_count
# if v2_count >=1:
#     print(f"Found {v2_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += v2_count
# print(f"words found {matrix_name} {v2_count}")
# ---------------------------------------------------------------------------
# matrix=H1_MATRIX
# words=WORDS
matrix_name = NAME
S1_MATRIX, S2_MATRIX = s1_s2(H1_MATRIX)
# -----------------------------------------------------------
matrix_name = 'S1_MATRIX'[0:3]
# matrix = S1_MATRIX[:]
# words = WORDS
# s1_count=0
s1_count, s1_solution = word_search(S1_MATRIX, WORDS, matrix_name)
s1_hits = s1_count
# if s1_count >=1:
#     print(f"Found {s1_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += s1_count
# print(f"words found {matrix_name} {s1_count}")
# -----------------------------------------------------------
matrix_name = 'S2_MATRIX'[0:3]
# matrix = S2_MATRIX[:]
# words = WORDS
# s2_count=0
s2_count, s2_solution = word_search(S2_MATRIX, WORDS, matrix_name)
s2_hits = s2_count
# if s2_count >=1:
#     print(f"Found {s2_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += s2_count
# print(f"words found {matrix_name} {s2_count}")
# ==================================================================
# matrix=H1_MATRIX
# words=WORDS
matrix_name = NAME
BS1_MATRIX, BS2_MATRIX = bs1_bs2(H1_MATRIX)
# -----------------------------------------------------------
# GO SEARCH BS1   WITH LINES 1-29 WITH 24 WORDS
# -----------------------------------------------------------
matrix_name = 'BS1_MATRIX'[0:3]
# matrix = BS1_MATRIX[:]
# words = WORDS
# bs1_count=0
cnt = 0
solution = []
bs1_count, bs1_solution = word_search(BS1_MATRIX, WORDS, matrix_name)
bs1_hits = bs1_count
# if bs1_count >=1:
#     print(f"Found {bs1_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += bs1_count
# -----------------------------------------------------------
matrix_name = 'BS2_MATRIX'[0:3]
# matrix = BS2_MATRIX[:]
# words = WORDS
# bs2_count=0
bs2_count, bs2_solution = word_search(BS2_MATRIX, WORDS, matrix_name)
bs2_hits = bs2_count
# if bs2_count >=1:
#     print(f"Found {bs2_count} words in matrix {matrix_name} ")
# else:
#     print(f"Did NOT find any words in matrix {matrix_name}\n ")
found_words_count += bs2_count
# print(f"words found {matrix_name} {bs2_count}")
# print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
# print(f'Total words found {found_words_count}')
# print('- - - - - - - - - - - - - -Create Solution - - - - - - - - - - - - - -')
words_found = h1_count + h2_count + v1_count + v2_count + s1_count + s2_count + bs1_count + bs2_count

hits = h1_hits + h2_hits + v1_hits + v2_hits + s1_hits + s2_hits + bs1_hits + bs2_hits

solution = h1_solution + h2_solution + v1_solution + v2_solution + \
           s1_solution + s2_solution + bs1_solution + bs2_solution
# print('- - - - - - - display-PRE-SOLUTION dictionary- - - - - - - - - - - - - - - - -')
# print(' H,V,S,BS    Word         Row    String        Index TO Index')
# k=0
# for i,sol in enumerate(solution):
#     x=15-len(sol[1])
#     y=15-len(sol[3])
#     print(i+1,'\t',sol[0],sol[1],' '*x,sol[2],'\t',sol[3],' '*y,sol[4],'  ',sol[5])
#     print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
# print('hit index of row, index of last char in row   0,1,2 is 3 hits')
# print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

print('\n\n---------------FINAL SOLUTION-------------------------')

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
## ---------------------------------------------------------------------------
display_matrix_40(NAME, H1_MATRIX, WORD_COUNT)
show_words(WORDS, WORD_COUNT)
## ---------------------------------------------------------------------------
# print('****************** T H E   E N D   *********************************')
