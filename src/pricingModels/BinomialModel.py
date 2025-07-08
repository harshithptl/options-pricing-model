import numpy as np

class BinomialModel:
    """
    Cox-Ross-Rubinstein Binomial Tree Model for European and American Option Pricing.
    """

    def __init__(self, S, K, r, T, sigma, N):
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.N = N

    def price(self, optionType="call", american=False):
        """
        Price a European or American option.

        Parameters:
            optionType (str): "call" or "put"
            american (bool): Whether option is American (early exercise)

        Returns:
            float: Option price
        """
        dt = self.T / self.N
        u = np.exp(self.sigma * np.sqrt(dt))
        d = 1 / u
        disc = np.exp(-self.r * dt)
        p = (np.exp(self.r * dt) - d) / (u - d)

        # Terminal prices
        ST = np.array([self.S * (u**j) * (d**(self.N - j)) for j in range(self.N + 1)])
        if optionType == "call":
            option_values = np.maximum(ST - self.K, 0)
        elif optionType == "put":
            option_values = np.maximum(self.K - ST, 0)
        else:
            raise ValueError("optionType must be 'call' or 'put'")

        # Backward induction
        for i in reversed(range(self.N)):
            ST = ST[:-1] / u  # move back one step
            option_values = disc * (p * option_values[1:] + (1 - p) * option_values[:-1])
            if american:
                if optionType == "call":
                    exercise = np.maximum(ST - self.K, 0)
                else:
                    exercise = np.maximum(self.K - ST, 0)
                option_values = np.maximum(option_values, exercise)

        return option_values[0]
