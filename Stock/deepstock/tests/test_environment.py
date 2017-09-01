import pytest
import logging

from deepstock.environment import Environment

LOGGER = logging.getLogger(__name__)

@pytest.fixture
def environment():
    return Environment(['AAPL', 'IBM', 'GOOG'])


def test_init(environment: Environment):
    # buy1...buy10,sell1...sell10,skip1...skip10
    assert len(environment.action_space) == 90
