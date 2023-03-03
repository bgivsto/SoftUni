countries = [x for x in input().split(", ")]
capitals = [x for x in input().split(", ")]

result = {k: v for k, v in zip(countries, capitals)}
for k, v in result.items():
    print(f"{k} -> {v}")
