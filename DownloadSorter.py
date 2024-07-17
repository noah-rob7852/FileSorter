import os
import pathlib
import shutil

FILE_SUFFIXES = ['.txt', '.mp4', '.mp3', '.jpeg', '.jpg', '.doc', '.docx', '.pptx',
                 '.exe', '.msi', '.png', '.pdf', '.html', '.csv', '.xlsx', '.bat']


def sort_files(filepath):
    for file in os.listdir(filepath):
        if pathlib.Path(file).suffix and file != __file__ and pathlib.Path(file).suffix in FILE_SUFFIXES:
            try:
                os.mkdir(f'{filepath}\\{pathlib.Path(file).suffix}')
            except OSError as e:
                pass
            except Exception as e:
                print(f'Unhandled exception occurred: {e}')

            try:
                shutil.move(f'{filepath}\\{file}', f'{filepath}\\{pathlib.Path(file).suffix}\\{file}')
                print(f'Moved {file} to {filepath}\\{pathlib.Path(file).suffix}')
            except Exception as e:
                print(f'Failed to move {file} to {filepath}\\{pathlib.Path(file).suffix}.')


if __name__ == "__main__":
    sort_files(os.getcwd())
