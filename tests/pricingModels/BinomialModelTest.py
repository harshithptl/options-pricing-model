import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from pricingModels.BinomialModel import BinomialModel

def test_call_price_converges_to_black_scholes():
    model = BinomialModel(S=100, K=100, r=0.05, T=1, sigma=0.2, N=500)
    price = model.price(optionType="call")
    expected_bs = 10.4506
    assert math.isclose(price, expected_bs, rel_tol=0.02)

def test_put_price_converges_to_black_scholes():
    model = BinomialModel(S=100, K=100, r=0.05, T=1, sigma=0.2, N=500)
    price = model.price(optionType="put")
    expected_bs = 5.5735
    assert math.isclose(price, expected_bs, rel_tol=0.02)

def test_invalid_option_type():
    model = BinomialModel(S=100, K=100, r=0.05, T=1, sigma=0.2, N=100)
    try:
        model.price(optionType="invalid")
        assert False
    except ValueError:
        pass

def test_american_call_equals_european_no_dividends():
    model = BinomialModel(S=100, K=100, r=0.05, T=1, sigma=0.2, N=500)
    euro_price = model.price(optionType="call", american=False)
    amer_price = model.price(optionType="call", american=True)
    assert math.isclose(euro_price, amer_price, rel_tol=1e-3)

def test_american_put_higher_than_european():
    model = BinomialModel(S=100, K=100, r=0.05, T=1, sigma=0.2, N=500)
    euro_put = model.price(optionType="put", american=False)
    amer_put = model.price(optionType="put", american=True)
    assert amer_put >= euro_put

