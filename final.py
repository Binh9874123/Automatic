import os 
import cv2
import funtion as fun
command = 'prostak.exe'

pathdata = 'C:\\Users\\Binh9874123\\OneDrive\\Desktop\\Automatic\\Xulyhinhanh\\M_1C_4_dots_DI\\'

show_flag = 0
output = (pathdata+'node8out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 23,23,square',output)
img = cv2.imread(pathdata +'node8out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (pathdata+'node10out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 13,13,3,square,square',output)
img = cv2.imread(pathdata +'node10out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (pathdata+'node13out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel3d_result(command,'-s 5,5,3,square,square',output)
img = cv2.imread(pathdata +'node13out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (pathdata+'node199out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(pathdata +'node199out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (pathdata+'node217out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread(pathdata +'node217out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (pathdata+'node217out1.txt')
output = (pathdata+'node229out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vstrel_result(command,'',input,output)
img = cv2.imread(pathdata +'node229out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'-cDI.tif',pathdata+'rotate.txt')
output = (pathdata+'node306out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.turn3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node306out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node306out1.tif',pathdata+'-apee-z.txt')
output = (pathdata+'node307out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.apee3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node307out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node307out1.tif',pathdata+'crop-sm.txt')
output = (pathdata+'node310out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.geometry3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node310out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node310out1.tif',pathdata+'node8out1.txt')
output = (pathdata+'node7out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.lhbg_result(command,'',input,output)
img = cv2.imread(pathdata +'node7out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node7out1.tif',pathdata+'node10out1.txt')
output = (pathdata+'node9out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median3d_result(command,'-r 1',input,output)
img = cv2.imread(pathdata +'node9out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node9out1.tif',pathdata+'node310out1.tif')
output = (pathdata+'node11out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vaff_result(command,'-s -1.0,1.0,0.0',input,output)
img = cv2.imread(pathdata +'node11out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node11out1.tif')
output = (pathdata+'node302out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand3d_result(command,'-p 2.0',input,output)
img = cv2.imread(pathdata +'node302out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node302out1.tif')
output = (pathdata+'node202out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.hno_result(command,'',input,output)
img = cv2.imread(pathdata +'node202out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node202out1.tif')
output = (pathdata+'node12out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node12out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node12out1.tif',pathdata+'node13out1.txt')
output = (pathdata+'node14out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion3d_result(command,'-r 1',input,output)
img = cv2.imread(pathdata +'node14out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node202out1.tif',pathdata+'node13out1.txt')
output = (pathdata+'node15out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion3d_result(command,'-r 1',input,output)
img = cv2.imread(pathdata +'node15out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node202out1.tif',pathdata+'node15out1.tif')
output = (pathdata+'node16out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct3d_result(command,'-r 26',input,output)
img = cv2.imread(pathdata +'node16out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node12out1.tif',pathdata+'node14out1.tif')
output = (pathdata+'node17out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct3d_result(command,'-r 26',input,output)
img = cv2.imread(pathdata +'node17out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node17out1.tif')
output = (pathdata+'node18out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node18out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node16out1.tif',pathdata+'node18out1.tif')
output = (pathdata+'node19out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node19out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node16out1.tif',pathdata+'node18out1.tif')
output = (pathdata+'node20out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vaff_result(command,'-s -1.0,1.0,0.0',input,output)
img = cv2.imread(pathdata +'node20out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node20out1.tif',pathdata+'node19out1.tif')
output = (pathdata+'node21out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.vmax_result(command,'',input,output)
img = cv2.imread(pathdata +'node21out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node21out1.tif')
output = (pathdata+'node22out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.despekle3d_result(command,'-r 3',input,output)
img = cv2.imread(pathdata +'node22out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node22out1.tif',pathdata+'node199out1.txt')
output = (pathdata+'node198out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.lhbg_result(command,'',input,output)
img = cv2.imread(pathdata +'node198out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node198out1.tif')
output = (pathdata+'node209out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.imcanny_result(command,'0x1+0.03+0.1 -depth 8',input,output)
img = cv2.imread(pathdata +'node209out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node209out1.tif',pathdata+'node217out1.txt')
output = (pathdata+'node216out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.chole_result(command,'',input,output)
img = cv2.imread(pathdata +'node216out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node22out1.tif')
output = (pathdata+'node304out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.5',input,output)
img = cv2.imread(pathdata +'node304out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node216out1.tif',pathdata+'node217out1.txt')
output = (pathdata+'node305out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gopen_result(command,'-r 1',input,output)
img = cv2.imread(pathdata +'node305out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node305out1.tif')
output = (pathdata+'node218out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.distance_result(command,'-r 7',input,output)
img = cv2.imread(pathdata +'node218out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node218out1.tif')
output = (pathdata+'node219out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node219out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node219out1.tif')
output = (pathdata+'node220out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.cwtsd_result(command,'-r 8',input,output)
img = cv2.imread(pathdata +'node220out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node220out1.tif',pathdata+'node305out1.tif')
output = (pathdata+'node221out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul3d_result(command,'',input,output)
img = cv2.imread(pathdata +'node221out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node221out1.tif',pathdata+'node229out1.tif')
output = (pathdata+'node228out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.sselect_result(command,'-p 0.1 -s 100,5,accept -r 8',input,output)
img = cv2.imread(pathdata +'node228out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node228out1.tif')
output = (pathdata+'node303out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink3d_result(command,'-p 0.5',input,output)
img = cv2.imread(pathdata +'node303out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node304out1.tif',pathdata+'node303out1.tif')
output = (pathdata+'node314out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3dinit_result(command,'-r 26 -s DImol',input,output)
img = cv2.imread(pathdata +'node314out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node303out1.tif',pathdata+'-cellmask.tif',pathdata+'node314out1.txt')
output = (pathdata+'node315out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.quremask_result(command,'-r 26 -s celnumber',input,output)
img = cv2.imread(pathdata +'node315out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node315out1.txt')
output = (pathdata+'node316out1.csv')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d2csv_result(command,'',input,output)
img = cv2.imread(pathdata +'node316out1.csv')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node303out1.tif',pathdata+'-cellmask.tif')
output = (pathdata+'node273out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3dinit_result(command,'-r 26 -s nDI',input,output)
img = cv2.imread(pathdata +'node273out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node304out1.tif',pathdata+'-cellmask.tif',pathdata+'node273out1.txt')
output = (pathdata+'node313out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d_result(command,'-r 26 -s cDI',input,output)
img = cv2.imread(pathdata +'node313out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (pathdata+'node313out1.txt')
output = (pathdata+'node264out1.csv')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.qu3d2csv_result(command,'',input,output)
img = cv2.imread(pathdata +'node264out1.csv')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
