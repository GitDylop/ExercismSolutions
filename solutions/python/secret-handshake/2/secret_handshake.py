import sys

def commands(binary_str):
    handshake = []

    if binary_str[-1] == "1":
        handshake.append("wink")
    if binary_str[-2] == "1":
        handshake.append("double blink")
    if binary_str[-3] == "1":
        handshake.append("close your eyes")
    if binary_str[-4] == "1":
        handshake.append("jump")
    if binary_str[-5] == "1":
        reversed_handshake = []
        for action in range(len(handshake)):
            reversed_handshake.append(handshake[-1 - action])

        return reversed_handshake

    return handshake
