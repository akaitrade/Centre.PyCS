# Centre.PyCS
# ![Icon](https://centr.tech/wp-content/uploads/CENTR-Concept-Logo-1.png) Centre.PyCS
Third Party Library for implementing Credits Blockchain in Python

## Installation of PIP
```
pm> pip install Centr.PyCS 
```
Or
```
pm> pip3 install Centr.PyCS 
```

## Getting started

After installing it's time to actually use it. To get started we have to add the PyCS namespace:  `Import Connector from PyCS;`.

Centre is providing an easy way of connecting to the Credits Blockchain where the goal is to limit the time needed for new Developers intergrating the Credits Blockchain into there projects

## Detailed Documentation

For All Centre build Libraries there is detailed documentation which can be found here:
https://centr.gitbook.io/netcs

## Connector Object

In order to get the library working we first need to initialize the Connector object
```csharp
connect_ = Connector("95.111.224.219:9091");
```
The Connector object needs to have 2 variables the first: IP address of a node running Credits Blockchain and Second: the API port of that particular node.

## Examples
Retrieving Balance
--
For a very easy example we are going to retrieve a Balance of a give wallet address
```csharp
var connect_ = new Connector("95.111.224.219", 9091);
var balance = connect_.balance("4SFfA1S2xfA3BdgkTn2tK14yDhLuD11RVz78kqx35jct");
```
With only 2 Lines of code we can now retrieve a balance from the blockchain that easy !

Sending Transaction
--
In the next example we are going to send an transaction with the native currency CS
```csharp
var connect_ = new Connector("95.111.224.219", 9091);
Console.WriteLine(connect_.SendTransaction(1, 0, "Enter Sender Publickey", "Enter Sender Privatekey", "Enter Receiver Publickey"));
```
Well look at that ! You now sended an transaction on the Credits Blockchain great job ;)

## Contribution

Everyone is free to help me out as this will be a community driven Library !
