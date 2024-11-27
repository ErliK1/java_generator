import os 
import subprocess

def compile():
    current_path = os.getcwd()

    if (current_path.split('/')[-1] == 'src'):
        current_path = current_path.split('/')[0:-1]
        current_path = '/'.join(current_path)
        os.chdir(current_path)

    dir_list = os.listdir()

    if not ('src' in dir_list and 'bin' in dir_list):
        raise OSError("src/bin not found. Are you sure you are in project dir?")

    src_dir = os.path.join(current_path, 'src')
    bin_dir = os.path.join(current_path, 'bin')

    os.chdir(src_dir)

    src_files = os.listdir()
    java_files = list(filter(lambda x: '.java' in x, src_files))

    java_files_str = ' '.join(java_files)

    os.system(f'javac -d {bin_dir} {java_files_str}')


if __name__ == '__main__':
    compile()
