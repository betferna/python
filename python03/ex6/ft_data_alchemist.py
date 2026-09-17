#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    capitalized_only = [name for name in initial_players if name.istitle()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(50, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    avg_score = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg_score}")

    high_scores = {
        name: score for name, score in scores.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()