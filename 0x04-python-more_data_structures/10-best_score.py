#!/usr/bin/python3
def best_score(a_dictionary):
    score = ['', float('-inf')]
    if a_dictionary is None:
        return (None)
    else:
        for key, value in a_dictionary.items():
            if value > score[1]:
                score[0] = key
                score[1] = value
    return (score[0])
        
