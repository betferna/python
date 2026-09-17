#!/bin/env python3

import sys

def score_analytics():
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1: 
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for i in range(1, len(sys.argv)):
            try:
                int(sys.argv[i])
                
            except ValueError:
                print(f"Invalid parameter {sys.argv[i]}")
                return
            
        total_score = 0
        low_score = int(sys.argv[1])
        high_score = 0
        for i in range(1, len(sys.argv)):
            total_score =+ int(sys.argv[i])
            if int(sys.argv[i]) < low_score:
                low_score = int(sys.argv[i])
            if int(sys.argv[i]) > high_score:
                high_score = int(sys.argv[i])
        print(f"Total players: {len(sys.argv)-1}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score/(len(sys.argv)-1)}")
        print(f"Low score: {low_score}")
#               print(f"High score: {high_score}")
        print(f"Score range: {high_score - low_score}")

if __name__ == "__main__":
    score_analytics()
