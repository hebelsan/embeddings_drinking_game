import random
import numpy as np
from scipy import spatial


def read_vectors(file_name):
    embeddings_dict = {}
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            # we might have to check if values[1] is another word
            vector = np.asarray(values[1:], "float32")
            embeddings_dict[word] = vector
    return embeddings_dict


def find_closest_embeddings(embeddings_dict, embedding):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))



if __name__ == "__main__":
    embeddings_dict = read_vectors("vectors.txt")
    size = len(embeddings_dict)
    print("embedding created...")
    
    while(True):
        # take random word
        rand_int = random.randint(0, size)
        all_words = list(embeddings_dict.keys())
        rand_word = all_words[rand_int]
        print(rand_word)
    
        p1_word = input("player1 one choose a related word: ")
        p2_word = input("player2 one choose a related word: ")
        
        p1_distance = spatial.distance.euclidean(embeddings_dict[rand_word], embeddings_dict[p1_word])
        p2_distance = spatial.distance.euclidean(embeddings_dict[rand_word], embeddings_dict[p2_word])
        print("distance p1: " + str(p1_distance))
        print("distance p2: " + str(p2_distance))
        
        print("top 5 close words:")
        result_list = find_closest_embeddings(embeddings_dict, embeddings_dict[rand_word])[1:6]
        print(result_list)
