#!/bin/bash

url="http://www.ovh.net/files/1Mio.dat"
# for Header Information
curl -I ${url} 

#curl ${url} -O
#curl ${url} -o NewFileDownload
#curl ${url} > NewFileDownload2
