import matplotlib.pyplot as plt
import matplotlib.animation as animation

# the maximum current per motor without a central power manager is limited to
# maxCurrent / numMotors
numMotors = 16
maxCurrent = 20
perMotorCap = maxCurrent / numMotors

def gen():
    time = -1
    while time <= 18:
        time += 1
        yield time

def update(time):
    # the current limit for each motor is reduced equally
    xdata.append(time)
    ydata[0].append(perMotorCap)
    ydata[1].append(perMotorCap)
    ydata[2].append(perMotorCap)
    ydata[3].append(perMotorCap)

    # update the line objects
    lines[0].set_data(xdata, ydata[0])
    lines[1].set_data(xdata, ydata[1])
    lines[2].set_data(xdata, ydata[2])
    lines[3].set_data(xdata, ydata[3])
    return lines

# create a figure with 4 subplots (one for each subsystem)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# initialize line objects (one for each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
line3, = ax3.plot([], [], lw=2)
line4, = ax4.plot([], [], lw=2)
lines = [line1, line2, line3, line4]

# initialize axes
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_ylim(0, 2.5)
    ax.set_xlim(0, 18)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Current")
    ax.grid()

ax1.set_title("Chassis", pad=10)
ax2.set_title("Tilter", pad=10)
ax3.set_title("Lift", pad=10)
ax4.set_title("Intake", pad=10)

# initialize data containers
xdata, ydata = [], [[], [], [], []]
time = 0

def init():
    global xdata, ydata
    xdata, ydata = [], [[], [], [], []]

# save gif
a = animation.FuncAnimation(fig, update, frames=gen, interval=250,
    repeat=True, init_func=init)
f = r"withoutPowerManager.gif"
writergif = animation.PillowWriter(fps=10)
a.save(f, writer=writergif)
