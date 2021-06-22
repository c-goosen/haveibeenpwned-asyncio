import os
from haveibeenpwned_asyncio import haveIbeenPwnedPasswords, haveIbeenPwnedAccount, haveIbeenPwnedPastes
import asyncio

if __name__ == "__main__":
    # Validation Class, inherits from Indentity Class
    loop = asyncio.get_event_loop()
    passwords = ["P@ssw0rd"]
    accounts = ["admin@gmail.com", "test@test.com", "test@gmail.com"]

    print(
        loop.run_until_complete(
            haveIbeenPwnedPasswords(
                passwords=passwords, semaphore_max=10
            ).query_passwords()
        )
    )

    test_acc = haveIbeenPwnedAccount(
        accounts=accounts,
        semaphore_max=10,
        api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None),
    )
    print(loop.run_until_complete(test_acc.query_accounts()))
    print(test_acc.query_accounts_sync())

    test_pastes = haveIbeenPwnedPastes(
        accounts=accounts,
        semaphore_max=5,
        api_key=os.getenv("HAVEIBEENPWNED_API_KEY", None),
    )
    print(loop.run_until_complete(test_pastes.query_accounts()))
    print(test_pastes.query_accounts_sync())