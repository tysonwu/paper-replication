# paper-replication
 Replicating results and findings from the paper "Risks and Returns of Cryptocurrency by Liu & Tsyvinski (2018).

 Their original paper is available at https://economics.yale.edu/sites/default/files/files/Faculty/Tsyvinski/cryptoreturns%208-7-2018.pdf.

## Introduction

Inspired by the paper ‘Risks and Returns of Cryptocurrency’ by Liu and Tsyvinski (2018), this project replicates some of the results from the original paper, as well as extending the results to a few more cryptocurrencies in the market. The methodologies used are same as in the original paper.

## Data Collection

We focus on the following cryptocurrencies, which are high-ranked in terms of their asset price:

- Bitcoin (BTC)
- Ethereum (ETH)
- XRP (XRP)
- Bitcoin Cash (BCH)
- Litecoin (LTC)
- EOS (EOS)
- Stellar (XLM)

The price data are collected from Coin Metrics (https://coinmetrics.io/data-downloads/) and CoinDesk (https://coindesk.com/data). The data collected is different in collection period as price data of earlier dates (2011-2013) are neither unavailable in the above websites (nor in other free cryptocurrency sites).

Data on Twitter mentions are unavailable on the Internet, hence skipped.

Data on Bitcoin Wallet users are obtained from Quandl, validated by blockchain.info (https://quandl.com/data/BCHAIN/MWNUS-Bitcoin-My-Wallet-Number-of-Users).

Data on Google searches are obtained from Google (https://trends.google.com/trends). Popularity of searches are scored in the scale of 1-100 with 100 assigned to the date point with maximum popularity in the selected time frame.