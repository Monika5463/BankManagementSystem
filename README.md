# Bank Management System

## Project Overview

The Bank Management System is a simple console-based application that allows users to perform various banking tasks such as opening new accounts, depositing and withdrawing money, checking balances, displaying customer details, and closing accounts. The application is built using Python and interacts with a MySQL database to store and manage account-related information.

## Features

1. **Open New Account:** Users can input customer details such as name, account number, date of birth, address, contact number, and opening balance to open a new account. The provided information is stored in the 'account' and 'amount' tables in the database.

2. **Deposit Amount:** Users can deposit money into their accounts by specifying the amount and account number. The application fetches the current balance from the database, updates it with the deposited amount, and stores the new balance.

3. **Withdraw Amount:** Users can withdraw money from their accounts by providing the withdrawal amount and account number. Similar to the deposit function, the application calculates and updates the account balance in the database.

4. **Balance Enquiry:** Users can check the balance of a particular account by entering the account number. The application retrieves and displays the account balance.

5. **Display Customer Details:** Users can view the details of a customer's account by providing the account number. The application fetches the relevant information from the 'account' table and displays it to the user.

6. **Close Account:** Users can close an account by specifying the account number. This action removes both the account details and the associated balance from the database.

## How to Run

1. Make sure you have Python and the MySQL connector library installed on your system.

2. Create a MySQL database named 'bank_management' with two tables named 'account' and 'amount'. The 'account' table should have columns for name, account number, date of birth, address, and contact number. The 'amount' table should have columns for account number and balance.

3. Update the `host`, `user`, `password`, and `database` fields in the code with your MySQL credentials.

4. Run the script in a Python environment.

5. The application will display a menu of options. Enter the corresponding number to perform the desired task.

## Future Improvements

- Implement better input validation and error handling.
- Provide more security measures to protect sensitive customer information.
- Add authentication mechanisms to ensure only authorized users can access the system.
- Develop a graphical user interface (GUI) to enhance user experience.

## Conclusion

The Bank Management System is a basic yet functional application that demonstrates fundamental concepts of database management and interaction using Python. It serves as a starting point for building more sophisticated banking systems and showcases the integration of programming and database technologies.
