"""
  ext file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os
from itertools import imap

WORK_DIR = os.getcwd()


def global_replacement(input_file, output_file, original_word, replace_word):
  '''
  Replaces the <origina_word> with <replace_word>...

  input_file - handle of the INPUT file (fileObject)
  output_file - handle of the OUTPUT file (fileObject)
  original_word - a word to seek for
  replace_word - a word to replace
  '''

  replace_the_word = lambda x: x.replace(original_word, replace_word)
  changed_file = imap(replace_the_word, input_file)							# Creates iterable with changes  
  
  while True:
    try:
      output_file.write(changed_file.next())
    except StopIteration:
  	  break


def make_uniques_dict(input_file):
  '''
  '''
  uniques = {}
  for line in input_file:
    for symb in '!@#$%^&*()_+=-[]{}.,:;\'\"?':
      line = line.replace(symb, '')
    list_of_words = line.split()
    for each in list_of_words:
      if each not in uniques:
        uniques[each] = 1
      else:
        uniques[each] += 1

  return uniques


#def update_dict(dict1, dict2):
#  for key in dict2.keys():
#    if key in dict1:
#	    dict1[key] += dict2[key]
#	  else:
#       dict1[key] = dict2[key]
#	return dict1

file_name = 'lorem.txt'
path_to_file = os.path.join(WORK_DIR, file_name)
path_to_mod_file = os.path.join(WORK_DIR, file_name.split('.')[0]+'_mod.txt')	# Adds '_mod' to the filename

# GLOBAL REPLACE TEST
file_to_read = open(path_to_file, 'r')
file_to_write = open(path_to_mod_file, 'w')

global_replacement(file_to_read, file_to_write, 'at', 'FFF')

file_to_read.close()
file_to_write.close()

# MAKE UNIQUES TEST
file_to_read = open(path_to_file, 'r')
print(make_uniques_dict(file_to_read))

file_to_read.close()
