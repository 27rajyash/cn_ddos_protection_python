import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Initialize data lists
cpu_data = []
memory_data = []
network_sent_data = []
network_recv_data = []
timestamps = []

# Initialize starting point for network data
net_io_start = psutil.net_io_counters()
start_time = time.time()

def monitor_resources():
    """
    Collect resource data and update lists.
    """
    global net_io_start
    
    # CPU and memory usage
    cpu_data.append(psutil.cpu_percent(interval=0))
    memory_data.append(psutil.virtual_memory().percent)

    # Network usage
    net_io = psutil.net_io_counters()
    bytes_sent = (net_io.bytes_sent - net_io_start.bytes_sent) / (1024 * 1024)  # Convert to MB
    bytes_recv = (net_io.bytes_recv - net_io_start.bytes_recv) / (1024 * 1024)  # Convert to MB
    network_sent_data.append(bytes_sent)
    network_recv_data.append(bytes_recv)

    # Timestamps for the x-axis
    timestamps.append(time.time() - start_time)

    # Limit data to 50 points to avoid overloading the graph
    if len(timestamps) > 50:
        cpu_data.pop(0)
        memory_data.pop(0)
        network_sent_data.pop(0)
        network_recv_data.pop(0)
        timestamps.pop(0)

def update_graph(frame):
    """
    Update the graph in real-time.
    """
    monitor_resources()

    # Clear and redraw each subplot
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # CPU usage
    ax1.plot(timestamps, cpu_data, label="CPU Usage (%)", color='red')
    ax1.set_title("CPU Usage")
    ax1.set_ylim(0, 100)
    ax1.set_ylabel("Percentage")
    ax1.legend(loc="upper right")

    # Memory usage
    ax2.plot(timestamps, memory_data, label="Memory Usage (%)", color='blue')
    ax2.set_title("Memory Usage")
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("Percentage")
    ax2.legend(loc="upper right")

    # Network usage
    ax3.plot(timestamps, network_sent_data, label="Network Sent (MB)", color='green')
    ax3.plot(timestamps, network_recv_data, label="Network Received (MB)", color='orange')
    ax3.set_title("Network Bandwidth")
    ax3.set_ylabel("MB")
    ax3.legend(loc="upper right")

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
fig.tight_layout(pad=4)

# Real-time animation
ani = FuncAnimation(fig, update_graph, interval=1000, cache_frame_data=False)  # Update every second

# Start the graph
plt.show()
