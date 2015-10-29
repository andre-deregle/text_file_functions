"""
  ext file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os
from itertools import imap

WORK_DIR = os.getcwd()


def global_replacement(original_word, replace_word, input_filename, output_filename=''):
  '''
  Replaces the <origina_word> with <replace_word> in <input_filename> and saves
  the changes to <output_filename> (or to <input_filename>_mod.txt).

  input_filename - handle of the INPUT file (fileObject)
  output_filename - handle of the OUTPUT file (fileObject)
  original_word - a word to seek for
  replace_word - a word to replace
  '''
  input_path = os.path.join(WORK_DIR, input_filename)
  if output_filename == '':	
  	output_path = os.path.join(WORK_DIR, input_filename.split('.')[0]+'_mod.txt')	# Adds '_mod' to the input_filename
  else:
    output_path = os.path.join(WORK_DIR, output_filename)
  
  file_to_read = open(input_path, 'r')
  file_to_write = open(output_path, 'w')

  changed_file = imap( lambda x: x.replace(original_word, replace_word), file_to_read )			# Creates generator to output strs with words changed

  while True:		# Using this iteration through the Generator NOT too use any temp variables
      try:
        file_to_write.write(changed_file.next())
      except StopIteration:
        break

  file_to_read.close()
  file_to_write.close()


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


# GLOBAL REPLACE TEST

global_replacement('at', 'FFF', 'lorem.txt')

# MAKE UNIQUES TEST
#file_to_read = open(path_to_file, 'r')
#print(make_uniques_dict(file_to_read))

#file_to_read.close()
