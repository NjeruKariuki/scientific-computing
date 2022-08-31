import math
from scipy import spatial
import math
import time


start_time = time.time()
'''users a,b,c,d with ratings for 2 items'''
a = [3, 2]
b = [5, 6]
c = [9, 3]
d = [3, 8]

#list of users combinations
users_list = ['a_and_b', 'a_and_c', 'a_and_d', 'b_and_c', 'b_and_d', 'c_and_d']


def find_similar_users():
    '''using cosine similarity to find similar users
        returns 2 users who are most similar
    '''

    #results list
    results = []
    #use spation cosine to find 2 most similar users
    a_and_b = spatial.distance.cosine(a, b)
    results.append(a_and_b)
    a_and_c = spatial.distance.cosine(a, c)
    results.append(a_and_c)
    a_and_d = spatial.distance.cosine(a, d)
    results.append(a_and_d)
    b_and_c = spatial.distance.cosine(b, c)
    results.append(b_and_c)
    b_and_d = spatial.distance.cosine(b, d)
    results.append(b_and_d)
    c_and_d = spatial.distance.cosine(c, d)
    results.append(c_and_d)

    #find most similar
    similar = min(results)
    pos = results.index(similar)
    
    return similar, pos

def main():
    res = find_similar_users()
    pos = res[1]
    results = f"Most similar users are {users_list[pos]} with similarity of:  {res[0]}"
    print(results)


if __name__ == "__main__":
    main()
    end_time = time.time()
    print(f"Program took: {end_time-start_time} seconds to run") #calcuate time to run program


    
    
    
    
    
