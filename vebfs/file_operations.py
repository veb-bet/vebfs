import os
import shutil
import logging
import fnmatch

logging.basicConfig(level=logging.INFO)

# Копирует файл из исходного пути в целевой
def copy_file(src, dest):
    """Копирует файл из исходного пути в целевой."""
    if not os.path.exists(src):
        raise FileNotFoundError(f"Файл не найден: {src}")
    shutil.copy2(src, dest)
    logging.info(f"Копирован файл: {src} → {dest}")

# Перемещает файл из исходного пути в целевой
def move_file(src, dest):
    """Перемещает файл из исходного пути в целевой."""
    if not os.path.exists(src):
        raise FileNotFoundError(f"Файл не найден: {src}")
    shutil.move(src, dest)
    logging.info(f"Файл перемещен: {src} → {dest}")

# Удаляет файл по указанному пути
def delete_file(file_path):
    """Удаляет файл по указанному пути."""
    if os.path.exists(file_path):
        os.remove(file_path)
        logging.info(f"Удалён файл: {file_path}")
    else:
        raise FileNotFoundError(f"Файл не найден: {file_path}")

# Удаляет директорию. При recursive=True — удаляет вместе с содержимым
def delete_directory(directory_path, recursive=False):
    """Удаляет директорию. При recursive=True — удаляет вместе с содержимым."""
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        if recursive:
            shutil.rmtree(directory_path)
            logging.info(f"Рекурсивно удалена директория: {directory_path}")
        else:
            os.rmdir(directory_path)
            logging.info(f"Удалена пустая директория: {directory_path}")
    else:
        raise FileNotFoundError(f"Директория не найдена: {directory_path}")

# Создает резервную копию файла
def create_backup(file_path, backup_path):
    """Создает резервную копию файла."""
    if os.path.exists(file_path):
        shutil.copy2(file_path, backup_path)
        logging.info(f"Создана резервная копия: {file_path} → {backup_path}")
    else:
        raise FileNotFoundError(f"Файл не найден: {file_path}")

# Возвращает размер файла в байтах
def get_file_size(path):
    """Возвращает размер файла в байтах."""
    if os.path.exists(path):
        return os.path.getsize(path)
    else:
        raise FileNotFoundError(f"Файл не найден: {path}")

# Возвращает список всех файлов в директории и поддиректориях
def list_all_files(directory):
    """Возвращает список всех файлов в директории и поддиректориях."""
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

# Создаёт директорию, если она не существует
def ensure_directory_exists(path):
    """Создаёт директорию, если она не существует."""
    os.makedirs(path, exist_ok=True)
    logging.info(f"Директория гарантирована: {path}")

# Проверка существования файла или директории
def check_exists(path):
    """Проверяет, существует ли файл или директория по указанному пути."""
    if os.path.exists(path):
        return True
    return False
