import sys
import os
import cv2
import automatic
import manual

print("1 - Automatic")
print("2 - Manual")
print("Choose an option: ")
option = input()

#main
if __name__ == "__main__":

    #python show.py mdsn_no_p/input backgrounds results
    #receive arguments: dataset_path, background_path, output_path
    dataset_path = sys.argv[1] #dataset_path = 'mdsn_no_p/input'
    background_path = sys.argv[2] #background_path = 'backgrounds'
    output_path = sys.argv[3] #output_path = 'results'

    string = " " + dataset_path + " " + background_path + " " + output_path

    if option == "1":
        os.system("python automatic.py" + string)
    elif option == "2":
        os.system("python manual.py" + string)
    else:
        print("Invalid option")
        sys.exit()