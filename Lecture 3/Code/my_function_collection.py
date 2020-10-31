def reverse_integer(num):
    result = ""
    num = str(num)
    for i in range(len(num)):
        i += 1
        result += num[-i]

    print(f"Result is  {result}")  # slight modification

    return int(result)


PI = 3.141


if __name__ == "__main__":

    reverse_integer(784592749214)
