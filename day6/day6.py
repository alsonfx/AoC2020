from collections import Counter

customs = open('customs.txt', 'r')

groups = customs.read().split('\n\n')
group_count = 0
all_yes_count = 0
for person in groups:
    # person = person.strip()
    questions = Counter(person)
    del questions['\n']
    group_count += len(questions)
    print(questions)

    yes_cnt = len(person.split())
    all_yes_count += sum(yes == yes_cnt for key, yes in questions.items())

print(f"The sum of group responses is: {group_count}")
print(f"The sum of all yes responses in a group is: {all_yes_count}")
