import pytest

from haveibeenpwned_asyncio import haveIbeenPwnedClient
from haveibeenpwned_asyncio.constants import haveibeenpwned


class TesthaveIbeenPwnedClient:
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
