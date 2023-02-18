import json
import re
import os
from datetime import datetime

ALL_SONGS_JSON = "allSongs.json"
LYRICS_PATH = 'lyrics//'
LIST_OF_SONGS = []

banned_words = ['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'to', 'it', 'i', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this', 'they', 'at', 'but', 'we', 'his', 'from', 'that', 'not', 'by', 'she', 'or', 'as', 'what', 'go', 'their', 'can', 'who', 'get', 'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'as', 'up', 'one', 'time', 'there', 'year', 'so', 'think', 'when', 'which', 'them', 'some', 'me', 'people', 'take', 'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two', 'more', 'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because', 'day', 'more', 'use', 'no', 'man', 'find', 'here', 'thing', 'give', 'many', 'well', 'only']

def main():
    files_extension = os.listdir(LYRICS_PATH)
    for file_extension in files_extension:
        song = dict()
        song["name"] = file_extension[:-4].lower()
        song["keys"] = song["name"].split() if len(song["name"].split()) > 1 else []
        song["keys"] = list(set(song["keys"]))
        song["keys"] = list(filter(bool, map(lambda x : x if x not in banned_words else False, song["keys"])))
        song["filename"] = file_extension
        LIST_OF_SONGS.append(song)
    json_string = json.dumps(LIST_OF_SONGS)
    #print(json_string)
    now = datetime.now()
    datetime_string = now.strftime("%d%m%Y%H%M%S")
    filename = f"allSongs-{datetime_string}.json"
    with open(filename, "w") as f:
        f.write(json_string)
    
main()
    