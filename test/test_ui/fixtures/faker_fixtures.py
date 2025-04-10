import allure
import pytest
from faker import Faker


@pytest.fixture
def fake_data():
    """
    Fixture that provides a Faker instance

    Returns:
        Faker: Instance with en_US locale
    """
    with allure.step("Initialize Faker"):
        fake = Faker("en_US")
    yield fake
