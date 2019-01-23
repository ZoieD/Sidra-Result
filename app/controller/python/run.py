import numpy as np
from keras.layers import Dense,Dropout,Activation,Input
from keras.models import Sequential,Model
import sys

n = sys.argv[1]
ll = sys.argv[2]
hh = sys.argv[3]
lh = sys.argv[4]
za = sys.argv[5]
lra = sys.argv[6]
w = sys.argv[7]

#model create
def make_model():
    model=Sequential()
    model.add(Dense(units=100,activation='relu',input_dim=6))
#     model.add(Dropout(0.05))
    model.add(Dense(units=80,activation='relu'))
    model.add(Dense(units=60,activation='relu'))
    model.add(Dense(units=40,activation='relu'))
    model.add(Dense(units=20,activation='relu'))
#     model.add(Dropout(0.05))
    model.add(Dense(units=1,activation=None))
    model.compile(loss='logcosh',optimizer='adam',metrics=['accuracy'])
    return model

if __name__=='__main__':
	model = make_model()
	model.load_weights('C:/Users/Dou-Zi.Dou/Downloads/Calculators/grf_to_excel/app/controller/python/modules/pressure_module.h5',by_name=False)
	# arr = [N, lL, hH, LH, Za, LRa]
	x_test_pressure = np.array([[n, ll, hh, lh, za, lra]])
	pred_pressure = model.predict(x_test_pressure)
	print(pred_pressure)

	model.load_weights('C:/Users/Dou-Zi.Dou/Downloads/Calculators/grf_to_excel/app/controller/python/modules/impulses_module.h5',by_name=False)
	# arr = [N, lL, hH, LH, Za, LRa]
	x_test_impulses = np.array([[n, ll, hh, lh, za, lra]])
	pred_impulses = model.predict(x_test_impulses)
	print(pred_impulses)

	t0 = 2*pred_impulses*pow(float(w), 1/3) / pred_pressure
	print(t0)
