
## Example Input and Output

### Example Input:

The program does not require user input during execution. The following client data and transactions are predefined in the code:

```python
# Client 1
cliente1 = Cliente("Maria", "123.456.789-00", 1000.0)

# Client 2
cliente2 = Cliente("João", "987.654.321-00", 500.0)

# Performing a PIX transfer from cliente1 to cliente2
cliente1.realizar_pix(200.0, cliente2)
```

### Example Output:

When running the program, the output will display the initial and updated balances, as well as the transaction history of each client:

```
Saldo do cliente Maria: R$1000.0
Saldo do cliente João: R$500.0

Saldo do cliente Maria: R$800.0
Saldo do cliente João: R$700.0

Remetente: 123.xxx.xxx-00
Destinatário: 987.xxx.xxx-00
Valor: R$200.0

Remetente: 123.xxx.xxx-00
Destinatário: 987.xxx.xxx-00
Valor: R$200.0
```

In this example:
- **Maria** starts with a balance of **R$1000.0**.
- **João** starts with a balance of **R$500.0**.
- After a **PIX transfer of R$200.0** from Maria to João:
  - **Maria’s** balance is updated to **R$800.0**.
  - **João’s** balance is updated to **R$700.0**.
  
The transaction is also recorded in the transaction history of both clients.

