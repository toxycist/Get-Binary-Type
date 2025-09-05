import os

directory_path = "./binaries"
file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path)]

MAGIC_NUMBERS = {
    "504B0304": "ZIP Archive / Microsoft Word (New) / Microsoft Excel (New)",
    "89504E470D0A1A0A": "PNG Image",
    "FFD8FF": "JPEG Image",
    "474946383961": "GIF Image",
    "424D": "BMP Image",
    "49492A00": "TIFF Image (Little Endian)",
    "4D4D002A": "TIFF Image (Big Endian)",
    "255044462D": "PDF Document",
    "494433": "MP3 Audio",
    "52494646": "WAV Audio / AVI Video (starts with RIFF)",
    "664C6143": "FLAC Audio",
    "0000001866747970": "MP4 Video",
    "0000001466747970": "MOV (QuickTime)",
    "4D5A": "EXE (Windows Executable)",
    "7F454C46": "ELF (Executable and Linkable Format)",
    "7573746172": "Tar Archive",
    "1F8B": "GZ Archive",
    "52617221": "RAR Archive",
    "00014243": "ISO (CD/DVD Image)",
    "53514C6974652066697468646266": "SQLite Database",
    "4C00000001140200": "Windows Shortcut (LNK)",
    "D0CF11E0A1B11AE1": "Microsoft Word (Old) / Microsoft Excel (Old)",
    "38425053": "Adobe Photoshop (PSD)",
}

sorted_magic_numbers = dict(sorted(MAGIC_NUMBERS.items(), key=lambda x: len(x[0]), reverse=True))

def get_filetype(file_path):
    with open(file_path, 'rb') as file:
        content = file.read(28)
        for magic_number, filetype in sorted_magic_numbers.items():
            if content.hex().upper().startswith(magic_number):
                return filetype
        return "Unknown file type"

for file_path in file_paths:
    print(f"{file_path}: {get_filetype(file_path)}")