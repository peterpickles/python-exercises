# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there
# def p_times(input, num_times =1):


def p_times(statement, num):
    for i in range (0, num):
        print(statement)


# Call the function
p_times('string', 5)