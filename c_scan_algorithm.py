def c_scan(current_head, requests):
    requests.sort()
    total_seek_time = 0
    while requests:
        for i in range(len(requests)):
            if requests[i] >= current_head:
                total_seek_time += abs(current_head - requests[i])
                current_head = requests.pop(i)
             
                break
        else:
            total_seek_time += (5000 - current_head)
            current_head = 0
        
    return total_seek_time

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python c_scan_algorithm.py initial_head_position requests_file.txt")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    requests_file = sys.argv[2]

    with open(requests_file, 'r') as file:
        requests = [int(line.strip()) for line in file]

    total_seek_time = c_scan(initial_head_position, requests)
    print("Total seek time for C-SCAN algorithm:", total_seek_time)
