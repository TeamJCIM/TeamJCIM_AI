import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('data.csv', encoding = 'cp949')

input_num = pd.DataFrame(data, columns = ['평균기온(℃)', '평균풍속(m/s)', '평균습도(%rh)', '평균일강수량(mm)', '일사합', 
                                               '평균전력사용량', '코스피', '미세먼지', '최저기온(℃)','최고기온(℃)', 
                                               '평균 현지기압(hPa)','평균지면온도(℃)', '합계 소형증발량(mm)'])
input_day = pd.DataFrame(data, columns = ['요일'])
input_holi = pd.DataFrame(data, columns = ['공휴일/국경일'])
input_wek = pd.DataFrame(data, columns = ['평일/주말'])
y = pd.DataFrame(data, columns = ['전력'])

# StandardScaler 객체 생성
scaler = StandardScaler()

# 데이터 세트 변환
scaler.fit(input_num)
input_num = scaler.transform(input_num)

# ndarray -> dataframe
input_num = pd.DataFrame(input_num, columns = ['평균기온(℃)', '평균풍속(m/s)', '평균습도(%rh)', '평균일강수량(mm)', '일사합', 
                                               '평균전력사용량', '코스피', '미세먼지', '최저기온(℃)','최고기온(℃)', 
                                               '평균 현지기압(hPa)','평균지면온도(℃)', '합계 소형증발량(mm)'])

# 요일 변환
encoder= LabelEncoder()
encoder.fit(input_day)
input_day= encoder.transform(input_day)
input_day = pd.DataFrame(input_day, columns = ['요일'])

input_num['일시'] = data['일시']
input_day['일시'] = data['일시']
input_holi['일시'] = data['일시']
input_wek['일시'] = data['일시']
input_num = input_num.set_index('일시')
input_day = input_day.set_index('일시')
input_holi = input_holi.set_index('일시')
input_wek = input_wek.set_index('일시')
y['일시'] = data['일시']
y = y.set_index('일시')
y = np.ravel(y, order='C')

x = input_num.join(input_day)
x = x.join(input_holi)
x = x.join(input_wek)

saved_model = joblib.load('./model.pkl')

pre = saved_model.predict(x)
print(pre)

# print('heool')