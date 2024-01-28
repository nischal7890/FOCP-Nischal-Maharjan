import sys

def format_time(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours} Hours, {minutes} Minutes"

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        return

    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in lines:
        if line.strip() == 'END':
            break

        cat, entry_time, exit_time = line.strip().split(',')
        entry_time, exit_time = int(entry_time), int(exit_time)

        if cat == 'OURS':
            cat_visits += 1
            total_time_in_house += exit_time - entry_time
            durations.append(exit_time - entry_time)
        elif entry_time != exit_time:
            other_cats += 1

    if cat_visits == 0:
        print('No visits recorded for the correct cat.')
        return

    average_duration = format_time(sum(durations) // len(durations))
    longest_duration = format_time(max(durations))
    shortest_duration = format_time(min(durations))

    print('Log File Analysis')
    print('==================')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}')
    print(f'Total Time in House: {format_time(total_time_in_house)}')
    print(f'Average Visit Length: {average_duration}')
    print(f'Longest Visit: {longest_duration}')
    print(f'Shortest Visit: {shortest_duration}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Missing command line argument!')
    else:
        analyze_cat_shelter_log(sys.argv[1])
