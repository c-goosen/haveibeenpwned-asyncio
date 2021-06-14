# import pytest  # noqa
# import os
# from haveibeenpwned_asyncio import haveIbeenPwnedPasswords
#
# # @pytest.fixture
# # def test_query_acc_fixture():
# #     return haveIbeenPwnedAccount(
# #             accounts=['test@test.com', 'admin@gmail.com'],
# #             semaphore_max=10,
# #             api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
# #                               )
# @pytest.mark.asyncio
# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         ("test@1234", True),
#         ("test!1234", False),
#     ],
# )
# async def test_query_password(test_input,expected):
#     assert expected == await haveIbeenPwnedPasswords(
#         passwords=[test_input],
#         api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None)
#     ).query_passwords()
