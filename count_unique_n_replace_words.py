"""
Text file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os

WORK_DIR = os.getcwd()

def global_replacement(file_name, origina_word, replace_word):
  '''
  Replaces the <origina_word> with <replace_word> in file <file_name>.

  file_name - name of the file in working dir
  origina_word - a word to seek for
  replace_word - a word to replace
  '''

  path_to_file = os.path.join(WORK_DIR, file_name)
  file_read = open(path_to_file, 'r')
  data = ''

  for line in file_read:
    line = line.replace(origina_word, replace_word)
    data += line

  file_read.close()

  file_write = open(path_to_file, 'w')
  file_write.write(data)
  file_write.close()


global_replacement('lorem.txt', 'ut', 'XXX')

