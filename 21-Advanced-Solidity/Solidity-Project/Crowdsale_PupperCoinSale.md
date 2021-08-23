#   How to Crowdsale our PupperCoin
## ---------------------------------------------------------------------------------------------

## Background

Your company has decided to crowdsale their PupperCoin token in order to help fund the network development.
This network will be used to track the dog breeding activity across the globe in a decentralized way, and allow humans to track the genetic trail of their pets. You have already worked with the necessary legal bodies and have the green light on creating a crowdsale open to the public. However, you are required to enable refunds if the crowdsale is successful and the goal is met, and you are only allowed to raise a maximum of 300 Ether. The crowdsale will run for 24 weeks.



### Creating your project
#### 1) Create PupperCoin Contract
Using Remix, create a file called `PupperCoin.sol` and create a standard `ERC20Mintable` token. Since you're already an expert at this, you can simply use this [starter code](../Starter-Code/PupperCoin.sol).

![crowd](Images/01_PupperCompile.png)


#### 2) Create Crowdsale Contract

Leverage the [Crowdsale](../Starter-Code/Crowdsale.sol) starter code, saving the file in Remix as `Crowdsale.sol`.

You will need to bootstrap the contract by inheriting the following OpenZeppelin contracts:

* `Crowdsale`

* `MintedCrowdsale`

* `CappedCrowdsale`

* `TimedCrowdsale`

* `RefundablePostDeliveryCrowdsale`

![crowd](Images/02_Crowdsale.png)


When passing the `open` and `close` times, use `now` and `now + 24 weeks` to set the times properly from your `PupperCoinCrowdsaleDeployer` contract.

#### 4) PupperCoinCrowdsaleDeployer
![crowd](Images/03_pupperDeployed.png)

### Testing the Crowdsale: Localhost8545


#### 1) Return PupperCoin and PupperSales Address
![crowd](Images/04_pupperTokenaddress.png)

#### 2) PupperCoin Token Contract
![crowd](Images/05_pupperTokensupply.png)

#### 3) PupperCoinSale contract deployed
![crowd](Images/06_pupperTokenSale.png)

#### 4) Mycrypto Token
![crowd](Images/09_pupper_mycrp.png)
-----------------------

### Testing the Crowdsale: Rinkeby Tesnet

![crowd](Images/06_pupperTokenSale.png)

1----

![crowd](Images/01_RinMetamask.png)

2----

![crowd](Images/02_Rin_Address.png)

3-----

![crowd](Images/03_Rin_coinsale.png)

4----

![crowd](Images/07_metamaskToken.png)
5
![crowd](Images/09_RinMetamask.png)
kMDItemIsScreenCapture:1