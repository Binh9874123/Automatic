import os 
import cv2
from wand.image import Image
def lhbg_result(command ,id , input ,output):
	os.system(command+' -o lhbg '+id+' '+input+' '+output)
	return output

def strel_result(command ,id , output):
	os.system(command+' -o strel '+id+' '+output)
	return output

def median3d_result(command ,id , input ,output):
	os.system(command+' -o median3d '+id+' '+input+' '+output)
	return output

def strel3d_result(command ,id , output):
	os.system(command+' -o strel3d '+id+' '+output)
	return output

def vaff_result(command ,id , input ,output):
	os.system(command+' -o vaff '+id+' '+input+' '+output)
	return output

def invert3d_result(command ,id , input ,output):
	os.system(command+' -o invert3d '+id+' '+input+' '+output)
	return output

def gerosion3d_result(command ,id , input ,output):
	os.system(command+' -o gerosion3d '+id+' '+input+' '+output)
	return output

def reconstruct3d_result(command ,id , input ,output):
	os.system(command+' -o reconstruct3d '+id+' '+input+' '+output)
	return output

def mul3d_result(command ,id , input ,output):
	os.system(command+' -o mul3d '+id+' '+input+' '+output)
	return output

def vmax_result(command ,id , input ,output):
	os.system(command+' -o vmax '+id+' '+input+' '+output)
	return output

def despekle3d_result(command ,id , input ,output):
	os.system(command+' -o despekle3d '+id+' '+input+' '+output)
	return output

def hno_result(command ,id , input ,output):
	os.system(command+' -o hno '+id+' '+input+' '+output)
	return output

def imcanny_result(command ,id , input ,output):
	with Image(filename = input) as image:
		with image.clone() as canny:
			canny.canny(0, 1, 0.1, 0.3)
			canny.save(filename =output)
	return output

def chole_result(command ,id , input ,output):
	os.system(command+' -o chole '+id+' '+input+' '+output)
	return output

def distance_result(command ,id , input ,output):
	os.system(command+' -o distance '+id+' '+input+' '+output)
	return output

def cwtsd_result(command ,id , input ,output):
	os.system(command+' -o cwtsd '+id+' '+input+' '+output)
	return output

def sselect_result(command ,id , input ,output):
	os.system(command+' -o sselect '+id+' '+input+' '+output)
	return output

def vstrel_result(command ,id , input ,output):
	os.system(command+' -o vstrel '+id+' '+input+' '+output)
	return output

def qu3d2csv_result(command ,id , input ,output):
	os.system(command+' -o qu3d2csv '+id+' '+input+' '+output)
	return output

def qu3dinit_result(command ,id , input ,output):
	os.system(command+' -o qu3dinit '+id+' '+input+' '+output)
	return output

def expand3d_result(command ,id , input ,output):
	os.system(command+' -o expand3d '+id+' '+input+' '+output)
	return output

def shrink3d_result(command ,id , input ,output):
	os.system(command+' -o shrink3d '+id+' '+input+' '+output)
	return output

def gopen_result(command ,id , input ,output):
	os.system(command+' -o gopen '+id+' '+input+' '+output)
	return output

def turn3d_result(command ,id , input ,output):
	os.system(command+' -o turn3d '+id+' '+input+' '+output)
	return output

def apee3d_result(command ,id , input ,output):
	os.system(command+' -o apee3d '+id+' '+input+' '+output)
	return output

def geometry3d_result(command ,id , input ,output):
	os.system(command+' -o geometry3d '+id+' '+input+' '+output)
	return output

def qu3d_result(command ,id , input ,output):
	os.system(command+' -o qu3d '+id+' '+input+' '+output)
	return output

def quremask_result(command ,id , input ,output):
	os.system(command+' -o quremask '+id+' '+input+' '+output)
	return output
