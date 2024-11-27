import os 

def execute():
    current_path = os.getcwd()

    if current_path.split('/')[-1] in ['src', 'bin']:
        current_path = current_path.split('/')[0:-1]
        current_path = '/'.join(current_path)
        os.chdir(current_path)

    dir_list = os.listdir()

    if not ('src' in dir_list and 'bin' in dir_list):
        raise OSError("src/bin not found. Are you sure you are inside the project")

    bin_dir = os.path.join(current_path, 'bin')

    os.chdir(bin_dir)

    dir_list = os.listdir()

    if ('Main.class' not in dir_list):
        raise OSError("Main executable class not found")

    main_cls = list(filter(lambda x: x == 'Main.class', dir_list))[0]

    main_cls = main_cls[0:-6]

    os.system(f'java {main_cls}')


if __name__ == '__main__':
    execute()



