from bank_accounts import*

A = BankAccount("A",1000)
B = BankAccount("B",2000)

A.getBalance()
B.getBalance()

A.deposit(100)
B.deposit(200)

A.withdraw(100)
B.withdraw(10000)

A.transfer(100,B)
B.transfer(100000,A)

C = InterestsAcc("C",400)
C.deposit(10)
C.transfer(10,A)

