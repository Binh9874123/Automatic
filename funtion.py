import os 
import cv2
def gerosion_result(command ,id , input ,output):
	os.system(command+' -o gerosion '+id+' '+input+' '+output)
	return output

def strel_result(command ,id , output):
	os.system(command+' -o strel '+id+' '+output)
	return output

def reconstruct_result(command ,id , input ,output):
	os.system(command+' -o reconstruct '+id+' '+input+' '+output)
	return output

def invert_result(command ,id , input ,output):
	os.system(command+' -o invert '+id+' '+input+' '+output)
	return output

def andif_result(command ,id , input ,output):
	os.system(command+' -o andif '+id+' '+input+' '+output)
	return output

def cwtsd_result(command ,id , input ,output):
	os.system(command+' -o cwtsd '+id+' '+input+' '+output)
	return output

def mul_result(command ,id , input ,output):
	os.system(command+' -o mul '+id+' '+input+' '+output)
	return output

def threshold_result(command ,id , input ,output):
	os.system(command+' -o threshold '+id+' '+input+' '+output)
	return output

def expand_result(command ,id , input ,output):
	os.system(command+' -o expand '+id+' '+input+' '+output)
	return output

def display_result(command ,id , input ,output):
	os.system(command+' -o display '+id+' '+input+' '+output)
	return output

def heq_result(command ,id , input ,output):
	os.system(command+' -o heq '+id+' '+input+' '+output)
	return output

def median_result(command ,id , input ,output):
	os.system(command+' -o median '+id+' '+input+' '+output)
	return output

def gmag_result(command ,id , input ,output):
	os.system(command+' -o gmag '+id+' '+input+' '+output)
	return output

def movl_result(command ,id , input ,output):
	os.system(command+' -o movl '+id+' '+input+' '+output)
	return output

def avg_result(command ,id , input ,output):
	os.system(command+' -o avg '+id+' '+input+' '+output)
	return output

def despekle_result(command ,id , input ,output):
	os.system(command+' -o despekle '+id+' '+input+' '+output)
	return output

def gclose_result(command ,id , input ,output):
	os.system(command+' -o gclose '+id+' '+input+' '+output)
	return output

def shrink_result(command ,id , input ,output):
	os.system(command+' -o shrink '+id+' '+input+' '+output)
	return output

def max_result(command ,id , input ,output):
	os.system(command+' -o max '+id+' '+input+' '+output)
	return output

def minusabs_result(command ,id , input ,output):
	os.system(command+' -o minusabs '+id+' '+input+' '+output)
	return output
