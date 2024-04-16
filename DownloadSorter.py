import os
import pathlib
import shutil
def sort_files(filepath):
    for file in os.listdir(filepath):
        if pathlib.Path(file).suffix and file != __file__:
            try:
                os.mkdir(f'{filepath}\\{pathlib.Path(file).suffix}')
            except OSError as e:
                pass
            except Exception as e:
                print(f'Unhandled exception occurred: {e}')
            shutil.move(f'{filepath}\\{file}', f'{filepath}\\{pathlib.Path(file).suffix}\\{file}')
            print(f'Moved {file} to {filepath}\\{pathlib.Path(file).suffix}')
if __name__ == "__main__":
    sort_files(os.getcwd)