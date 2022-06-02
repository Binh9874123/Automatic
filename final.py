import os 
import cv2
import funtion as fun
command = 'prostak.exe'

path_data = 'C:\\Users\\Binh9874123\\OneDrive\\Desktop\\Automatic\\Xulyhinhanh\\en_1_measurementsrr2\\'

show_flag = 0
output = (path_data+'node29out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(path_data +'node29out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8108out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 19,19,5,disk,square',output)
img = cv2.imread(path_data +'node8108out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8117out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 7,7,3,square,square',output)
img = cv2.imread(path_data +'node8117out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8123out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 31,31,7,square,square',output)
img = cv2.imread(path_data +'node8123out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8130out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 11,11,5,square,square',output)
img = cv2.imread(path_data +'node8130out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8136out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(path_data +'node8136out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8137out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 3,3,3,square,square',output)
img = cv2.imread(path_data +'node8137out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'-mch-z.tif')
output = (path_data+'node8218out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.hystthresh_result(command,'-s 25.0,120.0,10,4',input,output)
img = cv2.imread(path_data +'node8218out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

output = (path_data+'node8220out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 13,13,square',output)
img = cv2.imread(path_data +'node8220out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node8230out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 5,5,square',output)
img = cv2.imread(path_data +'node8230out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'-mDAPI.tif')
output = (path_data+'node8232out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand_result(command,'-p 2.0',input,output)
img = cv2.imread(path_data +'node8232out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8232out1.tif')
output = (path_data+'node8233out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.halfsizes_result(command,'',input,output)
img = cv2.imread(path_data +'node8233out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8233out1.txt')
output = (path_data+'node8234out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.m_ar_plus_result(command,'-s 200,200,200,200',input,output)
img = cv2.imread(path_data +'node8234out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8234out1.txt')
output = (path_data+'node8235out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.ar_x_result(command,'-p 0.4',input,output)
img = cv2.imread(path_data +'node8235out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8235out1.txt')
output = (path_data+'node8236out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.ar_x_result(command,'-p 2.5',input,output)
img = cv2.imread(path_data +'node8236out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8233out1.txt',path_data+'node8236out1.txt')
output = (path_data+'node8237out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.ar_minus_result(command,'',input,output)
img = cv2.imread(path_data +'node8237out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8232out1.tif',path_data+'node8237out1.txt')
output = (path_data+'node8238out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.pad3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8238out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8238out1.tif',path_data+'rotate.txt')
output = (path_data+'node8239out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.turn3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8239out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8239out1.tif',path_data+'-apee-z.txt')
output = (path_data+'node8240out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.apee3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8240out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8218out1.tif',path_data+'node8220out1.txt')
output = (path_data+'node8219out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8219out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8240out1.tif',path_data+'node8219out1.tif')
output = (path_data+'node15out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.heq_result(command,'',input,output)
img = cv2.imread(path_data +'node15out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node15out1.tif')
output = (path_data+'node8107out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.4',input,output)
img = cv2.imread(path_data +'node8107out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8107out1.tif',path_data+'node8108out1.txt')
output = (path_data+'node8109out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8109out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8109out1.tif')
output = (path_data+'node8110out1.tif',path_data+'node8110out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold3d_result(command,'-p 15.0 -s plain -r 1',input,output)
img = cv2.imread(path_data +'node8110out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8110out1.tif')
output = (path_data+'node8111out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand3d_result(command,'-p 2.5',input,output)
img = cv2.imread(path_data +'node8111out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8111out1.tif')
output = (path_data+'node8217out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.distance_result(command,'-r 7',input,output)
img = cv2.imread(path_data +'node8217out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8217out1.tif')
output = (path_data+'node8113out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.4',input,output)
img = cv2.imread(path_data +'node8113out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8113out1.tif',path_data+'node8108out1.txt')
output = (path_data+'node8114out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8114out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8114out1.tif')
output = (path_data+'node8115out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand3d_result(command,'-p 2.5',input,output)
img = cv2.imread(path_data +'node8115out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8115out1.tif',path_data+'node8117out1.txt')
output = (path_data+'node8116out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8116out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8116out1.tif')
output = (path_data+'node8118out1.tif',path_data+'node8118out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold3d_result(command,'-p 3.0 -s plain -r 1',input,output)
img = cv2.imread(path_data +'node8118out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8118out1.tif')
output = (path_data+'node28out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.edge_result(command,'-s 0.589744,0.564103,12,15,5,10,8',input,output)
img = cv2.imread(path_data +'node28out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node28out1.tif',path_data+'node29out1.txt')
output = (path_data+'node30out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.chole_result(command,'',input,output)
img = cv2.imread(path_data +'node30out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node30out1.tif')
output = (path_data+'node8119out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.max3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8119out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8119out1.tif',path_data+'node29out1.txt')
output = (path_data+'node31out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node31out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node31out1.tif')
output = (path_data+'node32out1.tif',path_data+'node32out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.crop_result(command,'',input,output)
img = cv2.imread(path_data +'node32out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8240out1.tif',path_data+'node32out1.tif')
output = (path_data+'node8120out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.geometry3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8120out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node30out1.tif',path_data+'node32out1.tif')
output = (path_data+'node8121out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.geometry3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8121out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8120out1.tif',path_data+'node8121out1.tif')
output = (path_data+'node8122out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8122out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8122out1.tif',path_data+'node8123out1.txt')
output = (path_data+'node8177out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.lheq3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8177out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'-cDAPI.tif',path_data+'node32out1.tif')
output = (path_data+'node8254out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.geometry3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8254out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8177out1.tif')
output = (path_data+'node8128out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.despekle3d_result(command,'-r 5',input,output)
img = cv2.imread(path_data +'node8128out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8128out1.tif',path_data+'node8130out1.txt')
output = (path_data+'node8129out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8129out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8129out1.tif',path_data+'node8230out1.txt')
output = (path_data+'node8229out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8229out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8129out1.tif',path_data+'node8229out1.tif')
output = (path_data+'node8228out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread(path_data +'node8228out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8228out1.tif')
output = (path_data+'node8131out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8131out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8131out1.tif')
output = (path_data+'node8132out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.cwtsd3d_result(command,'-r 6',input,output)
img = cv2.imread(path_data +'node8132out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8121out1.tif',path_data+'node8132out1.tif')
output = (path_data+'node8158out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8158out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8158out1.tif',path_data+'node8137out1.txt')
output = (path_data+'node8144out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8144out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8254out1.tif',path_data+'node8144out1.tif')
output = (path_data+'node8244out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.setp_result(command,'-r -1',input,output)
img = cv2.imread(path_data +'node8244out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8144out1.tif',path_data+'node8144out1.tif')
output = (path_data+'node8080out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3dinit_result(command,'-r 26 -s cellmask',input,output)
img = cv2.imread(path_data +'node8080out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8129out1.tif',path_data+'node8144out1.tif')
output = (path_data+'node8134out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8134out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8134out1.tif')
output = (path_data+'node8133out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.edge_result(command,'-s 0.735043,0.735043,12,15,11,10,8',input,output)
img = cv2.imread(path_data +'node8133out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8133out1.tif',path_data+'node8136out1.txt')
output = (path_data+'node8135out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.chole_result(command,'',input,output)
img = cv2.imread(path_data +'node8135out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8135out1.tif',path_data+'node8158out1.tif')
output = (path_data+'node8181out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8181out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8181out1.tif',path_data+'node8137out1.txt')
output = (path_data+'node8176out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gopen3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node8176out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8122out1.tif',path_data+'node8176out1.tif')
output = (path_data+'node8215out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8215out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8176out1.tif')
output = (path_data+'node8147out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8147out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node8147out1.tif',path_data+'node8144out1.tif')
output = (path_data+'node8146out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node8146out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
