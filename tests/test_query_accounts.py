# import pytest  # noqa
# import os
# from haveibeenpwned_asyncio import haveIbeenPwnedAccount
# from .conftest import MockResponse

# @pytest.fixture
# def test_query_acc_fixture():
#     return haveIbeenPwnedAccount(
#             accounts=['test@test.com', 'admin@gmail.com'],
#             semaphore_max=10,
#             api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
#                               )
# @pytest.mark.asyncio
# @pytest.mark.parametrize(
#     "test_input,resp_code,expected",
#     [
#         ("test@test.com", 200, True),
#         ("test@gmail.com", 404, False),
#     ],
# )
# async def test_query_account(mocker,test_input,resp_code, expected):
#     resp = MockResponse('[{"Name":"000webhost"},{"Name":"123RF"},{"Name":"17Media"}]', resp_code)
#     mocker.patch('aiohttp.ClientSession.get', return_value=resp)
#     resp == list(await haveIbeenPwnedAccount(
#         accounts=[test_input],
#         semaphore_max=10,
#         api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
#     ).query_accounts())
#     assert resp ==  test_input
#     assert resp ==  resp_code
#
