"""
if there are N persons in a room, total number of handshakes will be (N-1)*N/2
"""
def totalHandshakes(n):
    return n * (n - 1) // 2

print(totalHandshakes(2))
print(totalHandshakes(3))
print(totalHandshakes(30))