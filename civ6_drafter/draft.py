import random

LEADER_PASS = [
    "Abraham Lincoln - American",
    "Nzinga Mbande - Kongolese",
    "Tokugawa - Japanese",
    "Nader Shah - Persian",
    "Wu Zetian - Chinese",
    "Yongle - Chinese",
    "Ramses II - Egyptian",
    "Sundiata Keita - Malian",
    "Theodora - Byzantine",
    "Sejong - Korean",
    "Ludwig II - German",
    "Elizabeth I - English",
    "Saladin (Sultan) - Arabian",
    "Suleiman (Muhteşem) - Ottoman",
    "Qin Shi Huang (Unifier) - Chinese",
    "Cleopatra (Ptolemaic) - Egyptian",
    "Harald Hardrada (Varangian) - Norwegian",
    "Victoria (Age of Steam) - English"
]


def main():
    players = ["Алесь", "Мишаня", "Саман", "Елизавета"]
    for legend in players:
        nation = random.choice(LEADER_PASS)
        print(f"{legend} will play {nation}")


if __name__ == "__main__":
    main()