import math
from pricingModels.MonteCarloModel import MonteCarloModel

def test_monte_carlo_call_price():
    model = MonteCarloModel(100, 100, 0.05, 1, 0.2, n_sims=100_000)
    price = model.price(optionType="call")
    assert price > 5 and price < 20  # very loose bounds

def test_monte_carlo_put_price():
    model = MonteCarloModel(100, 100, 0.05, 1, 0.2, n_sims=100_000)
    price = model.price(optionType="put")
    assert price > 1 and price < 15
