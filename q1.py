from pathlib import Path
import json

data = Path("data.json").read_text()
words_list = json.loads(data)
word=input()
print(words_list[word])