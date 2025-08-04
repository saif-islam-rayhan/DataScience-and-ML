# Create data with duplicates
import pandas as pd
data = {
    'ID': [101, 102, 101, 104, 102],
    'Product': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Price': [50, 30, 50, 80, 30]
}
df = pd.DataFrame(data)

print("\nDuplicate rows:")
print(df[df.duplicated()])

# Remove duplicates keeping first occurrence
clean_df = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(clean_df)

# Remove duplicates based on specific columns
clean_df = df.drop_duplicates(subset=['ID'])
print("\nAfter removing duplicates by ID:")
print(clean_df)