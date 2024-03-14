from moralis import evm_api

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjhlYWI4NTg0LWQwNWUtNGQyMi05ZTk0LTA2MTZhYjMwNzQ4OCIsIm9yZ0lkIjoiMzcyNjUxIiwidXNlcklkIjoiMzgyOTczIiwidHlwZUlkIjoiMDE4OWRiMjYtMWI1Yi00YmZjLWJkZjQtNmMyYjU5NmFjNGVjIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MDU0MjA0OTYsImV4cCI6NDg2MTE4MDQ5Nn0.aHyNmDlzRV4CNVbROmDpvaFtl2LmUdHf9TgT_oxQkkw"
params = {
    "address": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "chain": "eth"
}

result = evm_api.token.get_token_price(
    api_key=api_key,
    params=params,
)

historicalPrice = []
for to_block in range(16323500, 16323550, 10):
  params = {
    "address": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "chain": "eth",
    "to_block": to_block
  }
  result = evm_api.token.get_token_price(
    api_key=api_key,
    params=params,
  )
  historicalPrice.append(result)
print(historicalPrice)

print(result)