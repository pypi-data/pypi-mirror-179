# algoql
Algorand streaming Query Language

## Usage
````commandline
python main.py <query>
````

### Get current block round
``` sql
SELECT b.rnd FROM block AS b;
```
Output:
```
{'rnd': 25242464}
{'rnd': 25242465}
```

### Get decoded transaction notes:
``` sql
SELECT BASE64DECODE(txns.txn.note, "utf-8") AS note FROM block.txns AS txns WHERE BASE64DECODE(txns.txn.note, "utf-8") IS NOT NULL;
```
Output:
```
{'note': 'Reach 0.1.11'}
```