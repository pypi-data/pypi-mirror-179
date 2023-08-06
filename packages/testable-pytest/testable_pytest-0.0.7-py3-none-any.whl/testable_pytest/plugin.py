import pytest


@pytest.fixture
def testable_case(request: pytest.FixtureRequest):
    print(request.node.name)
