nums = input().split()
max_run_of_b = int(nums[2]) + ((20 - int(nums[1])) * 36)
if int(nums[0]) >= max_run_of_b:
    print('NO')
else:
    print("YES")
