def recurse(level):
    print(f"Level: {level}")
    if level:
        recurse(level - 1)

def not_called():
    print("This is not called")
