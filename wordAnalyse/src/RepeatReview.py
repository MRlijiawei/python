
import csv

def Find_LastReview():

     fr = open(r'/Users\Administrator\Desktop\News-Recommend-System-master1\test/train_date_set1.txt')
     f=open(r'/Users\Administrator\Desktop\News-Recommend-System-master1\test/test.csv','w')
     dic={}

     for line in fr.readlines():
        # line.strip().split('\t')
         dic[line.strip().split('\t')[0]]=line.strip().split('\t')[1]+'\t'+line.strip().split('\t')[2]+'\t'+line.strip().split('\t')[3]+'\t'+line.strip().split('\t')[4]

     for key in dic:
         print key,dic[key]
         f.write(key+'\t'+dic[key]+'\n')
if __name__=='__main__':
    Find_LastReview()