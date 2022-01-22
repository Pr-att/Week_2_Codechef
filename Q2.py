ans, nums = 0, []
for i in range(1, 100000):
    ans += i
    nums.append(ans)
for k in range(int(input())):
    req = int(input())
    for j in range(len(nums)):
        if req == nums[j]:
            print(j + 1)
            break
        elif req < nums[j]:
            print(j)
            break

