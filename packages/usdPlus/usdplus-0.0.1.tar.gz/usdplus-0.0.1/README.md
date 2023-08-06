# OverPy.Fi

OverPy.Fi allows you to access realtime data from Overnight.fi.  

Overnight Finance is an Asset Management Protocol offering Low-Risk 
Passive Yield Products primarily for conservative stablecoin investors, 
both individuals and protocol treasuries.

This package was created to access data such as; strategies, payouts, APYs
network specific to what Overnight offers 




## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install usdpluspy.

```bash
pip install usdplus
```

## Usage
These are the symbols to use per network  

'o' = Optimism  
'm' = Matic  
'b' = Binance  
'a' = Avalanche

```python
from usdplus import USDPlus

matic_network = USDPlus('m')

for line in matic_network.payouts():
    print(line)

'''
First 5 rows of data

[{'id': {'strategyName': 'USD+', 'tokenName': 'USDC'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x2791bca1f2de4661ed88a30c99a7a9449aa84174', 'percentage': 47.0293, 'netAssetValue': 839401.182572, 'updateDate': '2022-12-02T09:35:04.330661'}, {'id': {'strategyName': 'USD+', 'tokenName': 'USDT'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f', 'percentage': 3.4422, 'netAssetValue': 61437.194341, 'updateDate': '2022-12-02T09:35:04.33139'}, {'id': {'strategyName': 'USD+', 'tokenName': 'DAI'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063', 'percentage': 18.3381, 'netAssetValue': 327306.467433, 'updateDate': '2022-12-02T09:35:04.332155'}, {'id': {'strategyName': 'USD+', 'tokenName': 'WETH'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.33288'}, {'id': {'strategyName': 'USD+', 'tokenName': 'WMATIC'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.333609'}, {'id': {'strategyName': 'USD+', 'tokenName': 'aUSDC'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x625E7708f30cA75bfd92586e17077590C60eb4cD', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.334287'}, {'id': {'strategyName': 'USD+', 'tokenName': 'USD+'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.335375'}, {'id': {'strategyName': 'USD+', 'tokenName': 'nUSD'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0xb6c473756050de474286bed418b77aeac39b02af', 'percentage': 1.4967, 'netAssetValue': 26713.676041, 'updateDate': '2022-12-02T09:35:04.336119'}, {'id': {'strategyName': 'USD+', 'tokenName': 'TUSD'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x2e1ad108ff1d8c782fcbbb89aad783ac49586756', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.336857'}, {'id': {'strategyName': 'USD+', 'tokenName': 'USDC (delta-neutral)'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x2791bca1f2de4661ed88a30c99a7a9449aa84174', 'percentage': 29.7005, 'netAssetValue': 530108.236685, 'updateDate': '2022-12-02T09:35:04.33764'}, {'id': {'strategyName': 'USD+', 'tokenName': 'WBTC'}, 'strategyAddress': '0x236eeC6359fb44CCe8f97E99387aa7F8cd5cdE1f', 'tokenAddress': '0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6', 'percentage': 0.0, 'netAssetValue': 0.0, 'updateDate': '2022-12-02T09:35:04.33841'}]
{'transactionHash': '0xca14638182f43ddeb6acdde5b2e265c651992338bb547a6817aa379041f6cf45', 'payableDate': '2022-12-02T05:30:51', 'dailyProfit': 0.000158, 'annualizedYield': 6.3584470185, 'totalUsdPlus': 1801092.953976, 'totalUsdc': 1801092.953976, 'duration': 22.463611111}
{'transactionHash': '0x4210f6151e2d47a39a524d7b45bba5e41887b413ad00156e21cd90b51acc5248', 'payableDate': '2022-12-01T07:03:02', 'dailyProfit': 0.00035, 'annualizedYield': 13.6338182201, 'totalUsdPlus': 1796862.569403, 'totalUsdc': 1796862.569403, 'duration': 23.98}
{'transactionHash': '0xc4747ff27990da0d7de6152b961711cdbe655eab3c7fb349f08c44a73b91c083', 'payableDate': '2022-11-30T07:04:14', 'dailyProfit': 0.000271, 'annualizedYield': 11.1753411977, 'totalUsdPlus': 1796907.032724, 'totalUsdc': 1796907.032724, 'duration': 22.425833333}
{'transactionHash': '0xf996e7db3729b1d857638fc0830e66b2ce8d1d58f2a29563b02f3a56cbf4fef7', 'payableDate': '2022-11-29T08:38:41', 'dailyProfit': 0.000238, 'annualizedYield': 8.4902799174, 'totalUsdPlus': 1815534.162905, 'totalUsdc': 1815534.162905, 'duration': 25.630555555}
. . . . .
. . . . . 
. . . . . 

'''
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)