import h5py
import numpy as np
import pandas as pd
if __name__ == '__main__':
    files = ['rosbag2_2023_06_14-10_58_21.h5']
    
    for file in files:
        f = h5py.File(file, 'r')
        print(list(f.keys()))
        data={}
        timestamp = np.array(f['rm_wheelchair__range_0:stamp']).flatten()
        range_0 = np.array(f['rm_wheelchair__range_0:data']).flatten()
        range_1 = np.array(f['rm_wheelchair__range_1:data']).flatten()
        range_2 = np.array(f['rm_wheelchair__range_2:data']).flatten()
        range_3 = np.array(f['rm_wheelchair__range_3:data']).flatten()
        stamp_w = np.array(f['rm_wheelchair__camera__image_h264:stamp']).flatten()
        #data['timestamp'] = timestamp
        #data['range_0'] = range_0
        #data['range_1'] = range_1
        #data['range_2'] = range_2
        #data['range_3'] = range_3
        data['stamp_w'] = stamp_w
        #print(len(data['range_0']), len(data['range_1']), len(data['range_2']), len(data['range_3']))

        df = pd.DataFrame.from_dict(data)
        df.to_csv('test.csv', index=False)



#'rosbag2_2023_06_14-10_57_03.h5',
#'rosbag2_2023_06_14-10_58_21.h5',
#'rosbag2_2023_06_14-11_02_22.h5',
#'rosbag2_2023_06_14-11_03_52.h5',
#'rosbag2_2023_06_14-11_06_36.h5',
#'rosbag2_2023_06_14-11_07_13.h5',

#'rosbag2_2023_06_14-10_57_03.h5',0
            # 'rosbag2_2023_06_14-10_58_21.h5',1
            # 'rosbag2_2023_06_14-11_02_22.h5',2
            # 'rosbag2_2023_06_14-11_03_52.h5',3
            # 'rosbag2_2023_06_14-11_06_36.h5',4
            # 'rosbag2_2023_06_14-11_07_13.h5',5

            # 'rosbag2_2023_06_14-14_14_31.h5',6
            # 'rosbag2_2023_06_14-14_21_57.h5',7
            # 'rosbag2_2023_06_14-14_26_34.h5',8
            # 'rosbag2_2023_06_14-14_30_17.h5',9
            # 'rosbag2_2023_06_14-14_38_31.h5',10
            # 'rosbag2_2023_06_14-14_44_51.h5',11
            # 'rosbag2_2023_06_14-14_47_56.h5',12
            # 'rosbag2_2023_06_14-14_52_30.h5',13
            # 'rosbag2_2023_06_14-14_55_39.h5'14