def fcfs(current_head, requests):
    total_seek_time = 0
    for request in requests:
        total_seek_time += abs(current_head - request)
        current_head = request
    return total_seek_time

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python fcfs_algorithm.py initial_head_position requests_file.txt")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    requests_file = sys.argv[2]

    with open(requests_file, 'r') as file:
        requests = [int(line.strip()) for line in file]

    total_seek_time = fcfs(initial_head_position, requests)
    print("Total seek time for FCFS algorithm:", total_seek_time)
