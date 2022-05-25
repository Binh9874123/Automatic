import os 
import cv2
os.system('prostak.exe -o strel -s 9,9,square node4out1.out')
img = cv2.imread('node4out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o threshold -p 10.0 -s otsu -r 1 C:\\ProStack\\share\\prostack\\examples\\k167\\d218.tif node21out1.out,node21out2.out')
img = cv2.imread('node21out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o strel -s 3,3,square node31out1.out')
img = cv2.imread('node31out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o expand -p 2.0 C:\\ProStack\\share\\prostack\\examples\\k167\\d218.tif node35out1.out')
img = cv2.imread('node35out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o strel -s 3,3,square node48out1.out')
img = cv2.imread('node48out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o strel -s 23,23,disk node59out1.out')
img = cv2.imread('node59out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o strel -s 3,3,square node73out1.out')
img = cv2.imread('node73out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o expand -p 2.0 C:\\ProStack\\share\\prostack\\examples\\k167\\f218.tif node82out1.out')
img = cv2.imread('node82out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o expand -p 2.0 C:\\ProStack\\share\\prostack\\examples\\k167\\r218.tif node83out1.out')
img = cv2.imread('node83out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o strel -s 9,9,disk node95out1.out')
img = cv2.imread('node95out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o strel -s 5,5,square node112out1.out')
img = cv2.imread('node112out1.out')
if(img is not None):
	cv2.imshow('photo',img)
cv2.waitKey(500)
os.system('prostak.exe -o shrink -p 0.5 node82out1.out node127out1.out')
img = cv2.imread('node127out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o mul  node21out1.out,C:\\ProStack\\share\\prostack\\examples\\k167\\d218.tif node19out1.out')
img = cv2.imread('node19out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o heq  node19out1.out,node21out1.out node27out1.out')
img = cv2.imread('node27out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node82out1.out node41out1.out')
img = cv2.imread('node41out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o heq  node41out1.out node80out1.out')
img = cv2.imread('node80out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o heq  node83out1.out node81out1.out')
img = cv2.imread('node81out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o despekle -r 4 node80out1.out node84out1.out')
img = cv2.imread('node84out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o despekle -r 4 node81out1.out node85out1.out')
img = cv2.imread('node85out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o andif -s 10,0.5,0.9,frac node27out1.out node7out1.out')
img = cv2.imread('node7out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o expand -p 2.0 node7out1.out node23out1.out')
img = cv2.imread('node23out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node84out1.out,node48out1.out node47out1.out')
img = cv2.imread('node47out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node85out1.out,node48out1.out node49out1.out')
img = cv2.imread('node49out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o avg  node47out1.out,node49out1.out node50out1.out')
img = cv2.imread('node50out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o andif -s 20,0.3,0.7,frac node50out1.out node87out1.out')
img = cv2.imread('node87out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node23out1.out,node4out1.out node3out1.out')
img = cv2.imread('node3out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o reconstruct -r 4 node23out1.out,node3out1.out node5out1.out')
img = cv2.imread('node5out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node5out1.out node6out1.out')
img = cv2.imread('node6out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node6out1.out,node4out1.out node8out1.out')
img = cv2.imread('node8out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o reconstruct -r 4 node6out1.out,node8out1.out node9out1.out')
img = cv2.imread('node9out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o cwtsd -r 4 node9out1.out node18out1.out')
img = cv2.imread('node18out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o mul  node18out1.out,node23out1.out node26out1.out')
img = cv2.imread('node26out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node87out1.out,node59out1.out node52out1.out')
img = cv2.imread('node52out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o reconstruct -r 4 node87out1.out,node52out1.out node57out1.out')
img = cv2.imread('node57out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o threshold -p 3.0 -s plain -r 1 node26out1.out node22out1.out,node22out2.out')
img = cv2.imread('node22out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node22out1.out,node31out1.out node30out1.out')
img = cv2.imread('node30out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o median -r 1 node30out1.out,node31out1.out node32out1.out')
img = cv2.imread('node32out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gmag  node32out1.out node33out1.out')
img = cv2.imread('node33out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o threshold -p 1.0 -s plain -r 1 node33out1.out node34out1.out,node34out2.out')
img = cv2.imread('node34out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o movl -s magenta,yellow node34out1.out,node35out1.out node36out1.out')
img = cv2.imread('node36out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node57out1.out node54out1.out')
img = cv2.imread('node54out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node32out1.out,node112out1.out node111out1.out')
img = cv2.imread('node111out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node32out1.out node120out1.out')
img = cv2.imread('node120out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node54out1.out,node59out1.out node53out1.out')
img = cv2.imread('node53out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o reconstruct -r 4 node54out1.out,node53out1.out node58out1.out')
img = cv2.imread('node58out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gmag  node111out1.out node107out1.out')
img = cv2.imread('node107out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gclose -r 7 node58out1.out,node95out1.out node113out1.out')
img = cv2.imread('node113out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gmag  node113out1.out node117out1.out')
img = cv2.imread('node117out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o threshold -p 10.0 -s otsu -r 1 node117out1.out node119out1.out,node119out2.out')
img = cv2.imread('node119out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o mul  node120out1.out,node113out1.out node122out1.out')
img = cv2.imread('node122out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o shrink -p 0.5 node107out1.out node126out1.out')
img = cv2.imread('node126out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o cwtsd -r 4 node122out1.out node60out1.out')
img = cv2.imread('node60out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o reconstruct -r 4 node60out1.out,node32out1.out node130out1.out')
img = cv2.imread('node130out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o minusabs  node130out1.out,node60out1.out node134out1.out')
img = cv2.imread('node134out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gclose -r 1 node134out1.out,node73out1.out node136out1.out')
img = cv2.imread('node136out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node136out1.out node137out1.out')
img = cv2.imread('node137out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o mul  node130out1.out,node137out1.out node77out1.out')
img = cv2.imread('node77out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o gerosion -r 1 node77out1.out,node73out1.out node72out1.out')
img = cv2.imread('node72out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o invert  node72out1.out node129out1.out')
img = cv2.imread('node129out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o mul  node129out1.out,node137out1.out node138out1.out')
img = cv2.imread('node138out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o movl -s white,magenta,pink node82out1.out,node107out1.out,node138out1.out node110out1.out')
img = cv2.imread('node110out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o shrink -p 0.5 node138out1.out node123out1.out')
img = cv2.imread('node123out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o movl -s white,magenta,pink node127out1.out,node126out1.out,node123out1.out node125out1.out')
img = cv2.imread('node125out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)
os.system('prostak.exe -o max  node123out1.out,node127out1.out node133out1.out')
img = cv2.imread('node133out1.out')
if(img is not None):
	cv2.imshow('photo',img)
	cv2.waitKey(500)