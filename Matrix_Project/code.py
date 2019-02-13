import numpy as np
import matplotlib.pyplot as plt


########## Defining Variables #################
len = int(1e3)
theta = np.linspace(0,2*np.pi,len)
C1 = np.array([[0.],[0.]])
r1 = 2
C2 = np.array([[3.],[0.]])
r2 = 1
P2_1 = np.array([[2.5],[1.732/2]])
P2_2 = np.array([[3.5],[-np.sqrt(3)/2]])
dir_vec = np.array([[np.sqrt(3)/2],[0.5]])
cosp1 = np.cos(2*np.pi/3)
sinp1 = np.sin(2*np.pi/3)
cos = np.cos(np.pi/6)
sin = np.sin(np.pi/6)


############## plotting Circle 1 ################
Cr1 = np.array([0,0])
x_C1 = np.zeros((2,len))
for i in range(len):
	temp1 = Cr1 + 2*np.array([np.cos(theta[i]),np.sin(theta[i])])
	x_C1[:,i] = temp1.T
plt.plot(x_C1[0,:],x_C1[1,:],label='Circle 1')


############# plotting Circle 2 ##################
Cr2 = np.array([3,0])
x_C2 = np.zeros((2,len))
for i in range(len):
	temp1 = Cr2 + np.array([np.cos(theta[i]),np.sin(theta[i])])
	x_C2[:,i] = temp1.T
plt.plot(x_C2[0,:],x_C2[1,:],label='Circle 2')


############## plotting Tangent to Circle 1 ################
P1 = np.array([1.732,1])
len = 10
dir_vec = np.array([cosp1,sinp1])
lam_1 = np.linspace(-3,3,len)
x_P1 = np.zeros((2,len))
for i in range(len):
	temp1 = P1 + lam_1[i]*dir_vec
	x_P1[:,i] = temp1.T
plt.plot(x_P1[0,:],x_P1[1,:],label='Tangent at $P1$')


################ plotting Tangent to Circle 2 at P2_1 ####################
P2_1 = np.array([2.5,1.732/2])
len = 10
dir_vec = np.array([cos,sin])
lam_1 = np.linspace(-3,3,len)
x_AB = np.zeros((2,len))
for i in range(len):
	temp1 = P2_1 + lam_1[i]*dir_vec
	x_AB[:,i] = temp1.T
plt.xlim(-3,7)
plt.ylim(-5,5)
plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent at $P2_1$')


################# plotting Tangent to Circle 2 at P2_2 ###################
P2_2 = np.array([3.5,-1.732/2])
len = 10
dir_vec = np.array([cos,sin])
lam_1 = np.linspace(-3,3,len)
x_CD = np.zeros((2,len))
for i in range(len):
	temp1 = P2_2 + lam_1[i]*dir_vec
	x_CD[:,i] = temp1.T
plt.plot(x_CD[0,:],x_CD[1,:],label='Tangent at $P2_2$')



############# Marking the points on the graph #####################
types = ['P1', 'P2_1', 'P2_2', 'C1(0,0)','C2(3,0)' ]
x_coords = [1.732, 2.5, 3.5,0,3]
y_coords = [1, 0.866, -0.866,0,0]
for i,type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='o', color='red')
    plt.text(x-0.25, y+0.4, type, fontsize=12)

############### labelling the axes  #####################
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upperright')
plt.grid()
fig = plt.gcf()
fig.set_size_inches(18.5, 18.5)
fig.savefig('img.jpg', dpi=100)
plt.show()
