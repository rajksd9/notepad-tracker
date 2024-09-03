import os 
counter=1
def save_file_to_local(data):
    global counter
    if not os.path.exists("Notes"):
        os.mkdir("Notes")
  
    fileName=f"Note-{counter}"
    with open(f"Notes/{fileName}.txt","w") as file:
        for linedata in data:
            file.write(linedata)
    counter=counter+1


