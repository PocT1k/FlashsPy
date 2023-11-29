from utilities import format_flash_drive, move_video_to_flash_drive, safely_eject_flash_drive


def main():
    flash_drive_letter = "H"  # input('Введите букву флешки (например, H): ')
    video_path = f"F:\\Backups and saves\\ИНГРУП\\forWrite\\Af21okt\\Аргон Много адресов.mp4" #input('Введите путь к видеофайлу: ')

    #format_flash_drive(flash_drive_letter)
    #move_video_to_flash_drive(video_path, flash_drive_letter)
    safely_eject_flash_drive(flash_drive_letter)

if __name__ == "__main__":
    main()
