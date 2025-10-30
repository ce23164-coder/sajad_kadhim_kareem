
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {'name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'price': [1200, 25, 75, 300],
        'quantity': [5, 20, 10, 8]}
df = pd.DataFrame(data)

df['total value'] = df['price'] * df['quantity']


print(df)


df_sorted = df.sort_values('total value', ascending=False)


print(df_sorted)


write_filename = "products.csv"
df_sorted.to_csv(write_filename, index=False)

print(f"\n--- 3. DataFrame saved to {write_filename} ---")

df_read = pd.read_csv(write_filename)


print(df_read)





plt.figure(figsize=(8, 4))
plt.bar(df_read['name'], df_read['total value'], color='skyblue')

plt.title("Total Values of Products")
plt.xlabel("Product Name")
plt.ylabel("Total Value")
plt.xticks(rotation=45, ha='right')

plt.show()