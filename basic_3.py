import sys
import time
import psutil

def get_memory_usage_kb():
    return int(psutil.Process().memory_info().rss / 1024)

def run(input_file, output_file, method):
    X, Y = parse_input_file(input_file)
    start_time = time.time()
    cost, X1, X2 = method(X, Y)
    end_time = time.time()
    mem_kb = get_memory_usage_kb()
    time_ms = (end_time - start_time) * 1000

    with open(output_file, 'w+') as f:
        f.write(f"{cost}\n")
        f.write(f"{X1}\n")
        f.write(f"{X2}\n")
        f.write(f"{time_ms}\n")
        f.write(f"{mem_kb}\n")

def generate_string(base, indices):
    for index in indices:
        index = int(index)
        base = base[:index+1] + base + base[index+1:]
    return base


def parse_input_file(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0
    s1 = lines[i]
    i += 1
    j = 0
    s1_indices = []
    while lines[i].isdigit():
        s1_indices.append(int(lines[i]))
        j += 1
        i += 1

    s2 = lines[i]
    i += 1
    s2_indices = []
    while i < len(lines) and lines[i].isdigit():
        s2_indices.append(int(lines[i]))
        i += 1

    final_s1 = generate_string(s1, s1_indices)
    final_s2 = generate_string(s2, s2_indices)
    return final_s1, final_s2


def seq_align_basic(X, Y):
    m, n = len(X), len(Y)
    opt = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        opt[i][0] = i * delta
    for j in range(n + 1):
        opt[0][j] = j * delta

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c_sub = opt[i - 1][j - 1] + alpha[X[i - 1]][Y[j - 1]]
            c_del = opt[i - 1][j] + delta
            c_ins = opt[i][j - 1] + delta
            opt[i][j] = min(c_sub, c_del, c_ins)

    X1, Y1 = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        if opt[i][j] == opt[i - 1][j - 1] + alpha[X[i - 1]][Y[j - 1]]:
            X1 = X[i - 1] + X1
            Y1 = Y[j - 1] + Y1
            i -= 1
            j -= 1
        elif opt[i][j] == opt[i - 1][j] + delta:
            X1 = X[i - 1] + X1
            Y1 = "_" + Y1
            i -= 1
        else:
            X1 = "_" + X1
            Y1 = Y[j - 1] + Y1
            j -= 1

    while i > 0:
        X1 = X[i - 1] + X1
        Y1 = "_" + Y1
        i -= 1

    while j > 0:
        Y1 = Y[j - 1] + Y1
        X1 = "_" + X1
        j -= 1

    return opt[m][n], X1, Y1


if __name__ == '__main__':
    alpha = {
        'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
        'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
        'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
        'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
    }
    delta = 30
    run(sys.argv[1], sys.argv[2], seq_align_basic)