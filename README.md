# Option Pricing Models

This repository implements three classic option pricing models in Python:

- ✅ **Black-Scholes Model**
- ✅ **Binomial Model (Cox-Ross-Rubinstein)**
- ✅ **Monte Carlo Simulation**

Each model is implemented as an object-oriented class inheriting from a shared abstract base class to ensure consistent interfaces. This design makes it easy to extend, test, and integrate these models for use in trading research and strategy development.

---
## 🔎 Models and Descriptions

### 1️⃣ Black-Scholes Model

**Description**:
A closed-form analytical formula for European options assuming constant volatility, log-normal asset prices, and continuous trading.

**Features**:
- European call and put pricing
- Greeks (Delta, Gamma, Vega, Theta, Rho)

**Pros**:
✅ Fast, closed-form solution  
✅ Widely used and well-understood  
✅ Greeks easily computed analytically  

**Cons**:
⚠️ Only valid for European options  
⚠️ Assumes constant volatility  
⚠️ Doesn't model early exercise or dividends directly  

---

### 2️⃣ Binomial Model (Cox-Ross-Rubinstein)

**Description**:
A discrete-time tree model that approximates option prices by modeling the underlying asset's possible paths over multiple periods.

**Features**:
- European and American option pricing
- Early exercise feature for American options

**Pros**:
✅ Handles American-style early exercise  
✅ Intuitive tree structure  
✅ Converges to Black-Scholes as steps increase  

**Cons**:
⚠️ Slower than closed-form solutions  
⚠️ Requires choosing number of steps (trade-off between accuracy and speed)  

---

### 3️⃣ Monte Carlo Simulation

**Description**:
Uses random sampling of asset price paths under risk-neutral measure to estimate the expected discounted payoff.

**Features**:
- European call and put pricing
- Simulates many random paths

**Pros**:
✅ Flexible and intuitive  
✅ Easily extended to exotic options  
✅ Handles complex payoffs  

**Cons**:
⚠️ Computationally intensive  
⚠️ Requires many simulations for accuracy  
⚠️ Not well-suited for American options without complex modifications  

---

## ⚙️ Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```