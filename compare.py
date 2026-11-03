import timeit
from typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search


def read_file(filename: str) -> str:
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable[[str, str], int], text_: str, pattern_: str) -> float:
    return timeit.timeit(lambda: func(text_, pattern_), number=10)


if __name__ == '__main__':
    files = ['стаття 1.txt', 'стаття 2.txt']
    patterns = ("пошуку вимагає", "мама мила раму")
        
    results = []
    for filename in files:
        text = read_file(filename)
    
        for pattern in patterns:
            time = benchmark(boyer_moore_search, text, pattern)
            results.append((filename, boyer_moore_search.__name__, pattern, time))
            time = benchmark(kmp_search, text, pattern)
            results.append((filename, kmp_search.__name__, pattern, time))
            time = benchmark(rabin_karp_search, text, pattern)
            results.append((filename, rabin_karp_search.__name__, pattern, time))
    title = f"{'Файл':<20} | {'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for filename, algorithm, pattern, time in results:
        print(f"{filename:<20} | {algorithm:<30} | {pattern:<30} | {time}")