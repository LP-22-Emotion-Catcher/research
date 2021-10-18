import pandas as pd


def making_dataset(filename='kartaslovsent.csv'):
    words_df = pd.read_csv(filename, encoding = 'utf-8', sep=';')
    words_df = words_df[['term', 'tag', 'pstv', 'ngtv', 'neut']]

    negative_words = words_df[words_df['tag'] == 'NGTV']
    negative_words = negative_words.sort_values(by='ngtv', ascending = False)
    positive_words = words_df[words_df['tag'] == 'PSTV']
    positive_words = positive_words.sort_values(by='pstv', ascending = False)
    neutral_words = words_df[words_df['tag'] == 'NEUT']
    neutral_words = neutral_words.sort_values(by='neut', ascending = False)

    return negative_words, positive_words, neutral_words

negative_words, positive_words, neutral_words = making_dataset(filename='kartaslovsent.csv')

def emotion_recognizer(text, negative_words, positive_words, neutral_words):
    negative_color, positive_color, neutral_color = 0, 0, 0
    new_text = text.lower().split(' ')
    num_of_real_words = len(new_text)
    for word in new_text:
        word = word.replace(',','').replace('.','').replace('!','').replace('?','').strip()
        if len(word) < 3: # чтобы исключить союзы и предлоги
            num_of_real_words -= 1
            continue
        else:
            if word in list(negative_words['term']):
                negative_color += 1
            if word in list(positive_words['term']):
                positive_color += 1
            if word in list(neutral_words['term']):
                neutral_color += 1
    
    if negative_color > positive_color and negative_color > neutral_color:
        return 'negattive'
    elif positive_color > negative_color and positive_color > neutral_color:
        return 'positive'
    elif neutral_color > negative_color and neutral_color > positive_color:
        return 'neutral'
    else:
        return "can't predict"
