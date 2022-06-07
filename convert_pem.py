A = "MIIEpAIB" * 15

n = len(A)
sep = list(range(0, n, 64))
lines = []
for i in range(len(sep) - 1):
    lines.append(A[sep[i] : sep[i + 1]])
lines.append(A[sep[-1] :])
print("\n".join(lines))
