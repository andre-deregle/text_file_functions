"""
  ext file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os

from collections import defaultdict
from itertools import imap

WORK_DIR = os.getcwd()
UNIQUES = []


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


def make_uniques_list(file_name):
  global UNIQUES
  dict_of_uniq = defaultdict(int)
  path_to_file = os.path.join(WORK_DIR, file_name)
  file_to_read = open(path_to_file, 'r')

  for line in file_to_read:
    for symb in '!@#$%^&*()_+=-[]{}.,:;\'\"?':
      line = line.replace(symb, '')
    list_of_words = line.split()
    for each in list_of_words:
      dict_of_uniq[each] += 1
      if each not in UNIQUES:
        UNIQUES.append(each)
  file_to_read.close()
  for key, value in dict_of_uniq.iteritems():
    print key, "-", value
  print "Uniques array:\n", UNIQUES, "\nUniques words count:\n", len(UNIQUES)

global_replacement('at', 'FFF', 'lorem.txt')


make_uniques_list('lorem.txt')
