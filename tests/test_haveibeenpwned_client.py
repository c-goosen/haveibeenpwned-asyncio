import pytest
import time
from haveibeenpwned_asyncio import haveIbeenPwnedClient
from haveibeenpwned_asyncio.constants import haveibeenpwned

from collections.abc import Coroutine

from .conftest import MockResponse


class TesthaveIbeenPwnedClient:
    @pytest.fixture
    def urls_fixture(self):
        return [
            ("http://www.test.test/test1", "test1"),
            ("http://www.test.test/test2", "test2"),
            ("http://www.test.test/test3", "test3"),
        ]

    @pytest.fixture
    def haveibeenpwned_client_fixture(self):
        return haveIbeenPwnedClient()

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("test", "test/test"),
            ("testing", "testing/testing"),
        ],
    )
    def test_generate_url(self, haveibeenpwned_client_fixture, test_input, expected):
        base_url = f"{haveibeenpwned.BASE_URL.value}{haveibeenpwned_client_fixture.api_version}"
        test_url = haveibeenpwned_client_fixture.generate_url(test_input, test_input)
        assert test_url == f"{base_url}/{expected}"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                haveIbeenPwnedClient(api_key="abcdef"),
                {
                    "user-agent": "haveibeenpwned-asyncio-PyPi-Package",
                    "hibp-api-key": "abcdef",
                },
            ),
            (
                haveIbeenPwnedClient(api_key="123456"),
                {
                    "user-agent": "haveibeenpwned-asyncio-PyPi-Package",
                    "hibp-api-key": "123456",
                },
            ),
        ],
    )
    async def test_prep_headers(self, test_input, expected):
        assert (
            await test_input.prep_headers(haveibeenpwned.HTTP_HEADER.value) == expected
        )

    @pytest.mark.asyncio
    async def test_queue_all_requeusts(
        self, mocker, urls_fixture, haveibeenpwned_client_fixture
    ):
        resp = MockResponse("", 200)
        mocker.patch("aiohttp.ClientSession.get", return_value=resp)

        tasks = await haveibeenpwned_client_fixture.queue_all_requeusts(
            urls=urls_fixture
        )
        assert len(tasks) == 3
        for x in range(0, 2):
            assert isinstance(tasks[x], Coroutine)
        # Cleanup coroutines
        for task in tasks:
            # task.cancel()
            await task

    @pytest.mark.asyncio
    async def test_gather_all_requests(self, haveibeenpwned_client_fixture):
        async def await_test_func(timer: int = 0):
            """
            Function only to mock a courotine
            """
            time.sleep(timer / 5)
            return timer

        asyncio_tasks = []
        for x in range(0, 5):
            asyncio_tasks.append(await_test_func(x))

        responses = await haveibeenpwned_client_fixture.gather_all_requests(
            asyncio_tasks=asyncio_tasks
        )

        assert len(responses) == 5
        for x in range(0, 5):
            assert responses[x] == x

    @pytest.mark.asyncio
    async def test_aiohttp_client_get(self, mocker):
        resp_body = "0000798DC29B019E225BC6853A6E4A6841C"
        base_url = f"{haveibeenpwned.BASE_URL.value}"
        endpoint = "/range/01C92"
        full_url = f"{base_url}{endpoint}"

        # Mock aiohttp response
        resp = MockResponse(resp_body, 200)
        mocker.patch("aiohttp_retry.RetryClient.get", return_value=resp)

        client = haveIbeenPwnedClient(semaphore_max=1, truncate_response=False)
        resp = await client.aiohttp_client_get(url=full_url, obj="01C92")

        assert resp[1] == 200
        assert resp_body in resp[2]
