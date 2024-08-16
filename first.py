import os
import shutil
import ftplib

# Настройки FTP
FTP_HOST = 'ftp.example.com'
FTP_USER = 'username'
FTP_PASS = 'password'
FTP_DIRECTORY = '/test'
FTP_FILE = 'test.zip'

# Целевая папка для распаковки
TARGET_DIRECTORY = '/path/to/target/directory'

def download_and_extract_zip():
    # Подключение к FTP-серверу
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(FTP_DIRECTORY)

    # Загрузка архива
    file = open(FTP_FILE, 'wb')
    ftp.retrbinary(f'RETR {FTP_FILE}', file.write)

    # Распаковка архива
    shutil.unpack_archive(FTP_FILE, TARGET_DIRECTORY)

    # Удаление локального файла
    os.remove(FTP_FILE)

    print('Архив успешно загружен и распакован.')

if __name__ == '__main__':
    download_and_extract_zip()
