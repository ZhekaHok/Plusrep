# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=','):
    group1 = set(first_group.split(separator))
    group2 = set(second_group.split(separator))
    common_participants = list(set(group1.intersection(group2)))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

other_separator = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(other_separator)