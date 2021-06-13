import pytest  # noqa
import os
from haveibeenpwned_asyncio import haveIbeenPwnedAccount

# @pytest.fixture
# def test_query_acc_fixture():
#     return haveIbeenPwnedAccount(
#             accounts=['test@test.com', 'admin@gmail.com'],
#             semaphore_max=10,
#             api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
#                               )
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("test@test.com", True),
        ("test@gmail.com", False),
    ],
)
async def test_query_account(test_input,expected):
    assert expected == await haveIbeenPwnedAccount(
        accounts=[test_input],
        semaphore_max=10,
        api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
    ).query_accounts()
