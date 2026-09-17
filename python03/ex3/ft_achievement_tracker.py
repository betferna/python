#!/usr/bin/env python3
import random

ACHIEVEMENTS_POOL = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Crafting Genius",
    "Speed Runner",
    "Untouchable",
    "Collector Supreme",
    "World Savior",
    "Strategist",
    "Unstoppable",
    "Survivor",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set:
    count = random.randint(5, 10)
    selected = random.sample(ACHIEVEMENTS_POOL, count)
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_players_achievements = list(players.values())
    all_distinct = set().union(*all_players_achievements)
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set(all_players_achievements[0]).intersection(
        *all_players_achievements[1:]
    )
    print(f"Common achievements: {common}\n")

    for name, achievements in players.items():
        others_achievements = set().union(
            *[ach for p_name, ach in players.items() if p_name != name]
        )
        unique_to_player = achievements.difference(others_achievements)
        print(f"Only {name} has: {unique_to_player}")

    print()

    full_pool_set = set(ACHIEVEMENTS_POOL)
    for name, achievements in players.items():
        missing = full_pool_set.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
