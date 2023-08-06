# finhelp
## _Helping simplify finance_

A python package to make financial calculations simple. 

The package provides a wide range of tools and calculators designed specifically for financial applications.

## Features

- Net Income
- Simple Interest 
- Compound Interest 
- Inflation adjusted price 
- Purchasing Power
- Compounded Annual Growth Rate (CAGR)


## Example to use 

+ Compound Interest

```Python
# To calculate compound interest for 
# principal amount of 100000 invested for 10 years 
# at an interest rate of 10 per cent and the 
# compounding is annual.
from finhelp import compound_interest

print( compound_interest( 100000, 0.1, 10, 1))
# 159374.25
# The compounded interest earned is 159374.25  
```

+ Purchasing Power

```Python
# To determine the purchasing power 
# of the amount of 10,000 in future
from finhelp import purchasing_power

print( round( purchasing_power( 10000, 0.05, 10)))
# 6139
# The value of 10,000 will decline to
#  6139 in 10 years 
# if inflation is 5 per cent. 
```


