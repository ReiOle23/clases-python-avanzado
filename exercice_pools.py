import time, os
import math
from multiprocessing import Pool, cpu_count

def cpu_heavy_function(args):
    start_i, end_i = args
    checksum = 0.0
    t0 = time.perf_counter()
    _math_sqrt = math.sqrt
    _math_sin = math.sin

    for i in range(start_i, end_i):
        checksum += _math_sqrt(i) * _math_sin(i)

    elapsed = time.perf_counter() - t0
    return os.getpid(), elapsed, (end_i - start_i), checksum

if __name__ == "__main__":
    workers = cpu_count()-1
    N_total = 50_000_000

    chunk_size = N_total // workers
    ranges = []
    start = 1
    for w in range(workers):
        end = start + chunk_size
        if w == workers - 1:
            end = N_total + 1
        ranges.append((start, end))
        start = end
    
    with Pool(workers) as pool:
        results = pool.map(cpu_heavy_function, ranges)
        
    for r in results:
        os_id, elapsed, iters, chk = r
        print(f"Tiempo: {elapsed:.3f} s — Iteraciones: {iters} — checksum: {chk:.6f}")
        