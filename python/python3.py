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

def adjcollector(words):
    Adj = []
    count = 0
    for token in words:
        if token.pos_ == "ADJ":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            Adj.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Adj


listAdj = adjcollector(disneywords)
adj_freq = Counter(listAdj)
topTen = adj_freq.most_common(10)
print(topTen)
lastTen = adj_freq.most_common()[:-5:-1]
# print(lastTen)

bar_chartTopTenAdj = pygal.Bar()

bar_chartTopTenAdj.title= 'Top 10 Adjectives in Disney Songs'

for a in adj_freq:
    print(a[0], a[1])
    bar_chartTopTenAdj.add(a[0], a[1])

bar_chartTopTenAdj.render_to_file('bar_chartTopTenAdj.svg')
