def get_min_max(arr) -> tuple:
    length = len(arr)

    if length == 0:
        return ()
    if length == 1:
        return arr[0], arr[0]

    mid = length // 2

    left_min, left_max = get_min_max(arr[0:mid])
    right_min, right_max = get_min_max(arr[mid:length])

    return min(left_min, right_min), max(left_max, right_max)

if __name__ == "__main__":
    pass_data = [12,3,4,1,4,1,1,0,12]
    res = get_min_max(pass_data)
    print(res)