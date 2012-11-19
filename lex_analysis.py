import sys
import os
import re
import variable
from consts import *

def lex_analysis(data_file):
    f = open(data_file)
    if not f:
        print 'do not have the file'
        return
    
    urls = list()
    for url in f:
        url = url.rstrip()
        if url[-1] == '/':
            url = url[:-1]

        urlmatch = re.search(r'(//)', url)
        if urlmatch and urlmatch.lastindex == 1:
            url = url.split(r'//')[1]

        url = url.split(r'/')
        url[0] = url[0].split(r'.')
        urls.append(url)
    return urls

def mapping(urls):
    variable.word_to_number = dict()
    variable.word_to_number['.'] = 2
    variable.word_to_number['/'] = 3
    max_map_number = 4
    for url in urls:
        for domain in url[0]:
            if not variable.word_to_number.has_key(domain):
                variable.word_to_number[domain] = max_map_number
                max_map_number += 1
    for url in urls:
        for directory in url[1:]:
            if not variable.word_to_number.has_key(directory):
                variable.word_to_number[directory] = max_map_number
                max_map_number += 1
    return max_map_number

def init_need_deal(urls):
    variable.need_deal = list()
    for i in range(len(urls)):
        if not urls[i]:
            return False
        for domain in urls[i][0]:
            variable.need_deal.append((variable.word_to_number[domain], i))
            variable.need_deal.append((SIGN_DOT_TO_NUMBER, i))
        for j in range(1, len(urls[i])):
            variable.need_deal.append((variable.word_to_number[urls[i][j]], i))
        variable.need_deal.append((SIGN_SPLIT_TO_NUMBER, -1))
    return len(variable.need_deal)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'error argv, we need data_file and up_number'
    else:
        urls = lex_analysis(sys.argv[1])
        max_map_number = mapping(urls)
        init_need_deal(urls)
        print variable.need_deal
        print variable.word_to_number
        print max_map_number
