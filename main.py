import operator
import csv

import emoji

def extract_emojis(s):
  return ''.join(c for c in s if c in emoji.UNICODE_EMOJI)

with open('data.csv', 'r') as file:
    content = file.read()

emojis = extract_emojis(content)

group = {}
total = 0

for e in emojis:
    total += 1

    if e in group:
        group[e] += 1
    else:
        group[e] =1

sorted_group = sorted(group.items(), key=operator.itemgetter(1), reverse=True)

print('Total: {}'.format(total))

print("""
| Emoji    | Name     | Count    |  Percent |
| -------- | -------- | -------- | -------- |""")
for i in sorted_group[0:40]:
    [em, count] = i
    name = emoji.demojize(em)
    perc = 100 * count/total
    print('|{} | {} | {} | {}% |'.format(em, name, count, '{:.2f}'.format(perc)))
    