import sys
import os
import variable
from lex_analysis import *
from suffix_array import deal_suffix, init_father, make_group

def suffix_array(urls, up_number):
    max_map_number = mapping(urls)
    len_of_need_deal = init_need_deal(urls)

    deal_suffix(len_of_need_deal, max_map_number + 1)
    init_father(urls)
    result = make_group(up_number)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'error argv, we need data_file and up_number'
    else:
        urls = lex_analysis(sys.argv[1])
        max_map_number = mapping(urls)
        len_of_need_deal = init_need_deal(urls)
        #print variable.need_deal
        #print variable.word_to_number
        print max_map_number

        deal_suffix(len_of_need_deal, max_map_number + 1)
        init_father(urls)
        result = make_group(int(sys.argv[2]))

        for group in result:
            for url_num in group:
                a = 1
                print urls[url_num],
                print url_num
            print '##################################\n'

        #print len(result)

        #print variable.rank
        #print variable.sa
        #print variable.highet

