# External resources
import scipy.io as spo, matplotlib.pyplot as plt, scipy.fft as sfft, numpy as np

# Load the data

data_path = r"Q:\tutorials\MATLAB\FFT\FFT\MATLAB-FFT-Tutorial\time_series.mat"
file_object = spo.loadmat(data_path)

# Unpack the file object
time_axis = file_object["t"][0]
signal_voltage = file_object['s'][0]

# Define some constants
sample_frequency = file_object['fs'] # Hz

# Plot the time series

plt.subplot(2,1,1); plt.plot(time_axis, signal_voltage); plt.title('Time')

# Compute the transform of the signal

fft_raw = sfft.fft(signal_voltage)

# Start with the two sided spectrum

right_hand_side = fft_raw[round(len(fft_raw)/2):]

# Drop the complexity

mag_rhs = abs(right_hand_side/len(right_hand_side))

# Compute the single sided spectrum based on the dual-sided spectrum and the even-valued signal length L

single_sided_spectrum = 2*right_hand_side.copy()

# Define the frequency domain f

frequency_axis = sample_frequency*np.linspace(0, len(single_sided_spectrum))/len(single_sided_spectrum)

# Plot out the spectrum

plt.subplot(2,1,2); plt.plot(np.reshape(frequency_axis[:,0:45],(45)),
                                        np.abs(single_sided_spectrum)); plt.title("Frequency")
plt.show()

