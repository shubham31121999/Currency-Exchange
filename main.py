from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# API Base URLs
PRIMARY_API_BASE = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@"
FALLBACK_API_BASE = "https://{date}.currency-api.pages.dev/"

# Set up templates
templates = Jinja2Templates(directory="templates")

# Function to fetch currency data
async def fetch_currency_data(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error fetching data: {str(e)}"}

# Home Page with Currency Converter
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    currencies_url = f"{PRIMARY_API_BASE}latest/v1/currencies.json"
    currencies = await fetch_currency_data(currencies_url)

    # Fallback if primary API fails
    if "error" in currencies:
        fallback_url = f"{FALLBACK_API_BASE.replace('{date}', 'latest')}v1/currencies.json"
        currencies = await fetch_currency_data(fallback_url)

    # Fetch USD conversion rates for top 5 strongest and weakest
    usd_rates_url = f"{PRIMARY_API_BASE}latest/v1/currencies/usd.json"
    usd_rates = await fetch_currency_data(usd_rates_url)

    if "error" in usd_rates:
        fallback_usd_url = f"{FALLBACK_API_BASE.replace('{date}', 'latest')}v1/currencies/usd.json"
        usd_rates = await fetch_currency_data(fallback_usd_url)

    usd_rates = usd_rates.get("usd", {})

    # Get strongest (lowest value) and weakest (highest value) currencies
    sorted_rates = sorted(usd_rates.items(), key=lambda x: x[1])
    strongest = sorted_rates[:5]   # Top 5 with lowest conversion rate
    weakest = sorted_rates[-5:]    # Top 5 with highest conversion rate

    return templates.TemplateResponse("index.html", {
        "request": request,
        "currencies": currencies,
        "result": None,
        "strongest": strongest,
        "weakest": weakest
    })

# Handle Currency Conversion Request
@app.post("/", response_class=HTMLResponse)
async def convert_currency(
    request: Request,
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    conversion_url = f"{PRIMARY_API_BASE}latest/v1/currencies/{from_currency}.json"
    data = await fetch_currency_data(conversion_url)

    # Fallback if primary API fails
    if "error" in data:
        fallback_url = f"{FALLBACK_API_BASE.replace('{date}', 'latest')}v1/currencies/{from_currency}.json"
        data = await fetch_currency_data(fallback_url)

    # Calculate the conversion
    if to_currency in data.get(from_currency, {}):
        rate = data[from_currency][to_currency]
        converted_amount = round(amount * rate, 2)
        result = f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}"
    else:
        result = f"Conversion rate from {from_currency} to {to_currency} not available."

    # Fetch currency and USD rates again for the dropdown and strong/weak currencies
    currencies_url = f"{PRIMARY_API_BASE}latest/v1/currencies.json"
    currencies = await fetch_currency_data(currencies_url)

    usd_rates_url = f"{PRIMARY_API_BASE}latest/v1/currencies/usd.json"
    usd_rates = await fetch_currency_data(usd_rates_url)

    if "error" in usd_rates:
        fallback_usd_url = f"{FALLBACK_API_BASE.replace('{date}', 'latest')}v1/currencies/usd.json"
        usd_rates = await fetch_currency_data(fallback_usd_url)

    usd_rates = usd_rates.get("usd", {})

    sorted_rates = sorted(usd_rates.items(), key=lambda x: x[1])
    strongest = sorted_rates[:5]
    weakest = sorted_rates[-5:]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "currencies": currencies,
        "result": result,
        "strongest": strongest,
        "weakest": weakest
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
