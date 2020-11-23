import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x)+1

	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	# calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 

	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points as scatter plot 
	plt.plot(x, y, color = "m") 

	# predicted response vector 
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 
a=df2.index
a=np.append(a,[np.size(a)+1])
print("This is DF1")
b = estimate_coef(a, y11)
plot_regression_line(a, y11, b)
print("This is DF2")
b = estimate_coef(a, y21)
plot_regression_line(a, y21, b)
print("This is DF3")
b = estimate_coef(a, y31)
plot_regression_line(a, y31, b)
print("This is DF4")
b = estimate_coef(a, y41)
plot_regression_line(a, y41, b)
