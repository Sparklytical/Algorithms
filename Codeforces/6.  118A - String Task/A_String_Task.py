import re
n = input()
n = re.sub("[aeiouy]*([^aeiouy])[aeiouy]*", r".\1", n.lower())
print(n)
