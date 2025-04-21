import os
from vebfs import (
    copy_file, move_file, delete_file, delete_directory,
    create_backup, get_file_size, list_all_files, ensure_directory_exists,
    find_files, find_directories
)

# Подготовка
if not os.path.exists("example.txt"):
    with open("example.txt", "w") as f:
        f.write("Hello from vebfs!")

# Основные действия
copy_file("example.txt", "copy_example.txt")
move_file("copy_example.txt", "moved_example.txt")
create_backup("moved_example.txt", "backup_example.txt")

size = get_file_size("backup_example.txt")
print(f"Размер файла: {size} байт")

delete_file("moved_example.txt")

# Удалим папку, но сначала создадим её
if not os.path.exists("old_folder"):
    os.makedirs("old_folder")
delete_directory("old_folder", recursive=True)

# Создадим и гарантируем существование другой папки
ensure_directory_exists("logs")

# Поиск файлов и директорий
print("Все .txt файлы:", find_files(".", "*.txt"))
print("Все директории с 'log':", find_directories(".", "log*"))
