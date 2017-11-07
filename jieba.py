# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:20:11 2016

@author: xiao
"""

#encoding=utf-8
import jieba

def WordSeg(Inputfile, Outputfile):
    f = file(Inputfile)
    w = file(Outputfile, 'w')
    for line in f:
        line = line.strip().decode('utf-8')
        seg_list = jieba.cut(line,cut_all=False)
        writeline = ''
        for key in seg_list:
            writeline = writeline + key + '  '
        writeline = writeline.strip('  ')
        w.write(writeline.encode('utf-8') + '\n')
   # print "Full Mode:", "/ ".join(seg_list) #全模式
        
if __name__ == "__main__":
    Inputfile = "test"
    Outputfile = "answer1.txt"
    #seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    WordSeg(Inputfile, Outputfile)
    