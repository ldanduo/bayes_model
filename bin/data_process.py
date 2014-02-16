#!/usr/bin/python
#-*-coding:utf-8
"created by darrenan 2014:20:07"

import sys
import pdb
import re

sw_dict = {}


BREAK_RE=re.compile("“|”|\"|《|》|？|。|!|！|。|,|,|【|】|（|）|\|：|、|:|[|]|；|;")
def process_line(str_input):
    str_out = str_input
    str_out = BREAK_RE.sub("",str_out)
    return str_out

def load_dict(sw_file):
    infp = file(sw_file)
    for line in infp:
        sw_dict[line.strip()] = 1
    infp.close()
def process_file(input_file,output_file):
    #pdb.set_trace()
    infp = file(input_file)
    outfp = file(output_file,"w")
    for line in infp:
        tmp_list = []
        line = process_line(line)
        line = line.strip()
        array = line.split("\t")
        if len(array) != 2:
            print >> sys.stderr," len(array) not equal 2"
        subarray = array[0].split(" ")
        for word in subarray:
            word = word.strip()
            word_unicode = word.decode("utf-8","ignore")
            if len(word_unicode) ==1:
                continue
            if word in sw_dict:
                continue
            if word == "" or word == ' ':
                continue
            tmp_list.append(word.strip())
        print >> outfp,"%s\t%s" % (" ".join(tmp_list),array[1])

    infp.close()
    outfp.close()
if __name__ == '__main__':
    load_dict("./stop_words.txt_utf8")
    process_file("data.txt","data_rm_sw.txt")


