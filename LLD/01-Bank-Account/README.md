# Level 1: Bank Account

## Requirements
- An account is created with a user and a balance of 0.
- Deposit amount must be greater than 0.
- Withdraw amount must be greater than 0 and not more than the balance.
- Invalid deposits/withdrawals are rejected; balance is unchanged.
- The user can check their balance.

## Classes
- User: userId, name
- BankAccount: accountId, userId, balance
  - deposit(amount) -> boolean
  - withdraw(amount) -> boolean
  - checkBalance() -> double

## What I learned
- Boundary cases: withdrawing the exact balance must be allowed (> vs >=).
