def run_test():
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]

    tshirts = [(c, s) for c in colors for s in sizes]
    # print(tshirts)

    # generator expression
    for a in (f"color:{c}; size:{s}" for c in colors for s in sizes):
        print(a)


if __name__ == "__main__":
    run_test()
