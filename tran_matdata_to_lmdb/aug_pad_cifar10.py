import lmdb
import cv2
import sys 
caffe_root = "/data/hjy1312/C3D-master/C3D-v1.1/"
sys.path.insert(0, caffe_root + 'python')
import caffe
from caffe.proto import caffe_pb2

env1=lmdb.open('/data/hjy1312/data/RESNET/cifar-10/cifar10_train_lmdb_aug')
txn1=env1.begin()
cursor=txn1.cursor()
datum=caffe_pb2.Datum()

env2=lmdb.open('/data/hjy1312/data/RESNET/cifar-10/cifar10_pad4_train_lmdb_aug',map_size=int(1e12))
txn2=env2.begin(write=True)

count=0
for key,value in cursor:
    datum.ParseFromString(value)
    label=datum.label

    data=caffe.io.datum_to_array(datum)
    img=data.transpose(1,2,0)
    pad=cv2.copyMakeBorder(img,4,4,4,4,cv2.BORDER_REFLECT)

    array=pad.transpose(2,0,1)
    datum1=caffe.io.array_to_datum(array,label)

    str_id='{:08}'.format(count)
    txn2.put(str_id,datum1.SerializeToString())

    count+=1
    if count%1000 ==0:
        print('already handled with {} pictures'.format(count))
        txn2.commit()
        txn2=env2.begin(write=True)

txn2.commit()
env2.close()
env1.close()

