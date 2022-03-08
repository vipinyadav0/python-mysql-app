
fh = open("Vocabulary_list.csv", "r")

wd_list = fh.readlines()

wd_list.pop(0)

vocab_list = []

for rawstring in wd_list:
    word, definition = rawstring.split(',', 1)

    definition = definition.rstrip()

    vocab_list.append({word, definition})

print(vocab_list)