'''
    This function transforms original dataset by:
    * removing emojis, urls, hashtags
    * changing real user ids to virtual ones
    * saving time, virtual id, cleaned text only
    
    src: the original dataset from social platform (csv format)
    dst: the output dataset after preprocessing (csv format)
'''
import csv
import codecs
import re
import copy
import click
#remove emojis
def clean(desstr,restr=''):   
    try:  
        co = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55 \U00010000-\U0010ffff]+')  
    except re.error:  
        co = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u2B55 \U00010000-\U0010ffff])+')  
    return co.sub(restr, desstr)
@click.command()
@click.option('--src', 'source_csv', help='source csv file', required=True)
@click.option('--dst', 'output_csv', help='output csv file', required=True)
def preprocess(
    source_csv: str,
    output_csv: str
):
    csvfile = open(output_csv, mode='w', encoding='utf-8-sig', newline='')
    fieldnames = ['user_id', 'time', 'cleaned_text']
    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    write.writeheader()
    num = 0
    numid = 0
    idlist = {}
    with codecs.open(source_csv, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            tx = copy.copy(row['text'])
            if row['hashtags']==None:
                continue
            atlist = row['hashtags'].split(' ')
            for atp in atlist:
                if atp!='':
                    tx = re.sub('#'+atp, '', tx)
            if row['urls']==None:
                continue
            atlist = row['urls'].split(' ')
            for atp in atlist:
                if atp!='':
                    tx = re.sub(atp, '', tx)
            tx = re.sub(' +', ' ', tx)
            if row['user_id'] not in idlist:
                numid += 1
                idlist[row['user_id']] = numid
            if row['cleaned_text'] == '':
                continue
            if row['cleaned_text'] == None:
                continue
            num += 1
            write.writerow({'user_id': idlist[row['user_id']], 'time': row['created_at'], 'cleaned_text': clean(tx)})
    csvfile.close()
if __name__ == "__main__":
    preprocess()