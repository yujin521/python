import multiprocessing

#If the file is line based

fp=open('jinan.xlsx','rb')
content = fp.read().decode('utf-8')
with content as f:
    for line in f:
        multiprocessing.process(line) # <do something with line>

