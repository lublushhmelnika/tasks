from itertools import count

def chain():
 for number in count(1):
  for char in str(number):
    yield char

def position(number):
    input_to_str = str(number)
    generator = chain()
    position_index = 0

    for curr_char in generator:
         position_index += 1
         input_position_index = 0
         for input_char in input_to_str:
                if curr_char != input_char:
                        break
                curr_char = next(generator)
                input_position_index += 1
         if input_position_index == len(input_to_str):
            return position_index
         position_index += input_position_index

number=int(input())
print position(number)

