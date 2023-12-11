import json
import re

ALL_SONGS_JSON = "allSongs.json"
LYRICS_PATH = 'lyrics//'
LIST_OF_SONGS = []

def get_json_of_songs():
    f = open(ALL_SONGS_JSON, 'r')
    return json.load(f)

def nospecial(text):
  text = re.sub("[^a-zA-Z ]+", "", text).lower()
  text = text.replace(" ", "")
  return text
  

def get_loosely_references(json_list, lyrics, song):
    loosely_references = list()
    songs_but_the_actual = list(filter(lambda x : x["name"] != song , json_list))
    for song in songs_but_the_actual:
        for key in song["keys"]:
            if key in lyrics:
                ref = f"{key}: {song['name']}"
                loosely_references.append(ref)
    return loosely_references      

def print_song(song, used_songs, tab = False):
    if song not in used_songs:
        if tab:
            print(f"\t{song}")
        else:
            print(f"{song}")
        used_songs.add(song)
    else:
        if tab:
            print(f"\t({song})")
        else:
            print(f"({song})")
    return used_songs
    
def print_song_lref(song, used_songs, tab = False):
    lref = song.split(": ")[0]
    name = song.split(": ")[1]
    
    if name not in used_songs:
        if tab:
            print(f"\t{song}")
        else:
            print(f"{song}")
        used_songs.add(name)
    else:
        song = f"{lref}: ({name})"
        if tab:
            print(f"\t{song}")
        else:
            print(f"{song}")
    return used_songs
    
def main():
    json_list = get_json_of_songs()
    songs = list(map(lambda x : x["name"], json_list))
    
    for data in json_list:
        filename = data["filename"]
        song = dict()
        song["name"] = data["name"]
        song["references"] = list()
        song["looselyReferences"] = list()
        songs_but_the_actual = list(filter(lambda x : x != song["name"] , songs))
        lyrics = open(f"{LYRICS_PATH}{data['filename']}").read()
        lyrics = nospecial(lyrics)
        #print(lyrics)
        song["references"] = list(filter(bool, (map(lambda x : x if x in lyrics else False, songs_but_the_actual))))
        song["looselyReferences"] = get_loosely_references(json_list, lyrics, song["name"])
        if len(song["references"]) > 0:
            LIST_OF_SONGS.append(song)
    
    used_songs = set()
    for song in LIST_OF_SONGS:
        used_songs = print_song(song["name"], used_songs)
        
        for ref in song['references']:
            used_songs = print_song(ref, used_songs, tab = True)
        
        #for lref in song['looselyReferences']:
            #used_songs = print_song_lref(lref, used_songs, tab = True)
main()  