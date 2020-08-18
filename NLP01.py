from tensorflow.keras.preprocessing.text import Tokenizer


sentences =[
    'I love my dog',
    'I love my cat'
]

tokenizer = Tokenizer( num_words= 100)

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

tokenizer.fit

print(word_index)