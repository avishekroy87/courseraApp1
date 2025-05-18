import time

start_time = time.time();
# print("Hello World!");
#
# def add_num(a, b):
#     return a + b
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# result = add_num(num1, num2);
#
# print(result);
#
# for num in range(2, 20000000 , 2):
#     print(num);

numbersList = [1,2,3,4,5];
squaredList = list(map(lambda x: x*x, numbersList));

print(squaredList);
print("--- %s seconds ---" % (time.time() - start_time));