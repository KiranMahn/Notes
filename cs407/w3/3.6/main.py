from verispy import VERIS
data_dir="C:\\Users\\kiranmahn\\GitHub\\VCDB\\data\\json\\validated" #replace with your own address for data 

v = VERIS(json_dir=data_dir)

print (v.schema_url)