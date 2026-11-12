class User {
	double userId;
	String name;

	User (double userId, String name) {
		this.name = name;
		this.userId = userId;
	}
}

class BankAccount {
	double accountId;
	double userId;
	double balance;

	BankAccount(double accountId, double userId) {
		this.accountId = accountId;
		this.userId = userId;
		this.balance = 0;
	}

	boolean deposit (double amount) {
		if (amount <= 0) {
			return false;
		}
		this.balance += amount;
		return true;
	}

	boolean withdraw (double amount) {
		if (amount <= 0 || amount > balance) {
			return false;
		}
		this.balance -= amount;
		return true;
	}

	double checkBalance() {
		return balance;
	}
}

public class Main {
	public static void main(String args[]) {
		User user = new User(1, "hirtih");
		BankAccount account = new BankAccount(101, user.userId);
		System.out.println(account.deposit(500));     // expect true
        System.out.println(account.deposit(-50));     // expect false
        System.out.println(account.withdraw(200));    // expect true
        System.out.println(account.withdraw(1000));   // expect false
        System.out.println(account.checkBalance());   // expect 300.0
	}
}
