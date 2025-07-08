from pricingModels.BaseModel import OptionPricingModel
import numpy as np

class MonteCarloModel(OptionPricingModel):
    """
    Monte Carlo model for European option pricing.
    """

    def __init__(self, S, K, r, T, sigma, n_sims=10000):
        super().__init__(S, K, r, T, sigma)
        self.n_sims = n_sims

    def price(self, optionType="call", **kwargs):
        """
        Price a European option using Monte Carlo simulation.

        Parameters:
            optionType (str): "call" or "put"

        Returns:
            float: Estimated option price
        """
        if self.T <= 0:
            if optionType == "call":
                return max(self.S - self.K, 0)
            elif optionType == "put":
                return max(self.K - self.S, 0)
            else:
                raise ValueError("optionType must be 'call' or 'put'")

        # Simulate terminal prices
        z = np.random.normal(0, 1, self.n_sims)
        ST = self.S * np.exp((self.r - 0.5 * self.sigma ** 2) * self.T + self.sigma * np.sqrt(self.T) * z)

        if optionType == "call":
            payoffs = np.maximum(ST - self.K, 0)
        elif optionType == "put":
            payoffs = np.maximum(self.K - ST, 0)
        else:
            raise ValueError("optionType must be 'call' or 'put'")

        discounted_payoff = np.exp(-self.r * self.T) * np.mean(payoffs)
        return discounted_payoff
