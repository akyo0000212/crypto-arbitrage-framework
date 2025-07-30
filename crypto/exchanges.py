import ccxt

exchanges = {
    'binance': ccxt.binance(),
    'kucoin': ccxt.kucoin2(),
    'bittrex': ccxt.bittrex(),
}
for i in {1..5}
do
    echo "Commit number $i" >> log.txt
    git add log.txt
    git commit -m "Add log entry #$i

Co-authored-by: $ali000212 <$adamwilson0126@gmail.com>"
done