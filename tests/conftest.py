import pytest
import asyncio

from aresponses import ResponsesMockServer


class MockResponse:
    def __init__(self, text, status):
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    # asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture
async def aresponses(loop):
    async with ResponsesMockServer(loop=loop) as server:
        yield server
