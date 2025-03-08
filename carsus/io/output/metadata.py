class Metadata:
    def __init__(self):
        self.data = {}

    def add_entry(self, key, value):
        self.data[key] = value

    def update_entry(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError(f"Key '{key}' not found in metadata.")

    def get_entry(self, key):
        return self.data.get(key, None)

    def to_dataframe(self):
        import pandas as pd
        return pd.DataFrame(list(self.data.items()), columns=["Key", "Value"])
