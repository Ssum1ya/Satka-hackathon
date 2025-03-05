from collections import Counter

while True:
    user_input = input()
    user_input_array = []
    check = Counter(user_input_array)
    if check['('] != check[')']:
        print("Данные введены некоректно. Введите данные повторно")
    else:
        break

brackets = '()'
nums = '1234567890'
commands = 'лпвн'
temp_variable = ''
temp_command = ''
have_num = 0
for i in range(len(user_input)):
    if user_input[i] in brackets:
        if temp_command != '':
            user_input_array.append(temp_command)
            temp_command = ''
        if temp_variable != '':
            user_input_array.append(int(temp_variable))
            temp_variable = ''
        user_input_array.append(user_input[i])
    elif user_input[i] in nums:
        if temp_command != '':
            user_input_array.append(temp_command)
            temp_command = ''
        temp_variable = temp_variable + user_input[i]
    elif user_input[i] in commands:
        if temp_variable != '':
            user_input_array.append(int(temp_variable))
            temp_variable = ''
        temp_command = temp_command + user_input[i]

check = Counter(user_input_array)
if check['('] != check[')']:
    print("Данные введены некоректно. Введите данные повторно")
else:
    n = 0
    while len(user_input_array) != 1:
        check = Counter(user_input_array)
        oppening_bracket = 0
        closing_bracket = 0
        have_num = 0
        for i in range(len(user_input_array)):
            if user_input_array[i] == "(":
                oppening_bracket = i
            if user_input_array[i] == ')':
                closing_bracket = i
                break
        if check['('] != 0:
            for i in range(oppening_bracket + 1, closing_bracket):
                if str(user_input_array[i])[0] in nums:
                    user_input_array[i + 1] = user_input_array[i] * user_input_array[i + 1]
                    user_input_array.pop(i)
                    have_num = 1
                    break
            if have_num == 0:
                for i in range(oppening_bracket + 1, closing_bracket):
                    if not (user_input_array[i + 1] in brackets):
                        user_input_array[i] = user_input_array[i] + user_input_array[i + 1]
                        user_input_array.pop(i + 1)
                        break
        else:
            for i in range(len(user_input_array)):
                if str(user_input_array[i])[0] in nums:
                    user_input_array[i + 1] = user_input_array[i] * user_input_array[i + 1]
                    user_input_array.pop(i)
                    have_num = 1
                    break
            if have_num == 0:
                for i in range(len(user_input_array)):
                    try:
                        if not (user_input_array[i + 1] in brackets):
                            user_input_array[i] = user_input_array[i] + user_input_array[i + 1]
                            user_input_array.pop(i + 1)
                            break
                    except TypeError as e:
                        pass
        if len(user_input_array[oppening_bracket:closing_bracket + 1]) == 3:
            user_input_array.pop(oppening_bracket)
            user_input_array.pop(oppening_bracket + 1)
print(user_input_array[0])
