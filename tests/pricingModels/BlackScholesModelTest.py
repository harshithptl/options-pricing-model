from pricingModels.BlackScholesModel import BlackScholesModel
import math

def test_call_price_known_value():
    """
    Known textbook example:
    S = 100, K = 100, r = 0.05, T = 1, sigma = 0.2
    Call price ~10.4506
    """
    model = BlackScholesModel(S=100, K=100, r=0.05, T=1, sigma=0.2)
    price = model.price(optionType="call")
    expected = 10.4506
    assert math.isclose(price, expected, rel_tol=1e-4)

def test_put_price_known_value():
    """
    Same params, put price ~5.5735
    """
    model = BlackScholesModel(S=100, K=100, r=0.05, T=1, sigma=0.2)
    price = model.price(optionType="put")
    expected = 5.5735
    assert math.isclose(price, expected, rel_tol=1e-4)

def test_zero_time_to_expiry_call():
    """
    At expiry, call price = max(S - K, 0)
    """
    model = BlackScholesModel(S=120, K=100, r=0.05, T=0, sigma=0.2)
    price = model.price(optionType="call")
    expected = 20
    assert price == expected

def test_zero_time_to_expiry_put():
    """
    At expiry, put price = max(K - S, 0)
    """
    model = BlackScholesModel(S=80, K=100, r=0.05, T=0, sigma=0.2)
    price = model.price(optionType="put")
    expected = 20
    assert price == expected

def test_invalid_option_type():
    """
    Should raise ValueError for invalid optionType.
    """
    model = BlackScholesModel(S=100, K=100, r=0.05, T=1, sigma=0.2)
    try:
        model.price(optionType="invalid")
        assert False, "Expected ValueError for invalid optionType"
    except ValueError:
        pass

def test_delta_call():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    delta = model.delta(optionType="call")
    expected = 0.6368  # textbook value approx
    assert math.isclose(delta, expected, rel_tol=1e-4)

def test_delta_put():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    delta = model.delta(optionType="put")
    expected = -0.3632
    assert math.isclose(delta, expected, rel_tol=1e-4)

def test_gamma():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    gamma = model.gamma()
    expected = 0.018762
    assert math.isclose(gamma, expected, rel_tol=1e-4)

def test_vega():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    vega = model.vega()
    expected = 37.524 
    assert math.isclose(vega, expected, rel_tol=1e-4)

def test_theta_call():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    theta = model.theta(optionType="call")
    expected = -6.4140
    assert math.isclose(theta, expected, rel_tol=1e-4)

def test_theta_put():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    theta = model.theta(optionType="put")
    expected = -1.6578
    assert math.isclose(theta, expected, rel_tol=1e-4)

def test_rho_call():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    rho = model.rho(optionType="call")
    expected = 53.2325
    assert math.isclose(rho, expected, rel_tol=1e-4)

def test_rho_put():
    model = BlackScholesModel(100, 100, 0.05, 1, 0.2)
    rho = model.rho(optionType="put")
    expected = -41.8904
    assert math.isclose(rho, expected, rel_tol=1e-4)
