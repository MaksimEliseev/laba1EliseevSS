import ctypes
import os
import platform
import datetime

def get_computer_name():
    buffer = ctypes.create_unicode_buffer(1024)
    size = ctypes.c_ulong(len(buffer))
    if ctypes.windll.kernel32.GetComputerNameW(buffer, ctypes.byref(size)):
        return buffer.value
    return "Unknown"

def get_user_name():
    buffer = ctypes.create_unicode_buffer(1024)
    size = ctypes.c_ulong(len(buffer))
    if ctypes.windll.advapi32.GetUserNameW(buffer, ctypes.byref(size)):
        return buffer.value
    return "Unknown"

def get_windows_directory():
    buffer = ctypes.create_unicode_buffer(1024)
    if ctypes.windll.kernel32.GetWindowsDirectoryW(buffer, len(buffer)):
        return buffer.value
    return "Unknown"

def get_os_version():
    return platform.version()

def get_screen_resolution():
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    return f"{width}x{height}"

def get_current_date_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print(f"Имя компьютера: {get_computer_name()}")
    print(f"Имя пользователя: {get_user_name()}")
    print(f"Системная директория: {get_windows_directory()}")
    print(f"Версия ОС: {get_os_version()}")
    print(f"Разрешение монитора: {get_screen_resolution()}")
    print(f"Текущая дата и время: {get_current_date_time()}")

if __name__ == "__main__":
    main()