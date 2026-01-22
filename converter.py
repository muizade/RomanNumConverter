def int_to_roman(num):
    if not 1 <= num <= 3999:
        raise ValueError("Number out of range (1-3999)")
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(s):
    roman_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_values.get(char.upper(), 0)
        if value == 0:
            raise ValueError("Invalid Roman numeral")
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def is_valid_roman(s):
    valid_chars = set('IVXLCDM')
    if not all(char.upper() in valid_chars for char in s):
        return False
    try:
        num = roman_to_int(s)
        return int_to_roman(num) == s.upper()
    except ValueError:
        return False

def main():
    while True:
        print("1: Integer to Roman\n2: Roman to Integer\n3: Exit")
        choice = input("Choose mode: ").strip()
        if choice == '1':
            try:
                num = int(input("Enter integer (1-3999): "))
                print(int_to_roman(num))
            except ValueError as e:
                print(e)
        elif choice == '2':
            roman = input("Enter Roman numeral: ").strip().upper()
            if is_valid_roman(roman):
                print(roman_to_int(roman))
            else:
                print("Invalid Roman numeral")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
