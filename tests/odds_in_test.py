from statistics import mean


from baseblock import odds_of

MAX = 10


def driver(odds: int):

    results = []
    for j in range(0, MAX):  # 20.018 in 1000 trials
        ctr = 0
        for i in range(0, 100):
            if odds_of(odds):
                ctr += 1
        results.append(ctr)

    print(f"Result: odds={odds}% and {mean(results)}")


def main():
    driver(20)
    driver(25)
    driver(33)
    driver(40)
    driver(50)
    driver(66)
    driver(75)
    driver(80)


if __name__ == "__main__":
    main()
