from re import *

pattern="[ab]"

matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())