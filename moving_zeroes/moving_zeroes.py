'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    max_pointer = len(arr)
    pointer = 0

    while pointer < max_pointer:
        if arr[pointer] == 0:
            del arr[pointer]
            arr.append(0)
            max_pointer -= 1
        else:
            pointer += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")