import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

pattern = re.compile(
    r"(?P<ip>\d+.\d+.\d+.\d+) - - \[.+] \"(?P<req>.+) (?P<url>.+)"
    r" HTTP/1\.\d\" (?P<code>\d+) (?P<size>\d*)")


@dataclass
class ParseOptions:
    path: str
    json: str


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Path to log file", default='access.log')
    parser.add_argument("--json", help="Save to json file", action="store_true")
    args = parser.parse_args()
    option = ParseOptions(path=args.path, json=args.json)

    return option


options = get_args()


def count_requests():
    """
    Количество запросов по типу, например: GET - 20, POST - 10
    :return: list
    """
    type_method = []
    with Path(options.path).open('r', encoding="utf-8") as f:
        for line in f:
            result = pattern.search(line)
            if result:
                type_method.append(result.group("req"))
    type_method = [(i, type_method.count(i)) for i in set(type_method)]

    return type_method


def get_url():
    """
    Топ 10 самых частых запросов
    :return: list
    """
    urls = []
    with Path(options.path).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer:
                urls.append(answer.group("url"))
    urls = [(i, urls.count(i)) for i in set(urls)]
    urls = sorted(urls, key=lambda x: x[1])[-10:]

    return urls


def get_4xx_status_code():
    """
    Топ 5 самых больших по размеру запросов,
    которые завершились клиентской (4ХХ) ошибкой
    :return: list
    """
    urls_list = []
    with Path(options.path).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer and re.match(r"4\d{2}", answer.group("code")):
                urls_list.append([answer.group("url"),
                                  answer.group("code"),
                                  int(answer.group("size")),
                                  answer.group("ip")])
    urls_list = sorted(urls_list, key=lambda x: x[2])[-5:]

    return urls_list


def get_5xx_status_code():
    """
    Топ 5 пользователей по количеству запросов,
    которые завершились серверной (5ХХ) ошибкой
    :return: list
    """
    urls_list = []
    with Path(options.path).open('r', encoding="utf-8") as file:
        for line in file:
            answer = pattern.search(line)
            if answer and re.match(r"5\d{2}", answer.group("code")):
                urls_list.append(answer.group("ip"))
    urls_list = [(i, urls_list.count(i)) for i in set(urls_list)]
    urls_list = sorted(urls_list, key=lambda x: x[1])[-5:]

    return urls_list


data = {
    'top_requests': {x[0]: x[1] for x in count_requests()},
    'requests': {x[0]: x[1] for x in get_url()},
    'requests_status_code_4XX': [x for x in get_4xx_status_code()],
    'ip_status_code_5XX': {x[0]: x[1] for x in get_5xx_status_code()}
}


def parse_json(data: dict):
    with open('file.json', 'w') as f:
        json.dump(data, f, indent=3)


if options.json:
    parse_json(data)
    print("json file is created")
else:
    with open("file.txt", 'w') as f:
        print(data)
        f.write(str(data))
