'''
    This function calculate cosine similarity between tweets and given psychology terms in ItemList.
    
    src: csv file after preprocess function (csv format)
    dst: cosine similarity output. Each column is named by FactorList (csv format)
    ItemList: Psychology terms need calculating
    FactorList: Column name in the final file
'''
import sys
from text2vec import Similarity
import codecs
import csv
import click
# Two lists of sentences
ItemList = ['Right now, I am in awe.',
             'Right now, I am amazed.',
             'I am looking at breathtaking scenes.',
             'Right now, I am amused.',
             'I am watching something funny.',
             'I feel that there are only me and the scenes left.',
             'I forget the people and things around me.',
             'I feel I am the only person in the world.',
             'I feel lacking companionship.',
             'I miss having people around me.',
             'I feel that there are only me and the scenes left, but I do not feel lonely.',
             'I forget the people and things around me, and I do not miss them.',
             'I feel I am the only person in the world, but I do not feel empty.',
             'I am feeling alone, but I do not feel lonely.',
             'I enjoy being alone.',
             'I think being alone is meaningful to me.',
             'I think being alone is valuable to me.']
FactorList = ['Awe1', 'Awe2', 'Awe3', 'Amuse1', 'Amuse2', 'Alone1', 'Alone2', 'Alone3', 'Loneliness1', 'Loneliness2', 'AloneNotLonely1', 'AloneNotLonely2', 'AloneNotLonely3', 'AloneNotLonely4', 'Attitude1', 'Attitude2', 'Attitude3']
sim_model = Similarity()
def match_sentences(src, embx):
    tmp = {}
    res = sim_model.get_enc(src, embx)
    for i in range(len(ItemList)):
        tmp[FactorList[i]] = res[i]
    return tmp
@click.command()
@click.option('--src', 'source_csv', help='source csv file', multiple=True, required=True)
@click.option('--dst', 'output_csv', help='output csv file', required=True)
def calculate_similarity(
    source_csv,
    output_csv: str
):
    csvfile = open(output_csv, mode='w', newline='', encoding='utf-8-sig')
    fieldnames = ['UserId', 'Date', 'WordCount'] + FactorList
    for i in range(len(ItemList)):
        fieldnames.append(str(i))
    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    write.writeheader()
    num = 0
    avr = {}
    emb = sim_model.get_emb(ItemList)
    for sx in source_csv:
        with codecs.open(sx, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f, skipinitialspace=True):
                if row['cleaned_text'] == '':
                    continue
                if row['cleaned_text'] == None:
                    continue
                num += 1
                avr = match_sentences(row['cleaned_text'], emb)
                avr['UserId'] = row['user_id']
                avr['Date'] = row['time']
                tmp = row['cleaned_text'].split(' ')
                avr['WordCount'] = len(tmp)-tmp.count('')
                write.writerow(avr)
                if num%1000==0:
                    print(num)
    csvfile.close()
if __name__ == "__main__":
    calculate_similarity()
