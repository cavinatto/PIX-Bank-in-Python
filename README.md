# PIX-Bank-in-Python
This project simulates a simple banking system using **Object-Oriented Programming (OOP)**. It allows clients to perform PIX transactions, including deposits, withdrawals, and transfers. The goal is to practice OOP concepts such as classes, encapsulation, and object interaction.

## Features

- **Client Registration**: Create clients with their name, CPF, and initial balance.
- **Deposits and Withdrawals**: Clients can deposit and withdraw funds.
- **PIX Transfers**: Perform PIX transactions between clients.
- **Bank Statement**: Each client can access their transaction history.

## Object-Oriented Programming (OOP) Concepts

This project was developed using **Object-Oriented Programming (OOP)** principles, which provide an organized, modular, and maintainable structure. The key OOP concepts applied are:

- **Classes and Objects**:
  - The entities in the system are represented by **classes**, such as `Cliente` and `Pix`. Each client and each transaction is an **object** of these classes, encapsulating their data and behaviors.

- **Encapsulation**:
  - The `Cliente` class has private attributes (such as `__cpf`, `__saldo`, and `__extrato`) that can only be accessed or modified via public methods. This ensures that a client's internal data is protected from unauthorized changes.

- **Methods**:
  - The classes have **methods** that define the behavior of objects. For example, the `depositar()` method adds balance to a client, while the `realizar_pix()` method executes a PIX transfer.

- **Interaction Between Objects**:
  - The interaction between `Cliente` and `Pix` objects allows clients to perform transactions. The `Pix` object handles the transfer, updating the balance of the involved clients and recording the transaction in their statements.

- **Modularity**:
  - The code is divided into separate files, each responsible for a specific functionality: `client.py` (for the `Cliente` class), `pix.py` (for the `Pix` class), and `main.py` (for the main program control). This makes the code easier to read and maintain.
