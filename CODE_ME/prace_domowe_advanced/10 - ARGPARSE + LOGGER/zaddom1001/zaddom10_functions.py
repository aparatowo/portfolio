import logging

logger = logging.getLogger('wc_logger')


def count_lines(s):
    logger.debug('wywołano funkcję "count_lines()"')
    return len(s.split('\n'))


def count_words(s):
    logger.debug('wywołano funkcję "count_words()"')
    return sum([len(x.split()) for x in s.split('\n')])


def count_bytes(s):
    logger.debug('wywołano funkcję "count_bytes()"')
    return len(s.encode())


def set_logger(log_level):
    logger.setLevel(log_level)


def read_file_contents(f):
    file_content = f.read()
    return file_content


def open_file(filename):
    try:
        with open(filename) as f:
            logger.info(f'otwarto plik {filename}')
            file_content = read_file_contents(f)
    except FileNotFoundError:
        logger.warning(f'nie znaleziono pliku {filename}')
        exit()
    return file_content


def wc(filename, template):
    file_content = open_file(filename)

    szablony = {'full': '{lines} {words} {bytes} {filename}',
                'lines': '{lines} {filename}',
                'words': '{words} {filename}',
                'bytes': '{bytes} {filename}'}

    logger.info('wybrano szablon pełny')
    szablon = szablony[template]

    result = szablon.format(lines=count_lines(file_content),
                            words=count_words(file_content),
                            bytes=count_bytes(file_content),
                            filename=filename)

    return result
