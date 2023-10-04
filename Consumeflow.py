#data info
name = "Branin dataset"
url = "https://raw.githubusercontent.com/trentmc/branin/main/branin.arff"

#create data asset
(data_nft, datatoken, ddo) = ocean.assets.create_url_asset(name, url, {"from": alice})

#print
print("Just published asset:")
print(f"  data_nft: symbol={data_nft.symbol}, address={data_nft.address}")
print(f"  datatoken: symbol={datatoken.symbol}, address={datatoken.address}")
print(f"  did={ddo.did}")
