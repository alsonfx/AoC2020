# Declare passports in a batch file as valid or invalid.
# 1. Create a list of passport strings
# 2. check to see if each passport contains the required fields
# 3. count how many are valid / invalid.

import re

passports = open('passports.txt')

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_fields, valid_data = 0, 0

for passport in passports.read().split("\n\n"):
    passport = dict(map(lambda x: x.split(":"), passport.split()))
    if fields.issubset(set(passport.keys())):
        valid = True
        valid &= 1920 <= int(passport.get('byr')) <= 2002
        valid &= 2010 <= int(passport.get('iyr')) <= 2020
        valid &= 2020 <= int(passport.get('eyr')) <= 2030
        valid &= (passport.get('hgt').endswith("cm") and 150 <= int(passport.get('hgt')[:-2]) <= 193) or \
                 (passport.get('hgt').endswith("in") and 59 <= int(passport.get('hgt')[:-2]) <= 76)
        valid &= bool(re.fullmatch(r"#[0-9a-f]{6}", passport.get('hcl')))
        valid &= bool(re.fullmatch(r"[0-9]{9}", passport.get('pid')))
        valid &= passport.get('ecl') in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        valid_fields += 1
        valid_data += valid

print(f"Total Valid Passports: {valid_fields}")

print(f"Total Passports with Valid Data: {valid_data}")
