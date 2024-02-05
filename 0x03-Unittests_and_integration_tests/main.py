from utils import access_nested_map, get_json

print(access_nested_map({"a": {"b": {"c": 1}}}, ["a", "b", "c"]))
print(access_nested_map(nested_map={"a": 1}, path=("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
