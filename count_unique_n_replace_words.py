"""
Text file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os
from itertools import imap

WORK_DIR = os.getcwd()

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

global_replacement('lorem.txt', 'ut', 'XXX')

