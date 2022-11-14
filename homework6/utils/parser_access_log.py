import re
from pathlib import Path

pattern = re.compile(
    r"(?P<ip>\d+.\d+.\d+.\d+) - - \[.+] \"(?P<req>.+) (?P<url>.+)"
    r" HTTP/1\.\d\" (?P<code>\d+) (?P<count>\d*)")


def count_requests(path_to_file: str):
    """
    Количество запросов по типу, например: GET - 20, POST - 10
    :return: list
    """
    type_method = []
    with Path(path_to_file).open('r', encoding="utf-8") as f:
        for line in f:
            result = pattern.search(line)
            if result:
                type_method.append(result.group("req"))
    type_method = [(i, type_method.count(i)) for i in set(type_method)]

    return type_method


def get_url(path_to_file: str):
    """
    Топ 10 самых частых запросов
    :return: list
    """
    urls = []
    with Path(path_to_file).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer:
                urls.append(answer.group("url"))
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])[-10:]

    return urls


def get_4xx_status_code(path_to_file: str):
    """
    Топ 5 самых больших по размеру запросов,
    которые завершились клиентской (4ХХ) ошибкой
    :return: list
    """
    urls_list = []
    with Path(path_to_file).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer and re.match(r"4\d{2}", answer.group("code")):
                urls_list.append([answer.group("url"),
                                  answer.group("code"),
                                  int(answer.group("count")),
                                  answer.group("ip")])
    urls_list = sorted(urls_list, key=lambda x: x[2])[-5:]

    return urls_list


def get_5xx_status_code(path_to_file: str):
    """
    Топ 5 пользователей по количеству запросов,
    которые завершились серверной (5ХХ) ошибкой
    :return: list
    """
    urls_list = []
    with Path(path_to_file).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer and re.match(r"5\d{2}", answer.group("code")):
                urls_list.append(answer.group("ip"))
    urls_list = [(i, urls_list.count(i)) for i in set(urls_list)]
    urls_list = sorted(urls_list, key=lambda x: x[1])[-5:]

    return urls_list
