#! /usr/bin/python
import sys
import re


def find_abbreviations(file_path: str) -> list:
    """ Finding abbreviations in text file using regex.

    :param file_path: str, path to required file
    :return: list with found abbreviations
    """

    regex = re.compile(r'([А-ЯЁ]{2,}[ |\n[А-ЯЁ]{2,}]*?)\b')
    result = list()

    with open(file_path, encoding='utf-8') as f:
        for line in f:
            abbrev_list = re.findall(regex, line)
            if abbrev_list:
                result.extend(abbrev_list)

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Path to file was not passes as command line argument")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    result = find_abbreviations(file_path)
    for abbrev in result:
        print(abbrev.strip())
