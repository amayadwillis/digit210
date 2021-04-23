from collections import Counter
import spacy
import pygal
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'

disneysongs = open('disneySongLyrics.txt', 'r')
words = disneysongs.read()
disneywords = nlp(words)
# print(words)


def nouncollector(words):
    Nouns = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            Nouns.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Nouns

listNouns = nouncollector(disneywords)
noun_freq = Counter(listNouns)
topTen = noun_freq.most_common(10)
print(topTen)
lastTen = noun_freq.most_common()[:-5:-1]
# print(lastTen)

bar_chartOver10 = pygal.Bar()
bar_chartTopTen = pygal.Bar()

bar_chartOver10.title = 'Nouns Used Over 10 Times in Disney Songs'
bar_chartTopTen.title='Top 10 Nouns in Disney Songs'

for n in noun_freq:
    print(n,noun_freq[n])
    if noun_freq[n] > 10:
        bar_chartOver10.add(n,noun_freq[n])

for t in topTen:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

print(bar_chartOver10.render(is_unicode=True))
bar_chartOver10.render_to_file('bar_chartOver10.svg')
bar_chartTopTen.render_to_file('bar_chartTopTen.svg')
