def loading_bar(n):
    bar = "." * 10
    count = n // 10
    if count == 0:
        bar = bar.replace(".", "%", 1)
    else:
        bar = bar.replace(".", "%", count)

    if not count == 10:
        print(f"{n}% [{bar}]")
        print("Still loading...")
    else:
        print(f"100% Complete!")
        print(f"[{bar}]")


n = int(input())
loading_bar(n)
