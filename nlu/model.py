from tensorflow.python.keras.layers import embeddings
import yaml
import numpy as np

# Lib tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from  tensorflow.keras.utils import to_categorical


data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}|{}'.format(command['entity'], command['action']))


# Processar texto: palavras, caracteres, byte, sub-bytes, sub-palavras
'''
chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
'''

# Mapear char-idx
'''
chr2idx = {}
idx2chr = {}

for i, ch in enumerate(chars):
    chr2idx[ch] = i
    idx2chr[i] = ch
'''


max_seq = max([len(bytes(x.encode('utf-8'))) for x in inputs])

print('Maior seq: ', max_seq)

# Criar o dataset one-hot: (número de exemplos, tamano da sequencia, num caracteres)
# Criar o dataset disperso: (número de exemplos, tamano da sequencia)

# input data one-hot encoding
input_data = np.zeros((len(inputs), max_seq, 256), dtype='float32')

# input data sparce
# input_data = np.zeros((len(inputs), max_seq), dtype='float32')

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i,k, int(ch)] = 1.0


# Criar labels para o classificador

# output data
labels = set(outputs)

fwrite = open('labels.txt', 'w', encoding='utf-8')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label
    fwrite.write(label + '\n')
fwrite.close()

output_data = []

for output in outputs:
    output_data.append(label2idx[output])


output_data = to_categorical(output_data,len(output_data))

print(output_data[0])

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(output_data), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(input_data, output_data, epochs=512)

# Savar model
model.save('model.h5')

# Classificar de texto em cada uma entidade
def classify(text):
    # Criar uma array de entrada
    x = np.zeros((1, 48 , 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0
    
    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()
    print(idx2label[idx])

'''
while True:
    text = input('Digite algo: ')
    classify(text)
'''
