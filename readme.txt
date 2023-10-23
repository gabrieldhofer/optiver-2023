
definitions
-----------

basis point: equivalent to a 0.01% price move

bucket: 

wap: weighted average price

  ((bidprice * asksize) + (askprice * bidsize)) / (bidsize + asksize)

[bid/ask]_price: Price of the most competitive buy/sell level in the non-auction book.

[bid/ask]_size: the dollar notional amount on the most competitive buy-sell level in the non-auction book.

target: 60 second future move in the wap of the stock minus 60 second future move of the synthetic index

synthetic index: custom weighted index of Nasdaq-listed stocks constructed by Optiver..

revealed_targets When the first time_id for each date (i.e. when seconds_in_bucket equals zero) the API will serve a dataframe providing the true target values for the entire previous date. All other rows contain null values for the columns of interest.

