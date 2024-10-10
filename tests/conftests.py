print("conftest.py loaded")

import pytest
from setup import driver_setup as ds

@pytest.fixture
def driver():
    driver = ds.init_driver()
    yield driver
    driver.quit()