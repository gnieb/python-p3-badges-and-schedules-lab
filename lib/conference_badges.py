def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):

    index = 0
    room_list = []
    while index < len(names):
        room_list.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
        index += 1
    
    return room_list
   

def printer(names):

    print_badges = batch_badge_creator(names)
    for badge in print_badges:
        print(badge)

    print_room_assignment = assign_rooms(names)
    for badge in print_room_assignment:
        print(badge)
   


printer(["Arel", "Carol"])