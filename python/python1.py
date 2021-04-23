import spacy
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
disney = open('disneySongLyrics.txt', 'r')
words = disney.read()
print(words)
disneyWords = nlp(words)
for token in disneyWords:
     # if token.pos_ == "VERB":
     if token.pos_ == "NOUN":
        print(token.text, "---->", token.pos_, ":::::", token.lemma_)
# for entity in disneyWords.ents:
#     print(entity.text, entity.label_, spacy.explain(entity.label_))
