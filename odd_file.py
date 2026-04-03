def is_odd(num):
    try:
        if not isinstance(num,int):
            raise ValueError("input must be an integer")
        return num%2!=0
    except ValueError as e:
        print(e)
        return None

print(is_odd(5)) #Output: True
