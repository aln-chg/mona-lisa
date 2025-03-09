import yfinance as yf

stock_id = "2330.TW"
stock = yf.Ticker(stock_id)

financials = stock.financials
balance_sheet = stock.balance_sheet
cashflow = stock.cashflow

print(financials)
print(balance_sheet)
print(cashflow)
