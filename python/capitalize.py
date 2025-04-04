# Complete the solve function below.
def solve(s):
    parts = s.split(" ")
    new_parts = []
    for part in parts:
        new_parts.append(part.capitalize())
    return " ".join(new_parts)

if __name__ == '__main__':
    s = input("")
    print(solve(s))
