"""
Text file functions.
Authors:
  Nazar Ivantsiv
  Andriy Bondarev
"""
import os

WORK_DIR = os.getcwd()

def read_file_into_string(file_name):
  string_of_file = ''
  path_to_file = os.path.join(WORK_DIR, file_name)
  file_to_read = open(path_to_file, 'r')
  for line in file_to_read:
    string_of_file += line
  file_to_read.close()
  return string_of_file

read_file_into_string('lorem.txt')