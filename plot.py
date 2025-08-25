import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

# Load f2.mat file
f2 = sio.loadmat("data/f2.mat")
data = f2["var"]

# Extract every 5th value
data_sampled = data[:, ::5]

# First row is time
time = data_sampled[0, :]
signals = data_sampled[1:, :]  # Rows 2-7

# Signal definitions
signal_info = [
    {'name': 'Travel (x)', 'ylabel': 'Travel [rad]', 'color': 'blue'},
    {'name': 'Travel Rate (ẋ)', 'ylabel': 'Travel Rate [rad/s]', 'color': 'green'},
    {'name': 'Pitch (θ)', 'ylabel': 'Pitch [rad]', 'color': 'red'},
    {'name': 'Pitch Rate (θ̇)', 'ylabel': 'Pitch Rate [rad/s]', 'color': 'orange'},
    {'name': 'Elevation (φ)', 'ylabel': 'Elevation [rad]', 'color': 'purple'},
    {'name': 'Elevation Rate (φ̇)', 'ylabel': 'Elevation Rate [rad/s]', 'color': 'brown'}
]

# Create separate figure for each signal
for i in range(6):
    plt.figure(figsize=(10, 6))
    plt.plot(time, signals[i, :], color=signal_info[i]['color'], linewidth=1.5)
    plt.title(f'Helicopter {signal_info[i]["name"]} vs Time', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel(signal_info[i]['ylabel'], fontsize=12)
    plt.grid(True, alpha=0.7)
    plt.tight_layout()
    
    # Save each plot
    filename = f"helicopter_{signal_info[i]['name'].lower().replace(' ', '_').replace('(', '').replace(')', '').replace('ẋ', 'x_dot').replace('θ̇', 'theta_dot').replace('φ̇', 'phi_dot').replace('θ', 'theta').replace('φ', 'phi')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')

plt.show()
