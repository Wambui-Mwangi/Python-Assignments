# Write a function that uses
# while, if and continue statements to print all the even numbers 
# between 0 and 50. 

def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)

even_numbers()


# Write a function that takes an integer argument and prints
# "Prime" if the number is prime, and "Not prime" if the number is not prime.
# def prime_numbers(number):
def prime_numbers(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not prime")
                break
            else:
                print("Prime")
prime_numbers(12)
prime_numbers(3)



# Write a function that takes a list of integers as input and prints the sum
# of all the even numbers in the list.

def sum(numbers):
    added = 0
    for n in numbers:
        if n%2==0:
            added+=n
    print(added)
numbers = [1,2,3,4,5]
sum(numbers)



# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two integers (inclusive) 
# that are divisible by 3.

def all_integers(num1,num2):
    sum = 0
    for n in range(num1,num2):
        if n%3==0:
            sum+=n
            print(sum)
all_integers(0,10)


 

