from simple_pid import PID
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

## global variables
KP = 2.4
KI = 0.1
KD = 0.001
missile_locx, missile_locy = 0.2, 0.2


pidx = PID(Kp=KP, Ki=KI, Kd=KD, setpoint=missile_locx,sample_time=None)
pidy = PID(Kp=KP, Ki=KI, Kd=KD, setpoint=missile_locy,sample_time=None)


def PID_locupdate(currentx, currenty, mousex, mousey):
	pidx.setpoint = mousex
	pidy.setpoint = mousey
	updated_valx = pidx(currentx)
	updated_valy = pidy(currenty)

	return updated_valx, updated_valy


fig, ax = plt.subplots()
circ = Circle((0.5,0.5), 0.04)
circ2 = Circle((missile_locx,missile_locy),0.008)
circ2.set_facecolor('red')
ax.add_patch(circ2)
ax.add_patch(circ)

def update_mouse(event):
	ax.cla()
	circ = Circle((event.xdata, event.ydata), 0.04)
	ax.add_patch(circ)

	new_missile_x, new_missile_y  = PID_locupdate(missile_locx,missile_locy,event.xdata,event.ydata)
	circ2 = Circle((new_missile_x,new_missile_y),0.008)
	circ2.set_facecolor('red')
	ax.add_patch(circ2)
	fig.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event',update_mouse)
plt.show()

plt.show()
