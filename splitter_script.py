import pandas as pd 
from hazm import Normalizer, POSTagger, word_tokenize, Chunker, tree2brackets
import re 
# Define the pattern to match anything between []
pattern = r'\[(.*?)\]'


normalizer = Normalizer()
tagger = POSTagger(model='pos_tagger.model')
chunker = Chunker(model='chunker.model')

def find_chunks(sentence=None):
    if sentence is None:
        # ENTER‌ YOUR‌ SENTENCE HERE:
        sentence = input("جمله مورد نظر را وارید کنید:")
        
    tagged = tagger.tag(word_tokenize(sentence))
    parts = tree2brackets(chunker.parse(tagged))
    # Find all occurrences of the pattern in the input string
    extracted_phrases = re.findall(pattern, parts)
    for i, word in enumerate(extracted_phrases):
        if 'PP' in word:
            extracted_phrases.remove(word)
            
    corrected = []
    for word in extracted_phrases:
        if 'NP' in word:
            word = word.replace(' NP', '')
            corrected.append(word)
    
    return corrected


sentence = "نصب رکاب هات‌لاین هادی روکش‌دار با یک عدد کنکتور."
result = find_chunks(sentence = sentence)

print(result)
with open('Result.txt', 'w') as file:
    file.write(sentence)
    file.write('\n')
    for word in result:
        file.write(word+' | ')
    
    
