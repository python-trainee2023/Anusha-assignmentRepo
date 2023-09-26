def sum(start, stop):
    even_sum = 0
    odd_sum = 0

    for num in range(start, stop + 1):
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum


start = int(input("Enter a start value for a range:"))
stop = int(input("Enter a end value for a range:"))

if start > stop:
    print("Start value must be less than or equal to stop value.")
else:
    even_sum, odd_sum = sum(start, stop)

    print(f"Sum of even numbers from{start} to {stop}: {even_sum}")
    print(f"Sum of odd numbers from{start} to {stop}: {odd_sum}")
    
    
   