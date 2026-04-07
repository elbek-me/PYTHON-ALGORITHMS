N = int(input())
nums = list(map(int, input().split()))
no_duplicate_numbers = set(nums)
no_duplicate_number =sum(no_duplicate_numbers) *2 - sum(nums)
print(no_duplicate_number)



