'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    slide = []
    numbers = []
    current_max = 0
    check_num = 0

    for i in range(len(nums)):
        if nums[i] > current_max:
            current_max = nums[i]
        slide.append(nums[i])

        if k > 0:
            k -= 1
        else:
            check_num = slide[0]
            del slide[0]
            if check_num == current_max:
                current_max = max(slide)

        if k == 0:
            numbers.append(current_max)

    return numbers


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
