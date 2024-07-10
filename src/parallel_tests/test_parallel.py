import datetime
import logging
import time

import pytest

logging.basicConfig(format="%(message)s")


@pytest.mark.parametrize("n", [10, 20, 30, 40])
def test_it(n):
    n = n/2
    i = 0
    while True:
        if i == n:
            break

        logging.warning(f"{datetime.datetime.now().isoformat()} {n} Slept {i}/{n} seconds")
        time.sleep(1)
        i += 1

    assert n > 0
