import os
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_file(file_path, target_directory):
    """
    Копіює файл до цільової директорії, сортує його за розширенням.
    """
    ext = file_path.suffix.lstrip('.').lower()  # Отримуємо розширення файлу
    if not ext:  # Пропускаємо файли без розширення
        return

    # Створюємо папку для даного розширення
    ext_dir = target_directory / ext
    ext_dir.mkdir(parents=True, exist_ok=True)

    # Копіюємо файл до відповідної папки
    shutil.copy(file_path, ext_dir / file_path.name)


def process_directory(source_directory, target_directory, pool):
    """
    Рекурсивно обходить директорію та викликає копіювання файлів у потоках.
    """
    for item in source_directory.iterdir():
        if item.is_dir():
            # Передаємо обробку підкаталогів у пул потоків
            pool.submit(process_directory, item, target_directory, pool)
        elif item.is_file():
            # Копіюємо файли у відповідний підкаталог
            pool.submit(copy_file, item, target_directory)


def main():
    """
    Основна функція для запуску програми.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<target_directory>]")
        sys.exit(1)

    # Отримуємо шляхи до джерельної та цільової директорії
    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Source directory '{source_dir}' does not exist or is not a directory.")
        sys.exit(1)

    # Створюємо цільову директорію, якщо її ще немає
    target_dir.mkdir(parents=True, exist_ok=True)

    # Створюємо пул потоків
    with ThreadPoolExecutor() as pool:
        process_directory(source_dir, target_dir, pool)

    print(f"Files have been sorted and copied to '{target_dir}'")


if __name__ == "__main__":
    main()
