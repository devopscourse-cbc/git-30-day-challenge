from utils import timestamp, format_name

result = timestamp()
assert isinstance(result, str)
print(f"Timestamp: {result}")

assert format_name("Jane", "Doe") == "Jane Doe"
print("All utility tests passed")
