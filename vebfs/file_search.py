import os
import fnmatch
import re

def find_files(directory, pattern="*", recursive=True):
    """Ищет файлы в директории по шаблону (с поддержкой wildcard).
    
    Параметры:
    - directory: путь к директории для поиска.
    - pattern: шаблон для поиска (по умолчанию все файлы).
    - recursive: если True, ищет рекурсивно в подкаталогах (по умолчанию True).
    
    Возвращает:
    - список путей к файлам, соответствующим шаблону.
    """
    matched_files = []
    for root, dirs, files in os.walk(directory):
        # Если не нужно искать рекурсивно, ограничиваем поиск текущей директорией
        if not recursive and root != directory:
            continue
        for filename in fnmatch.filter(files, pattern):
            matched_files.append(os.path.join(root, filename))
    return matched_files

def find_directories(directory, pattern="*", recursive=True):
    """Ищет директории в директории по шаблону (с поддержкой wildcard).
    
    Параметры:
    - directory: путь к директории для поиска.
    - pattern: шаблон для поиска (по умолчанию все директории).
    - recursive: если True, ищет рекурсивно в подкаталогах (по умолчанию True).
    
    Возвращает:
    - список путей к директориям, соответствующим шаблону.
    """
    matched_dirs = []
    for root, dirs, files in os.walk(directory):
        # Если не нужно искать рекурсивно, ограничиваем поиск текущей директорией
        if not recursive and root != directory:
            continue
        for dirname in fnmatch.filter(dirs, pattern):
            matched_dirs.append(os.path.join(root, dirname))
    return matched_dirs

def find_files_regex(directory, regex):
    """Ищет файлы в директории по регулярному выражению.
    
    Параметры:
    - directory: путь к директории для поиска.
    - regex: регулярное выражение для поиска.
    
    Возвращает:
    - список путей к файлам, соответствующим регулярному выражению.
    """
    matched_files = []
    pattern = re.compile(regex)
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if pattern.match(filename):
                matched_files.append(os.path.join(root, filename))
    return matched_files

def find_directories_regex(directory, regex):
    """Ищет директории в директории по регулярному выражению.
    
    Параметры:
    - directory: путь к директории для поиска.
    - regex: регулярное выражение для поиска.
    
    Возвращает:
    - список путей к директориям, соответствующим регулярному выражению.
    """
    matched_dirs = []
    pattern = re.compile(regex)
    for root, dirs, files in os.walk(directory):
        for dirname in dirs:
            if pattern.match(dirname):
                matched_dirs.append(os.path.join(root, dirname))
    return matched_dirs
