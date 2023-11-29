import subprocess #py for external (terminal) commands
import shutil #py files and directories
import win32file
import win32con


def format_flash_drive(flash_drive_letter):
    print(f'\nДиск {flash_drive_letter}: начало работы.')
    try: # Форматируем флешку в FAT32
        format_command = f'format {flash_drive_letter}: /FS:FAT32 /Q /V:USB_INGROUP'
        subprocess.run(format_command, shell=True)

        print(f'Флешка {flash_drive_letter}: успешно отформатирована в FAT32.')
    except Exception as e:
        print(f'Произошла ошибка при форматировании флешки: {str(e)}')

def move_video_to_flash_drive(video_path, flash_drive_letter):
    print(f'\nПеремещение видео на флешку {flash_drive_letter}:')
    try:
        destination_path = f"{flash_drive_letter}://video.mp4"
        shutil.copy(video_path, destination_path)

        print(f'Видео успешно перемещено на флешку {flash_drive_letter}')
    except Exception as e:
        print(f'Произошла ошибка при перемещении видео: {str(e)}')

# def safely_eject_flash_drive(flash_drive_letter):
#     print(f'\nИзвлечение флешки {flash_drive_letter}:')
#     # Проверяем, существует ли устройство с указанной буквой диска
#     drive_path = f'\\\\.\\{flash_drive_letter}:'
#     drive_type = win32file.GetDriveType(drive_path)
#
#     if drive_type == win32con.DRIVE_REMOVABLE:
#         # Извлекаем флешку
#         win32file.DeviceIoControl(win32file.CreateFile(
#             drive_path, win32file.GENERIC_READ, win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE, None,
#             win32file.OPEN_EXISTING, 0, None), win32con.FSCTL_DISMOUNT_VOLUME, None, 0, None)
#         print(f'Флешка {flash_drive_letter}: безопасно извлечена.')
#     else:
#         print(f'Флешка {flash_drive_letter}: не является съемным устройством.')

def eject_flash_drive(drive_letter):
    # Check if the drive letter exists and is a removable drive
    drive_path = f'{drive_letter}:\\'
    if os.path.exists(drive_path) and os.path.ismount(drive_path):
        # Eject the drive using ctypes
        ctypes.windll.kernel32.WinExec(f'RunDll32.exe shell32.dll,Control_RunDLL hotplug.dll,{drive_path}')
        print(f'Flash drive {drive_letter} safely ejected.')
    else:
        print(f'Flash drive {drive_letter} not found or is not a removable drive.')
