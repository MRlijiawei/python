def print_dic(dic):
    f=open(r'f:/testcode/python/wordAnalyse/test/result_no_repeat_hot.txt','w')

    for k,v in dic.iteritems():
       if len(v)>=1:
        for i in v:
            f.write(k+'\t'+i+'\n')