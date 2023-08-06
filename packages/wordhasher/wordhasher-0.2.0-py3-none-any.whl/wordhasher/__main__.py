from wordhasher import WordHasher


def main():
    wh = WordHasher()
    print(wh)
    m = "This is a test."
    print(f"Hashing {m=} {wh.from_str(m)=}")
    print(f"Hashing {__file__=} {wh.from_str(__file__)=}")
    print("Default sample:", wh.sample())
    for mode in ["va", "an", "anN", "van", "vanN"]:
        print(f"  mode:{mode:<5}: {wh.sample(mode=mode)}")


if __name__ == "__main__":
    main()
