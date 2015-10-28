"""
Text file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os

from collections import defaultdict
from itertools import imap

WORK_DIR = os.getcwd()
UNIQUES = []

def global_replacement(file_name, origina_word, replace_word):
  '''
  Replaces the <origina_word> with <replace_word> in original file <file_name> & saves it to 
  <file_name>_mod.txt .

  file_name - name of the file in working dir
  origina_word - a word to seek for
  replace_word - a word to replace
  '''

  path_to_file = os.path.join(WORK_DIR, file_name)
  path_to_mod_file = os.path.join(WORK_DIR, file_name.split('.')[0]+'_mod.txt')	# Adds '_mod' to the filename

  file_to_read = open(path_to_file, 'r')

  replace_the_word = lambda x: x.replace(origina_word, replace_word)
  changed_file = imap(replace_the_word, file_to_read)							# Creates iterable with changes
  
  file_to_write = open(path_to_mod_file, 'w')
  
  for line in changed_file:
    file_to_write.write(line)
  
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

global_replacement('lorem.txt', 'ut', 'XXX')

make_uniques_list('lorem.txt')
