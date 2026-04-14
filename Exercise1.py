import matplotlib.pyplot as plt
def erlang_b(A, C):
    """
    Calculates the Erlang B blocking probability.
    A: Offered traffic in Erlangs
    C: Number of channels
    """
    inv_B = 1.0
    for k in range(1, C + 1):
        inv_B = 1.0 + inv_B * (k / A)
    
    return 1.0 / inv_B


# Parameters
A = 25 # Offered traffic in Erlangs

# We generate a list of channel numbers. 
# We'll plot from 15 up to 45 to see the curve drop clearly.
channels = list(range(15, 46)) 
probabilities = [erlang_b(A, c) for c in channels]

# Plotting the curve
plt.figure(figsize=(10, 6))
plt.plot(channels, probabilities, marker='o', markersize=4, linestyle='-', color='b')

# Adding a reference line for 10^-2 (useful for the next step)
plt.axhline(y=0.01, color='red', linestyle='--', label='$10^{-2}$ Threshold')

# Formatting the plot
plt.yscale('log') # Log scale is standard for blocking probabilities
plt.title('Blocking Probability vs. Number of Channels (A = 25 Erlangs)')
plt.xlabel('Number of Channels (C)')
plt.ylabel('Blocking Probability ($P_B$)')
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

# Display the plot
plt.show()