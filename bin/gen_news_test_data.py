#!/usr/bin/env python
#-*-conding:utf-8
"created by darrenan 2014:20:07"

import os
import sys
from numpy import *

def main():
    infp = file(sys.argv[1])
    trainfp = file(sys.argv[2],"w")
    testfp = file(sys.argv[3],"w")

    news_list = infp.readlines()
    test_size = int(len(news_list) * 0.2)

    print len(news_list)
    print test_size


    test_list = []
    for i in range(test_size):
        randomIndex = int(random.uniform(0,len(news_list)))
        test_list.append(news_list[randomIndex])
        del(news_list[randomIndex])
    print "###"
    print len(news_list)
    print len(test_list)
    for item in news_list:
        print >> trainfp,item.strip()
    for item in test_list:
        print >>testfp,item.strip()
    infp.close()
    trainfp.close()
    testfp.close()
if __name__ == '__main__':
    main()
