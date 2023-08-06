# red-py-sdk

![](https://img.shields.io/pypi/pyversions/Django.svg)


### install

```
pip3 install red-py-sdk
```

### Usage

#### Import

```
from redpysdk import Reddio
```

#### Init object
Init the object, you can use 'testnet' or 'mainnet' to init the sdk
```
reddio = Reddio("testnet")
```

#### Get StarkKey Pair
##### Usage
```
get_stark_key_pair()
```
It will generate an random starkkey pair

##### Example
```
>>> reddio.get_stark_key_pair()
('0x395d1708ab0ee91efcb7f26a2f4fcbe20faf3c7390517667fed37b0e481882a', '0x5aa1b67a486b6564a2b6ae7426950c03dfe6991f9d34ea45b6b0be0672a1818')
```

#### Mint NFT
##### Usage
```
mintNFT(api_key, contract_address, stark_key, amount)
```
It will mint $amount tokens of $contract_address to $stark_key. first you need to register at dashboard(dashboard.reddio.com) to get your $api_key, and make sure you register the contract_address as ERC721M

##### Example
```
>>> reddio.mintNFT(your_api_key,"0xd60523fd920eb9b7eff3e115203e32d91de5cf59","0x1ccc27877014bc1a81919fc855ebbd1b874603283c9ea93397d970b0704e581","10")
[302808, 302809, 302810, 302811, 302812, 302813, 302814, 302815, 302816, 302817]
```


#### Get Balance

##### Usage

```
get_balances(stark_key, page=1, limit=10)
```
It will return the starkkey's balance. including ERC20/ETH/ERC721

##### Example

```
reddio.get_balances("0x6ecaebbe5b9486472d964217e5470380782823bb0d865240ba916d01636310a")
```




#### Transfer

##### Usage
```
transferNFT(stark_private_key, starkkey, receiver, token_type, contract, tokenID, expiration_timestamp=4194303)
```

parameters
- stark_private_key: The private key of layer2
- starkkey: The stark key of layer2
- receiver: The receiver, should be starkkey of other account
- token_type: ERC721 or ERC721M. if mint on layer2 then it should be ERC721M. else it should be ERC721
- tokenID: The token id
- expiration_timestamp: When will it expiration, it is unix timestamp/3600

##### Example

```
reddio.transferNFT('private_key', '0x6ecaebbe5b9486472d964217e5470380782823bb0d865240ba916d01636310a', '0x1ada455b26b246260b7fd876429289639d7a0ce5fe295ff2355bd4f4da55e2', 'ERC721', '0x941661Bd1134DC7cc3D107BF006B8631F6E65Ad5', '618'))
```

In the example, you should replace the 'private_key' to the private key of the starkkey




#### Withdrawal

##### Usage
```
withdrawNFT(stark_private_key, starkkey, receiver, token_type, contract, tokenID, expiration_timestamp=4194303)
```

parameters
- stark_private_key: the private key of layer2
- starkkey: the stark key of layer2
- receiver: the receiver, should be starkkey of other account
- token_type: ERC721 or ERC721M. if mint on layer2 then it should be ERC721M. else it should be ERC721
- tokenID: the token id
- expiration_timestamp: when will it expiration, it is unix timestamp/3600

##### Example

```
reddio.withdrawNFT('private_key', '0x6ecaebbe5b9486472d964217e5470380782823bb0d865240ba916d01636310a', '0xffc882996cFAB2C8B9983394E09bb025a98e52bc', 'ERC721', '0x941661Bd1134DC7cc3D107BF006B8631F6E65Ad5', '663')
```

In the example, you should replace the 'private_key' to the private key of the starkkey


#### Others
- buy_nft
- sell_nft







