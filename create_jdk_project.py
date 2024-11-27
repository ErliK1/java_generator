import os 
import sys

args = sys.argv

current_path = os.getcwd()
path_of_new_dir = os.path.join(current_path, args[1])
path_of_src_main  = os.path.join(path_of_new_dir, 'src')
path_of_bin = os.path.join(path_of_new_dir, 'bin')
os.makedirs(path_of_src_main)
os.makedirs(path_of_bin)
os.chdir(path_of_src_main)
with open('Main.java', 'w') as fp:
    fp.write('public class Main {\n')
    fp.write('\tpublic static void main(String[] args){\n\n') 
    fp.write('\t}\n}')



