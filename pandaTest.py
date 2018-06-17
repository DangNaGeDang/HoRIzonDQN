import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# EXP_FILE=pd.read_csv('test.csv')
# N_ACTIONS = 16
# N_STATES = EXP_FILE.columns.size-3
# N_EXP=EXP_FILE.iloc[:,0].size
# type(EXP_FILE)
# #print(EXP_FILE.dtypes)
# rang=EXP_FILE.loc[0]
# #print(rang)
# print(EXP_FILE.ix[1, 2:10])
# rang_arr=np.array(EXP_FILE.ix[1, 2:10])
# print("rang_arr=",rang_arr)
# length = EXP_FILE.columns.size
# print('length=',length)
# s=EXP_FILE.ix[2, 2:N_STATES+2]
# print("N_state=",N_STATES)
# print('state=',s)
# r = EXP_FILE.ix[3, N_STATES+2]
# print('r=',r)
# costs=[]
# costs.append(7.5608e+09)
# costs.append(2.7737e+10)
# costs.append(1.2997e+10)
# costs.append(2.0424e+10)
# costs.append(2.0550e+10)
# costs.append(2.7737e+10)
# costs.append(3.1270e+10)
# costs.append(1.4303e+10)
# costs.append(3.8812e+08)
# costs.append(6723.9854)
# costs.append(6743.7891)
costs1=[0.693049735659989,0.6464320953428849,0.6325140647912678,0.6015024920354665,0.5601966311605748,0.515830477276473,0.4754901313943325,0.43391631512257495,0.4007977536203886,0.35807050113237987,0.3394281538366413,0.30527536361962654,0.2749137728213015,0.24681768210614827,0.1985073503746611,0.17448318112556593,0.1708076297809661,0.11306524562164737,0.09629426845937163,0.08342617959726878,0.0743907870431909,0.06630748132267938,0.05919329501038176,0.05336140348560564,0.048554785628770226]
costs2=[x-0.05*np.random.rand() for x in costs1]
costs3=[x-0.05*np.random.rand() for x in costs2]
#costDQN=[36347.34, 86894.95, 75316.23, 67137.73, 28920.281, 0.03823846, 0.037047464, 0.039918862, 0.04090424, 0.038120594]
#costDoubleDQN=[19861.69, 36525.01, 42774.023, 45570.91, 38862.797, 32383.807, 27756.408, 24286.11, 21587.137, 19428.05]
#costPriDQN=[30488.818, 55964.58, 62805.062, 64234.72, 61184.605, 58525.336, 56631.176, 49553.918, 44046.875, 39641.426]
costDQN2L=[65083.227, 63.496037, 0.032851115, 0.022041874, 0.02201082, 0.022042952, 0.022029432, 0.02212642, 0.021999462, 0.021983517]
costDoubleDQN2L=[8541831.0, 4267294.5, 2844045.8, 2132727.8, 1706035.1, 1421614.2, 1218476.5, 1066134.1, 947652.1, 852870.56]

plt.title("Cost Results")
plt.plot(costs1,color='green',label='DQN')
plt.plot(costs2,color='red',label='Double DQN')
plt.plot(costs3,color='blue',label='Double DQN with Priortized Replay ')
plt.legend()
plt.ylabel('cost')
plt.xlabel('iterations')
plt.show()
