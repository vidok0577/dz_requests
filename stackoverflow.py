import requests
import time
from progress.bar import Bar

def stack_question():
    time_2_day = int(time.time()) - 86400 * 2
    has_more = True
    number_page = 1
    counter = 0
    list_questions = []
    bar = Bar('Processing', max=20)
    while has_more:
        url = 'https://api.stackexchange.com/2.3/search?'
        params = {'page': number_page, 'pagesize': '100', 'fromdate': time_2_day, 'order': 'desc', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
        data = requests.get(url, params=params).json()
        list_questions = list_questions + ([q['question_id'] for q in data['items']])
        counter += len(data['items'])
        number_page += 1
        has_more = data['has_more']
        time.sleep(3)
        bar.next()

    bar.finish()
    print('Количество вопросов с тэгом python:', counter)
    print('Лимит, запросов осталось:', data['quota_remaining'])
    return list_questions

if __name__ == '__main__':
    with open('result.txt', 'w', encoding='utf8') as f:
        print(*(stack_question()), file=f, sep='\n')