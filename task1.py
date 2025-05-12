import sys
from pathlib import Path
import os
import shutil

def is_folder(directory):
    if not directory.exists():
        print(f'The path {directory} does not exist!')
    elif directory.suffix:
        print(f'The path {directory} leads to a file!')
    else:
        return True

def recursive_folder_sorted_copy(source, target):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_folder_sorted_copy(el, target)
            else:
                if os.access(el, os.R_OK):
                    ext = el.suffix[1:] if el.suffix else "no_extension"
                    ext_dir = target/ext
                    ext_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(el, ext_dir/el.name)
                else:
                    print(f'{el} is not accessible')             
    except Exception as e:
        print(f'Error - {e}')

def main():
    if len(sys.argv) > 1:
        source_directory = Path(sys.argv[1])
        if not is_folder(source_directory):
            return
        if len(sys.argv) > 2:
            target_directory = Path(sys.argv[2])
        else:
            target_directory = Path('temp')
    else:
        print('No source and target directories in the request! The source directory is required')
        return
    

    target_directory.mkdir(parents=True, exist_ok=True)
    recursive_folder_sorted_copy(source_directory, target_directory)
    print('Copying is successful')

if __name__ == "__main__":
    main()