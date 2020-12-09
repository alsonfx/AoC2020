from collections import defaultdict

rules = open('rules.txt', 'r')
rules_list = []

rules_cnt = []

for line in rules:
    parent_bag, child_bags = line.split(' bags contain ')
    if 'no other bags' in child_bags:
        rules_list.append((parent_bag, ''))
    else:
        child_bags = child_bags.split(', ')
        for child_bag in child_bags:
            rules_list.append((parent_bag, child_bag[2:(child_bag.index(' bag'))]))
            rules_cnt.append((parent_bag, [int(child_bag[:1]), child_bag[2:(child_bag.index(' bag'))]]))
rules.close()

bags_graph = defaultdict(list)
for parent, child in rules_list:
    bags_graph[parent].append(child)

bags_cnt = defaultdict(list)
for parent, child in rules_cnt:
    bags_cnt[parent].append(child)


def find_bag(graph, start, target, path=[]):
    path = path + [start]
    if start == target:
        return path
    if start not in graph:
        return None
    for new_parent in graph[start]:
        if new_parent not in path:
            new_path = find_bag(graph, new_parent, target, path)
            if new_path:
                return new_path
    return None


parent_bags = set()
for item in bags_graph:
    item_path = find_bag(bags_graph, item, 'shiny gold')
    if item_path:
        parent_bags.add(item_path[0])

print(f"The total bags that can hold a shiny gold bag are: {len(parent_bags) - 1}")


def count_bags(bag):
    if bags_cnt.get(bag):
        count = 1
        for num, child in bags_cnt.get(bag):
            count += num * count_bags(child)
        return count
    return 1


print(f"The total bags needed in one shiny gold bag is: {count_bags('shiny gold') - 1}")
