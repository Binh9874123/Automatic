import os 
import cv2
import funtion as fun
command = 'prostak.exe'

path_data = 'C:\\Users\\Binh9874123\\OneDrive\\Desktop\\Automatic\\Xulyhinhanh\\M_1C_4_dots_SXL\\'

show_flag = 0
output = (path_data+'node8out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 23,23,square',output)
img = cv2.imread(path_data +'node8out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node10out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 13,13,3,square,square',output)
img = cv2.imread(path_data +'node10out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node13out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 5,5,3,square,square',output)
img = cv2.imread(path_data +'node13out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node199out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(path_data +'node199out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node217out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(path_data +'node217out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'node217out1.txt')
output = (path_data+'node229out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vstrel_result(command,'',input,output)
img = cv2.imread(path_data +'node229out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'-cSXL.tif',path_data+'rotate.txt')
output = (path_data+'node306out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.turn3d_result(command,'',input,output)
img = cv2.imread(path_data +'node306out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node306out1.tif',path_data+'-apee-z.txt')
output = (path_data+'node307out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.apee3d_result(command,'',input,output)
img = cv2.imread(path_data +'node307out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node307out1.tif',path_data+'crop-sm.txt')
output = (path_data+'node310out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.geometry3d_result(command,'',input,output)
img = cv2.imread(path_data +'node310out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node310out1.tif',path_data+'node8out1.txt')
output = (path_data+'node7out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.lhbg_result(command,'',input,output)
img = cv2.imread(path_data +'node7out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node7out1.tif',path_data+'node10out1.txt')
output = (path_data+'node9out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node9out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node9out1.tif',path_data+'node310out1.tif')
output = (path_data+'node11out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vaff_result(command,'-s -1.0,1.0,0.0',input,output)
img = cv2.imread(path_data +'node11out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node11out1.tif')
output = (path_data+'node302out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand3d_result(command,'-p 2.0',input,output)
img = cv2.imread(path_data +'node302out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node302out1.tif')
output = (path_data+'node202out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.hno_result(command,'',input,output)
img = cv2.imread(path_data +'node202out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node202out1.tif')
output = (path_data+'node12out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(path_data +'node12out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node12out1.tif',path_data+'node13out1.txt')
output = (path_data+'node14out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node14out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node202out1.tif',path_data+'node13out1.txt')
output = (path_data+'node15out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion3d_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node15out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node202out1.tif',path_data+'node15out1.tif')
output = (path_data+'node16out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct3d_result(command,'-r 26',input,output)
img = cv2.imread(path_data +'node16out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node12out1.tif',path_data+'node14out1.tif')
output = (path_data+'node17out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct3d_result(command,'-r 26',input,output)
img = cv2.imread(path_data +'node17out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node17out1.tif')
output = (path_data+'node18out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(path_data +'node18out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node16out1.tif',path_data+'node18out1.tif')
output = (path_data+'node19out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node19out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node16out1.tif',path_data+'node18out1.tif')
output = (path_data+'node20out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vaff_result(command,'-s -1.0,1.0,0.0',input,output)
img = cv2.imread(path_data +'node20out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node20out1.tif',path_data+'node19out1.tif')
output = (path_data+'node21out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vmax_result(command,'',input,output)
img = cv2.imread(path_data +'node21out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node21out1.tif')
output = (path_data+'node22out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.despekle3d_result(command,'-r 3',input,output)
img = cv2.imread(path_data +'node22out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node22out1.tif',path_data+'node199out1.txt')
output = (path_data+'node198out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.lhbg_result(command,'',input,output)
img = cv2.imread(path_data +'node198out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node198out1.tif')
output = (path_data+'node209out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.imcanny_result(command,'0x1+0.03+0.1 -depth 8',input,output)
img = cv2.imread(path_data +'node209out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node209out1.tif',path_data+'node217out1.txt')
output = (path_data+'node216out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.chole_result(command,'',input,output)
img = cv2.imread(path_data +'node216out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node22out1.tif')
output = (path_data+'node304out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.5',input,output)
img = cv2.imread(path_data +'node304out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node216out1.tif',path_data+'node217out1.txt')
output = (path_data+'node305out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gopen_result(command,'-r 1',input,output)
img = cv2.imread(path_data +'node305out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node305out1.tif')
output = (path_data+'node218out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.distance_result(command,'-r 7',input,output)
img = cv2.imread(path_data +'node218out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node218out1.tif')
output = (path_data+'node219out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(path_data +'node219out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node219out1.tif')
output = (path_data+'node220out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.cwtsd_result(command,'-r 8',input,output)
img = cv2.imread(path_data +'node220out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node220out1.tif',path_data+'node305out1.tif')
output = (path_data+'node221out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(path_data +'node221out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node221out1.tif',path_data+'node229out1.tif')
output = (path_data+'node228out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.sselect_result(command,'-p 0.1 -s 100,5,accept -r 8',input,output)
img = cv2.imread(path_data +'node228out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node228out1.tif')
output = (path_data+'node303out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.5',input,output)
img = cv2.imread(path_data +'node303out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node304out1.tif',path_data+'node303out1.tif')
output = (path_data+'node314out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3dinit_result(command,'-r 26 -s SXLmol',input,output)
img = cv2.imread(path_data +'node314out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node303out1.tif',path_data+'-cellmask.tif',path_data+'node314out1.txt')
output = (path_data+'node315out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.quremask_result(command,'-r 26 -s celnumber',input,output)
img = cv2.imread(path_data +'node315out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node315out1.txt')
output = (path_data+'node316out1.csv')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d2csv_result(command,'',input,output)
img = cv2.imread(path_data +'node316out1.csv')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node303out1.tif',path_data+'-cellmask.tif')
output = (path_data+'node273out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3dinit_result(command,'-r 26 -s nSXL',input,output)
img = cv2.imread(path_data +'node273out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node304out1.tif',path_data+'-cellmask.tif',path_data+'node273out1.txt')
output = (path_data+'node313out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d_result(command,'-r 26 -s cSXL',input,output)
img = cv2.imread(path_data +'node313out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node313out1.txt')
output = (path_data+'node264out1.csv')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d2csv_result(command,'',input,output)
img = cv2.imread(path_data +'node264out1.csv')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
