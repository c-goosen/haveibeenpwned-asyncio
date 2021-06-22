import os
from haveibeenpwned_asyncio import (
    haveIbeenPwnedPasswords,
    haveIbeenPwnedAccount,
    haveIbeenPwnedPastes,
)
import asyncio

if __name__ == "__main__":
    # Validation Class, inherits from Indentity Class
    loop = asyncio.get_event_loop()
    passwords = ["P@ssw0rd"]
    accounts = ["admin@gmail.com", "test@test.com", "test@gmail.com"]

    test_passwords = haveIbeenPwnedPasswords(passwords=passwords, semaphore_max=10)
    print("\n>>>> test_passwords.query_accounts")
    print(loop.run_until_complete(test_passwords.query_passwords()))
    print("\n>>>> test_passwords.query_passwords_sync")
    print("\n\n")
    print(test_passwords.query_passwords_sync())
    print("\n\n")

    test_acc = haveIbeenPwnedAccount(
        accounts=accounts,
        semaphore_max=10,
        api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None),
    )
    print("\n>>>> test_acc.query_accounts")
    print(loop.run_until_complete(test_acc.query_accounts()))
    print("\n>>>> test_acc.query_accounts_sync")
    print("\n\n")
    print(test_acc.query_accounts_sync())
    print("\n\n")

    test_pastes = haveIbeenPwnedPastes(
        accounts=accounts,
        semaphore_max=5,
        api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None),
    )
    print("\n>>>> test_pastes.query_accounts")
    print(loop.run_until_complete(test_pastes.query_accounts()))
    print("\n>>>> test_pastes.query_accounts_sync")
    print("\n\n")
    print(test_pastes.query_accounts_sync())
    print("\n\n")
