[![CI](https://github.com/piotrgredowski/python-code/actions/workflows/ci.yml/badge.svg)](https://github.com/piotrgredowski/python-code/actions/workflows/ci.yml)

# My Python code samples

For talks, presentations, workshops, demos.

## Setup

### Option 1

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.lock -r requirements-dev.lock
```

### Option 2

Install [rye](https://github.com/mitsuhiko/rye).

Run

```bash
rye sync
rye shell
```

## Cases

- [x] `doctest`
  - [src/clock_angle](src/clock_angle)


- [ ] mutation tests with `mutmut`
  - [src/clock_angle](src/clock_angle)
  - [tests/clock_angle/test_clock_angle.py](tests/clock_angle/test_clock_angle.py)
