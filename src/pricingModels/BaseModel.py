from abc import ABC, abstractmethod

class OptionPricingModel(ABC):
    """
    Abstract base class for option pricing models.
    Enforces interface: all pricing models must implement price().
    """

    def __init__(self, S, K, r, T, sigma):
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma

    @abstractmethod
    def price(self, optionType="call", **kwargs):
        """
        Compute the option price.
        Must be implemented by subclasses.
        """
        pass
