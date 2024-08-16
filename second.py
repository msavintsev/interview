import os
import shutil
import ftplib
from contextlib import contextmanager

# Настройки FTP
FTP_HOST = 'ftp.example.com'
FTP_USER = 'username'
FTP_PASS = 'password'
FTP_DIRECTORY = '/test'
FTP_FILE = 'test.zip'

# Целевая папка для распаковки
TARGET_DIRECTORY = '/path/to/target/directory'

@contextmanager
def ftp_connection():
    try:
        # Подключение к FTP-серверу
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_DIRECTORY)
        yield ftp
    finally:
        ftp.quit()

def download_file(ftp, filename, local_path):
    with open(local_path, 'wb') as file:
        ftp.retrbinary(f'RETR {filename}', file.write)

def extract_zip(zip_file, target_dir):
    shutil.unpack_archive(zip_file, target_dir)

def cleanup(filename):
    os.remove(filename)

def download_and_extract_zip():
    try:
        local_zip_file = FTP_FILE
        with ftp_connection() as ftp:
            download_file(ftp, FTP_FILE, local_zip_file)
        extract_zip(local_zip_file, TARGET_DIRECTORY)
        cleanup(local_zip_file)
        print('Архив успешно загружен и распакован.')
    except (ftplib.error_perm, OSError) as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    download_and_extract_zip()
