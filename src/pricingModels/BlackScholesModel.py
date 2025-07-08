from pricingModels.BaseModel import OptionPricingModel
import numpy as np
from scipy.stats import norm

class BlackScholesModel(OptionPricingModel):
    """
    Black-Scholes model for European option pricing.
    """

    def __init__(self, S: float, K: float, r: float, T: float, sigma: float):
        """
        Initialize model parameters.

        Parameters:
            S (float): Spot price of the underlying
            K (float): Strike price
            r (float): Risk-free interest rate
            T (float): Time to maturity (in years)
            sigma (float): Volatility (annualized)
        """
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma

    def _d1(self) -> float:
        """
        Compute d1 in the Black-Scholes formula.
        """
        if self.T <= 0:
            return 0
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def _d2(self) -> float:
        """
        Compute d2 in the Black-Scholes formula.
        """
        return self._d1() - self.sigma * np.sqrt(self.T)

    def price(self, optionType: str = "call") -> float:
        """
        Compute the Black-Scholes price for a European call or put.

        Parameters:
            optionType (str): "call" or "put"

        Returns:
            float: Option price
        """
        if self.T <= 0:
            if optionType == "call":
                return max(self.S - self.K, 0)
            elif optionType == "put":
                return max(self.K - self.S, 0)
            else:
                raise ValueError("optionType must be 'call' or 'put'")

        d1 = self._d1()
        d2 = self._d2()

        if optionType == "call":
            price = self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        elif optionType == "put":
            price = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        else:
            raise ValueError("optionType must be 'call' or 'put'")

        return price
    
    def delta(self, optionType: str = "call") -> float:
        d1 = self._d1()
        if optionType == "call":
            return norm.cdf(d1)
        elif optionType == "put":
            return norm.cdf(d1) - 1
        else:
            raise ValueError("optionType must be 'call' or 'put'")

    def gamma(self) -> float:
        d1 = self._d1()
        return norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self) -> float:
        d1 = self._d1()
        return self.S * norm.pdf(d1) * np.sqrt(self.T)

    def theta(self, optionType: str = "call") -> float:
        d1 = self._d1()
        d2 = self._d2()
        pdf_d1 = norm.pdf(d1)
        if optionType == "call":
            theta = (- (self.S * pdf_d1 * self.sigma) / (2 * np.sqrt(self.T))
                     - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2))
        elif optionType == "put":
            theta = (- (self.S * pdf_d1 * self.sigma) / (2 * np.sqrt(self.T))
                     + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2))
        else:
            raise ValueError("optionType must be 'call' or 'put'")
        return theta

    def rho(self, optionType: str = "call") -> float:
        d2 = self._d2()
        if optionType == "call":
            return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2)
        elif optionType == "put":
            return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2)
        else:
            raise ValueError("optionType must be 'call' or 'put'")
