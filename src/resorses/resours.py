import os, glob
from datetime import datetime


def built_report():
    onlyfiles = glob.glob('/*/f1 flask/src/files/*')
    with open(onlyfiles[0], 'r') as abb_file:
        abb_dict = {line[:3]: list(line[3:].strip('\n').strip('_').split('_')) for line in abb_file}

    with open(onlyfiles[1], 'r') as end_file:
        end_dict = {line[:3]: line[3:].strip() for line in end_file}

    with open(onlyfiles[2], 'r') as start_file:
        start_dict = {line[:3]: line[3:].strip() for line in start_file}

    time_lap = {}
    format = ('%Y-%m-%d_%H:%M:%S.%f')
    for key in start_dict:
        if key in end_dict:
            start = datetime.strptime(start_dict[key], format)
            end = datetime.strptime(end_dict[key], format)
            r = end - start
            if start > end:
                time_lap[key] = 'DNF'
            else:
                time_lap[key] = str(r)[2:-3]

    time_lap = dict(sorted(time_lap.items(), key=lambda item: item[1]))

    report = {}
    for key, value in time_lap.items():
        if key in abb_dict.keys():
            report[key] = {'name': abb_dict[key][0],
                           'team': abb_dict[key][1],
                           'time': value}

    return report


def page_driver():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '/Python/API report/src/links/links.txt')
    full_path = os.path.join(dirname, '/Python/API report/src/files/abbreviations.txt')
    with open(full_path, 'r') as abb_file:
        abb_dict = {line[:3]: line[3:].strip('\n').strip('_').split('_') for line in abb_file}

    data = {}
    with open(path, 'r') as link_file:
        for k, v in abb_dict.items():
            data[k] = {'name': v[0],
                       'team': v[1],
                       'link': link_file.readline().strip('\n'), }

    return data



