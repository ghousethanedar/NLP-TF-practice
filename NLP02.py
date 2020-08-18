from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences =[
    'I love my dog',
    'I love my cat',
    'you are amazing',
    'Would you believe that my dog is super dog'
]


## Tokenizing the sentences

tokenizer = Tokenizer(num_words=100,oov_token='<OOV>')

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

sentences_01 = tokenizer.texts_to_sequences(sentences)

print(word_index)
print(sentences_01)

sentences_02 = pad_sequences(sentences_01,padding='post')

print(sentences_02)

## After tokeining the sentences we need to make the padding of the sentences



test_data =[
    'i really love my dog',
    'my dog loves my manatee'
]


test_seq=tokenizer.texts_to_sequences(test_data)


print(test_seq)


