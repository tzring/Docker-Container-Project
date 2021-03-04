#!/usr/bin/env python
# pylint: disable=no-value-for-parameter
import click


@click.command()
@click.option("--change", prompt="Amount for change:", help="Amount for change.")
def change_func(change):
    coin = [0.01, 0.05, 0.1, 0.25]
    coin_t = ['penny', 'nickel', 'dime', 'quarter']
    n = len(coin)
    change = float(change)
     
    ans = []
 
    i = n - 1
    while(i >= 0):
         
        while (round(change,2) >= coin[i]):
            change -= coin[i]
            ans.append(coin[i])
 
        i -= 1
 
    # Print result
    print("You will get:")
    for n, i in enumerate(coin_t):
        print(ans.count(coin[n]), i)


if __name__ == "__main__":
    change_func()
