import subprocess
import schedule
import time
import os


def start_program(program_path):
    program_name = os.path.basename(program_path)
    try:
        subprocess.Popen([program_path])
        print(f"{program_name} запущен.")
    except Exception as e:
        print(f"Ошибка при запуске {program_name}: {e}")

def stop_program(program_path):
    program_name = os.path.basename(program_path)
    try:
        subprocess.Popen(["taskkill", "/f", "/im", program_name])
        print(f"{program_name} завершен.")
    except Exception as e:
        print(f"Ошибка при завершении {program_name}: {e}")

#Название процесса БЕЗ кавычек!!!
program_path = input("Введите путь к исполняемому файлу: ")

# Запустить программу каждый день в 04:07
schedule.every().day.at("04:07").do(start_program, program_path)

# Завершить программу каждый день в 04:08
schedule.every().day.at("04:08").do(stop_program, program_path)

while True:
    schedule.run_pending()
    time.sleep(1)