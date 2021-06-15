import os
from haveibeenpwned_asyncio import haveIbeenPwnedPasswords, haveIbeenPwnedAccount
import asyncio

if __name__ == "__main__":
    # Validation Class, inherits from Indentity Class
    loop = asyncio.get_event_loop()
    passwords = ["test@1234", "test$1234"]
    accounts = ["admin@gmail.com", "test@test.com"]

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
