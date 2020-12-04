from itertools import *
import re

with open('input.txt', 'r') as input_file:
    data = input_file.read()

def clean_new_lines_in_list(passport_list):
    new_passport_list = []
    for passport in passport_list:
        new_passport_list.append(passport.replace('\n', ' ').strip())
    return new_passport_list

def is_valid_passport(passport, compulsory_fields):
    passport_fields = passport.split(' ')
    fields_contained_dict = dict( (field, False) for field in compulsory_fields)
    for pass_field in passport_fields:
        if (pass_field.split(':')[0] in fields_contained_dict):
            fields_contained_dict[pass_field.split(':')[0]] = True
    return not(False in fields_contained_dict.values())

def count_valid_passports(passport_info_list, compulsory_fields):
    valid_passport_count = 0
    for passport in passport_info_list:
        if (is_valid_passport(passport, compulsory_fields)):
            valid_passport_count = valid_passport_count + 1
    return valid_passport_count

passport_info_list = clean_new_lines_in_list(data.split('\n\n'))

print(count_valid_passports(passport_info_list, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))

# Part 2

def is_valid_passport_with_more_validation(passport, compulsory_fields):
    passport_fields = passport.split(' ')
    fields_contained_dict = dict( (field, False) for field in compulsory_fields)
    for pass_field in passport_fields:
        pass_field_pair = pass_field.split(':')
        if (pass_field_pair[0] in fields_contained_dict):
            if (pass_field_pair[0] == "byr"):
                if (re.match("(19[2-9][0-9])|(200[0-2])", pass_field_pair[1]) and len(pass_field_pair[1]) == 4):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "iyr"):
                if (re.match("(201[0-9])|(2020)", pass_field_pair[1]) and len(pass_field_pair[1]) == 4):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "eyr"):
                if (re.match("(202[0-9])|(2030)", pass_field_pair[1]) and len(pass_field_pair[1]) == 4):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "hgt"):
                if (re.search("(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in", pass_field_pair[1])):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "hcl"):
                if (re.search("#([a-f0-9]{6})", pass_field_pair[1]) and len(pass_field_pair[1]) == 7):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "ecl"):
                if (pass_field_pair[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    fields_contained_dict[pass_field_pair[0]] = True
            elif (pass_field_pair[0] == "pid"):
                if (re.search("[0-9]{9}", pass_field_pair[1]) and len(pass_field_pair[1]) == 9):
                    fields_contained_dict[pass_field_pair[0]] = True                
    return not (False in fields_contained_dict.values())

def count_valid_passports_with_validations(passport, compulsory_fields):
    valid_passport_count = 0
    for passport in passport_info_list:
        if (is_valid_passport_with_more_validation(passport, compulsory_fields)):
            valid_passport_count = valid_passport_count + 1
    return valid_passport_count


print(count_valid_passports_with_validations(passport_info_list, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))