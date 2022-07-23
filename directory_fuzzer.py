#!/bin/python3

import requests
import argparse
import datetime

print("="*50)
print(" "*30+"DIRECTORY FUZZER")
print("="*50)

time = datetime.datetime.now()
print("Start : "+str(time))
print("="*50+"\n")
parser=argparse.ArgumentParser()
parser.add_argument("-u","--url",dest="url",required=True)
parser.add_argument("-x","--extentions",dest="extentions",required=False,nargs="+")
parser.add_argument("-w","--wordlist",dest="wordlist",required=False)
args = parser.parse_args()


def fuzz(target):
	try:
		r=requests.get(target)
		if r.status_code !=404:
			response_code=r.status_code
			response_size=len(r.content)
			print(f"[+] {target}   |   Status : {response_code} ---> Size : {response_size}")
	except:
		print("Fuzzing Failed !")
		print("="*50)
		exit()


target=''
response_code=0
response_size=0
filePath="/usr/share/wordlists/dirb/common.txt"

if args.url.startswith("http") == False:
	print("Invalid URL!")
	print("Example : http://example.com")
	exit()
else:
	URL = args.url

	
if args.wordlist:
	filePath=args.wordlist
		

wordlist=open(filePath,'r')


if args.extentions:
	extens = args.extentions
	for word in wordlist:
		word=word.strip()
		if word.startswith("#"):
			continue
		else:
			for ex in extens:
				target=URL+word+ex
				fuzz(target)
				
			
else:
	for word in wordlist:
		word=word.strip()
		if word.startswith("#"):
			continue
		else:
			
			target=URL+word
			fuzz(target)
				
		
time = datetime.datetime.now()
print("\n"+"="*50)
print("Finish : "+str(time))		
print("="*50)

	
		

