#!/usr/bin/env python3

import random


ACHIEVEMENTS = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "Collector Supreme",
    "Speed Runner",
    "Strategist",
    "World Savior",
    "Untouchable",
    "Hidden Path Finder",
    "Survivor",
    "Treasure Hunter",
    "Sharp Mind",
    "Unstoppable",
    "Crafting Genius",
]


def gen_player_achievements() -> set[str]:
    number = random.randint(4, 8)

    selected = set()

    while len(selected) < number:
        achievement = random.choice(ACHIEVEMENTS)
        selected.add(achievement)

    return selected


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = alice.union(bob)
    all_achievements = all_achievements.union(charlie)
    all_achievements = all_achievements.union(dylan)

    print(f"All distinct achievements: {all_achievements}")

    common = alice.intersection(bob)
    common = common.intersection(charlie)
    common = common.intersection(dylan)

    print(f"Common achievements: {common}")

    others = bob.union(charlie)
    others = others.union(dylan)
    only_alice = alice.difference(others)
    print(f"Only Alice has: {only_alice}")

    others = alice.union(charlie)
    others = others.union(dylan)
    only_bob = bob.difference(others)
    print(f"Only Bob has: {only_bob}")

    others = alice.union(bob)
    others = others.union(dylan)
    only_charlie = charlie.difference(others)
    print(f"Only Charlie has: {only_charlie}")

    others = alice.union(bob)
    others = others.union(charlie)
    only_dylan = dylan.difference(others)
    print(f"Only Dylan has: {only_dylan}")

    print(
        f"Alice is missing: "
        f"{all_achievements.difference(alice)}"
    )

    print(
        f"Bob is missing: "
        f"{all_achievements.difference(bob)}"
    )

    print(
        f"Charlie is missing: "
        f"{all_achievements.difference(charlie)}"
    )

    print(
        f"Dylan is missing: "
        f"{all_achievements.difference(dylan)}"
    )


if __name__ == "__main__":
    main()