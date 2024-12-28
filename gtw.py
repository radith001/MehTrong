import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Buat fungsi gelombang sinus
def update_wave(frame, line, x):
    y = np.sin(2 * np.pi * (x - 0.01 * frame))  # Gelombang bergerak
    line.set_ydata(y)  # Perbarui data y
    return line,

# Pengaturan awal
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)  # Rentang x
y = np.sin(x)  # Nilai awal y
line, = ax.plot(x, y, lw=2, color='cyan')  # Gambar gelombang

# Styling plot
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')  # Latar belakang hitam
plt.axis('off')  # Sembunyikan sumbu

# Animasi
ani = animation.FuncAnimation(
    fig, update_wave, frames=200, fargs=(line, x), interval=20, blit=True
)

# Tampilkan
plt.show()
    