import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Our dataset — house sizes and prices
data = {
    'size_sqft': [500, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    'price_lakhs': [25, 40, 50, 60, 75, 85, 90, 100, 110, 130]
}

df = pd.DataFrame(data)
print(df)
print(f"\nShape: {df.shape}")
print("\nBasic Stats:")
print(df.describe())
