import random


def distance(a, b) -> float:
    return abs(a - b)


def read_lists_from_input():
    southpole_list = []
    northpole_list = []
    
    with open("input.txt") as file:
        for line in file.readlines():
            a, b = line.split("   ")

            southpole_list.append(int(a))
            northpole_list.append(int(b))
    
    return sorted(southpole_list), sorted(northpole_list)


def task_1(southpole_list, northpole_list):
    MAX_LENGTH = len(southpole_list)
    total_distance = 0    
    
    for i in range(MAX_LENGTH):
        a = southpole_list[i]
        b = northpole_list[i]
        
        # print(a, b)
        total_distance += distance(a, b)
    
    print("Total distance: ", total_distance)


def get_similarity_score(populated_list, unique_number):
    MAX_LENGTH = len(northpole_list)
    
    similarity_score = 0
    for i in range(MAX_LENGTH):
        if northpole_list[i] != unique_number:
            continue
        similarity_score += unique_number
        
    return similarity_score
        
    
def task_2(southpole_list, northpole_list):
    unique_numbers = set(southpole_list)
    similarity_score = 0
    
    for unique in unique_numbers:
        similarity_score += get_similarity_score(northpole_list, unique)

    print("Similarity score: ", similarity_score)            


if __name__ == "__main__":
    southpole_list, northpole_list = read_lists_from_input()
    task_1(southpole_list, northpole_list)
    task_2(southpole_list, northpole_list)
