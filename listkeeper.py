#! /usr/bin/python
import sys


def process_file(file_path: str) -> list:
    """ Reading required file with users data

    Reading file and creating unique username for every user.

    :param file_path: str, path to file with users data
    :return: list, updated users data with created usernames
    """

    created_usernames = set()
    records = list()

    with open(file_path, encoding='utf-8') as f:
        for line in f:
            user_data = line.split(':')
            user_data = {'id': user_data[0], 'first_name': user_data[1], 'patronymic': user_data[2], 'last_name': user_data[3],
                 'department': user_data[4].strip()}

            username = generate_username(user_data, created_usernames)

            records.append(
                (f"{user_data['last_name']}, {user_data['first_name']} {user_data['patronymic']}", user_data['id'], username))

    return sorted(records)


def generate_username(user_data: dict, created_usernames: set, max_first_name_letters: int=3, max_patronymic_letters: int=3) -> str:
    """Generating unique username, based on user's first and last name

    :param user_data: dict, main user data
    :param created_usernames: set with already existing usernames
    :param max_first_name_letters: int, max number of first letters of user's first name needed to create unique username
    :param max_patronymic_letters: int, max number of first letters of user's patronymic needed to create unique username
    :return: str, created username
    """

    first_name_letters = 1
    patronymic_letters = 1

    while True:
        username = f"{user_data['first_name'][0:first_name_letters]}{user_data['patronymic'][0:patronymic_letters] if user_data['patronymic'] else ''}{user_data['last_name']}"
        if username not in created_usernames:
            created_usernames.add(username)
            break

        if first_name_letters < max_first_name_letters:
            first_name_letters += 1
        elif patronymic_letters < max_patronymic_letters:
            patronymic_letters += 1
        else:
            username += str(user_data['id'])
            break

    return username


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Path to file was not passes as command line argument")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    result = process_file(file_path)
    print("{0:<30}{1:<5}{2}".format("Name", "ID", "Username"))
    for line in result:
        print("{0:<30}{1:<5}{2}".format(line[0], line[1], line[2]))
