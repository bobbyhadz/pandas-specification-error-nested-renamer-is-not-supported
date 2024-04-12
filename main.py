# Pandas SpecificationError: nested renamer is not supported

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 180.2, 190.3, 205.4],
})


series = df['salary'].agg(min='min', max='max')

# min    175.1
# max    205.4
# Name: salary, dtype: float64
print(series)

print(series[0])  # 👉️ 175.1
print(series[1])  # 👉️ 205.4