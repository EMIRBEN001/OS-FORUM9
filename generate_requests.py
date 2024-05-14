import random
import sys

def generate_requests(num_requests, num_cylinders):
    return [random.randint(0, num_cylinders - 1) for _ in range(num_requests)]

def save_requests_to_file(requests, file_path):
    with open(file_path, 'w') as file:
        for request in requests:
            file.write(str(request) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_requests.py num_requests num_cylinders output_file.txt")
        sys.exit(1)

    num_requests = int(sys.argv[1])
    num_cylinders = int(sys.argv[2])
    output_file = sys.argv[3]

    requests = generate_requests(num_requests, num_cylinders)
    save_requests_to_file(requests, output_file)
