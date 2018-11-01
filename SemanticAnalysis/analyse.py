from dict_tagger import *

def value_of(sentiment):
    if sentiment == 'positive':
        return 1
    elif sentiment == 'negative':
        return -1
    else:
        return 0

def sentence_score(sentence_tokens, previous_token, acum_score):
    if not sentence_tokens:

        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])


# text = sys.argv[1]
# if(text=="exit"):
#     sys.exit(0)
# text = """What can I say about this place.
# The staff of the restaurant is nice and the eggplant is not bad.
# Apart from that, very uninspired food, lack of atmosphere and too expensive.
# I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu.
# Will be the last time I visit, I recommend others to avoid."""
i = 0

def multi_input():
    text = []
    try:
        while True:
            data=input()
            text.append(data)
            if not data: break
            yield data
    except KeyboardInterrupt:
        return text


while 1:
    i = i+1
    print("[",i,"]","-> ")
    text = input()
    splitter = Splitter()
    postagger = POSTagger()

    splitted_sentences = splitter.split(text)

    print("tokenized text","\n",splitted_sentences)
    print("\n")
    pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

    print("POS tagged sentences","\n",pos_tagged_sentences)
    print("\n")

    dicttagger = DictionaryTagger([ 'dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])

    dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

    print("Sentiment Tagged Sentences","\n",dict_tagged_sentences)
    print("\n")


    sentiment = sentiment_score(dict_tagged_sentences)
    print("Semantic Value: ",sentiment,"\n")
    if(sentiment<0):
        print("Negative Sentence")
    elif(sentiment>0):
        print("Positive Sentence")
    else:
        print("Neutral Sentence")
    print('\n')
    # print('----------------------')
