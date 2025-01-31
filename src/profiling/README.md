# Profiling Python code

## Setup

```bash
python3 -m venv .venv # You can also use conda or virtualenv, your choice
.venv\Scripts\activate # Windows
# source .venv/bin/activate # Linux/MacOS
# conda activate your-environment-name # Conda
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

## Comparison

`pyinstrument`:

- Sampling profiler
- Lower overhead
- Easier to use
- Built-in visualization
- Good for quick, high-level analysis
- May miss very short function calls

`cProfile` with `snakeviz`:

- Deterministic profiler
- Higher overhead
- More detailed information
- Separate visualization tool (snakeviz)
- Captures all function calls
- Better for in-depth analysis

Choose pyinstrument for quick, low-impact profiling, and cProfile with snakeviz for comprehensive, detailed analysis.
