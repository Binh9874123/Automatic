import os 
import cv2
import funtion as fun
command = 'prostak.exe'

path_data = 'C:\\Users\\Binh9874123\\OneDrive\\Desktop\\Automatic\\'

show_flag = 0
output = (path_data+'node4out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 9,9,square',output)
img = cv2.imread('node4out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'d218.tif')
output = (path_data+'node21out1.tif',path_data+'node21out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold_result(command,'-p 10.0 -s otsu -r 1',input,output)
img = cv2.imread('node21out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

output = (path_data+'node31out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread('node31out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'d218.tif')
output = (path_data+'node35out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand_result(command,'-p 2.0',input,output)
img = cv2.imread('node35out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

output = (path_data+'node48out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread('node48out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node59out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 23,23,disk',output)
img = cv2.imread('node59out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node73out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 3,3,square',output)
img = cv2.imread('node73out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'f218.tif')
output = (path_data+'node82out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand_result(command,'-p 2.0',input,output)
img = cv2.imread('node82out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'r218.tif')
output = (path_data+'node83out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand_result(command,'-p 2.0',input,output)
img = cv2.imread('node83out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

output = (path_data+'node95out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 9,9,disk',output)
img = cv2.imread('node95out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

output = (path_data+'node112out1.txt')
if type(output) != type('abc'):
	output = ','.join(output)
fun.strel_result(command,'-s 5,5,square',output)
img = cv2.imread('node112out1.txt')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)

input = (path_data+'node82out1.tif')
output = (path_data+'node127out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink_result(command,'-p 0.5',input,output)
img = cv2.imread('node127out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node21out1.tif',path_data+'d218.tif')
output = (path_data+'node19out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul_result(command,'',input,output)
img = cv2.imread('node19out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node19out1.tif',path_data+'node21out1.tif')
output = (path_data+'node27out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.heq_result(command,'',input,output)
img = cv2.imread('node27out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node82out1.tif')
output = (path_data+'node41out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node41out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node41out1.tif')
output = (path_data+'node80out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.heq_result(command,'',input,output)
img = cv2.imread('node80out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node83out1.tif')
output = (path_data+'node81out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.heq_result(command,'',input,output)
img = cv2.imread('node81out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node80out1.tif')
output = (path_data+'node84out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.despekle_result(command,'-r 4',input,output)
img = cv2.imread('node84out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node81out1.tif')
output = (path_data+'node85out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.despekle_result(command,'-r 4',input,output)
img = cv2.imread('node85out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node27out1.tif')
output = (path_data+'node7out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.andif_result(command,'-s 10,0.5,0.9,frac',input,output)
img = cv2.imread('node7out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node7out1.tif')
output = (path_data+'node23out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.expand_result(command,'-p 2.0',input,output)
img = cv2.imread('node23out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node84out1.tif',path_data+'node48out1.txt')
output = (path_data+'node47out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node47out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node85out1.tif',path_data+'node48out1.txt')
output = (path_data+'node49out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node49out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node47out1.tif',path_data+'node49out1.tif')
output = (path_data+'node50out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.avg_result(command,'',input,output)
img = cv2.imread('node50out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node50out1.tif')
output = (path_data+'node87out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.andif_result(command,'-s 20,0.3,0.7,frac',input,output)
img = cv2.imread('node87out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node23out1.tif',path_data+'node4out1.txt')
output = (path_data+'node3out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node3out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node23out1.tif',path_data+'node3out1.tif')
output = (path_data+'node5out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread('node5out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node5out1.tif')
output = (path_data+'node6out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node6out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node6out1.tif',path_data+'node4out1.txt')
output = (path_data+'node8out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node8out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node6out1.tif',path_data+'node8out1.tif')
output = (path_data+'node9out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread('node9out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node9out1.tif')
output = (path_data+'node18out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.cwtsd_result(command,'-r 4',input,output)
img = cv2.imread('node18out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node18out1.tif',path_data+'node23out1.tif')
output = (path_data+'node26out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul_result(command,'',input,output)
img = cv2.imread('node26out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node87out1.tif',path_data+'node59out1.txt')
output = (path_data+'node52out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node52out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node87out1.tif',path_data+'node52out1.tif')
output = (path_data+'node57out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread('node57out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node26out1.tif')
output = (path_data+'node22out1.tif',path_data+'node22out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold_result(command,'-p 3.0 -s plain -r 1',input,output)
img = cv2.imread('node22out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node22out1.tif',path_data+'node31out1.txt')
output = (path_data+'node30out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node30out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node30out1.tif',path_data+'node31out1.txt')
output = (path_data+'node32out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.median_result(command,'-r 1',input,output)
img = cv2.imread('node32out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node32out1.tif')
output = (path_data+'node33out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gmag_result(command,'',input,output)
img = cv2.imread('node33out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node33out1.tif')
output = (path_data+'node34out1.tif',path_data+'node34out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold_result(command,'-p 1.0 -s plain -r 1',input,output)
img = cv2.imread('node34out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node34out1.tif',path_data+'node35out1.tif')
output = (path_data+'node36out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.movl_result(command,'-s magenta,yellow',input,output)
img = cv2.imread('node36out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node57out1.tif')
output = (path_data+'node54out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node54out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node32out1.tif',path_data+'node112out1.txt')
output = (path_data+'node111out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node111out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node32out1.tif')
output = (path_data+'node120out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node120out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node54out1.tif',path_data+'node59out1.txt')
output = (path_data+'node53out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node53out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node54out1.tif',path_data+'node53out1.tif')
output = (path_data+'node58out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread('node58out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node111out1.tif')
output = (path_data+'node107out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gmag_result(command,'',input,output)
img = cv2.imread('node107out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node58out1.tif',path_data+'node95out1.txt')
output = (path_data+'node113out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gclose_result(command,'-r 7',input,output)
img = cv2.imread('node113out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node113out1.tif')
output = (path_data+'node117out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gmag_result(command,'',input,output)
img = cv2.imread('node117out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node117out1.tif')
output = (path_data+'node119out1.tif',path_data+'node119out2.txt')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.threshold_result(command,'-p 10.0 -s otsu -r 1',input,output)
img = cv2.imread('node119out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node120out1.tif',path_data+'node113out1.tif')
output = (path_data+'node122out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul_result(command,'',input,output)
img = cv2.imread('node122out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node107out1.tif')
output = (path_data+'node126out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink_result(command,'-p 0.5',input,output)
img = cv2.imread('node126out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node122out1.tif')
output = (path_data+'node60out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.cwtsd_result(command,'-r 4',input,output)
img = cv2.imread('node60out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node60out1.tif',path_data+'node32out1.tif')
output = (path_data+'node130out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.reconstruct_result(command,'-r 4',input,output)
img = cv2.imread('node130out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node130out1.tif',path_data+'node60out1.tif')
output = (path_data+'node134out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.minusabs_result(command,'',input,output)
img = cv2.imread('node134out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node134out1.tif',path_data+'node73out1.txt')
output = (path_data+'node136out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gclose_result(command,'-r 1',input,output)
img = cv2.imread('node136out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node136out1.tif')
output = (path_data+'node137out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node137out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node130out1.tif',path_data+'node137out1.tif')
output = (path_data+'node77out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul_result(command,'',input,output)
img = cv2.imread('node77out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node77out1.tif',path_data+'node73out1.txt')
output = (path_data+'node72out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.gerosion_result(command,'-r 1',input,output)
img = cv2.imread('node72out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node72out1.tif')
output = (path_data+'node129out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.invert_result(command,'',input,output)
img = cv2.imread('node129out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node129out1.tif',path_data+'node137out1.tif')
output = (path_data+'node138out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.mul_result(command,'',input,output)
img = cv2.imread('node138out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node82out1.tif',path_data+'node107out1.tif',path_data+'node138out1.tif')
output = (path_data+'node110out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.movl_result(command,'-s white,magenta,pink',input,output)
img = cv2.imread('node110out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node138out1.tif')
output = (path_data+'node123out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.shrink_result(command,'-p 0.5',input,output)
img = cv2.imread('node123out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node127out1.tif',path_data+'node126out1.tif',path_data+'node123out1.tif')
output = (path_data+'node125out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.movl_result(command,'-s white,magenta,pink',input,output)
img = cv2.imread('node125out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)

input = (path_data+'node123out1.tif',path_data+'node127out1.tif')
output = (path_data+'node133out1.tif')
if type(output) != type('abc'):
	output = ','.join(output)
if type(input) != type('abc'):
	input = ','.join(input)
fun.max_result(command,'',input,output)
img = cv2.imread('node133out1.tif')
if(show_flag == 1 and img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
