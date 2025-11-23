SELECT id,
       price,
       volume_24h,
       market_cap,
       last_updated
FROM public.bitcoin_quotes
LIMIT 1000;