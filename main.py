import os.path
import glob
from PIL import Image 

trimr = 13
triml = 18

filenameExtension = "png"

targetPattern = r"input/*.{}".format(filenameExtension)

if __name__ == "__main__":
    
    daten = glob.glob(targetPattern)
    datenIndex = len(daten)
    
    for i in range (0 , datenIndex):
            
        filename = daten[i]
        img = Image.open(filename)
        
        string = str(os.path.basename(filename))
        l = len(string) - triml - 4
        string = string[trimr:l]
        print(string)
        path = "output/{}.{}".format(string, filenameExtension)
        
        img.save(path)
        
        
            
        
        
        
        
        
        

        