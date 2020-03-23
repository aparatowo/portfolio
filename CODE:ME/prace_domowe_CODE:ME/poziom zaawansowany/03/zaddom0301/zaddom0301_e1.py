# Rafał Nitychoruk


def strip_extensions(files):
    list_of_files = [file.split('.', 1)[0] for file in files if file != None ]
    return list_of_files


if __name__ == '__main__':
    files = ['spreadsheet.xlsx', 'music.mp3', 'backup.log', None, 'temp', 'archive.tar.gz']

    print(strip_extensions(files))
