import numpy as np
import pandas as pd
from keras.layers import Dense,Dropout,Activation,Input
from keras.models import Sequential,Model
from keras import metrics
import matplotlib.pyplot as plt
import os

#model create
def make_model():
    model=Sequential()
    model.add(Dense(units=100,activation='relu',input_dim=6))
#     model.add(Dropout(0.05))
    model.add(Dense(units=80,activation='relu'))
    model.add(Dense(units=40,activation='relu'))
#     model.add(Dropout(0.05))
    model.add(Dense(units=1,activation=None))
    model.compile(loss='mse',optimizer='adam',metrics=[metrics.mae])
    print(model.summary())
    return model

if __name__=='__main__':
	model = make_model()
	df_train_pressure=pd.read_csv('./data_processer/pressure_data.csv')
	df_train_impulses=pd.read_csv('./data_processer/impulses_data.csv')
	x_train_pressure = df_train_pressure.drop('y',axis=1)
	y_train_pressure = df_train_pressure['y']
	x_train_impulses = df_train_impulses.drop('y',axis=1)
	y_train_impulses = df_train_impulses['y']

	model.fit(x_train_pressure, y_train_pressure, batch_size=40, epochs=100, verbose=1)
	model.save_weights('modules/pressure_module.h5')
	model.fit(x_train_impulses, y_train_impulses, batch_size=40, epochs=100, verbose=1)
	model.save_weights('modules/impulses_module.h5')		