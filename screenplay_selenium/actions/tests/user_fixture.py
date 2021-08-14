import pytest
from screenplay import Actor
from screenplay_selenium.abilities import browse_the_web


@pytest.fixture
def user():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())
    yield user
    user.clean_up()
