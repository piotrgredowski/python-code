# Profiling Python code

## Setup

```bash
python3 -m venv .venv
.venv\Scripts\activate # Windows
# source .venv/bin/activate # Linux/MacOS
pip install pyinstrument snakeviz
```

## Sources

- https://docs.python.org/3/library/timeit.html
- https://docs.python.org/3/library/profile.html
- https://pyinstrument.readthedocs.io/en/latest/home.html
- https://realpython.com/python-profiling/#pyinstrument-take-snapshots-of-the-call-stack

## Profiling with pyinstrument

```bash
python -m pyinstrument --color --renderer=html --use-timing-thread --show-all --timeline --outfile _pyinstrument.profile.html src/profiling/primes.py
python -m pyinstrument --color --renderer=html --use-timing-thread --show-all --outfile _pyinstrument.profile.html src/profiling/primes.py
python -m pyinstrument --color --renderer=html --use-timing-thread --show-all --timeline src/profiling/primes.py
python -m pyinstrument src/profiling/primes.py
```

## Profiling with cProfile

```bash
python -m cProfile -o _profile_data.profile.pstats src/profiling/primes.py
python -m snakeviz _profile_data.profile.pstats
```
