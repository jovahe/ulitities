
import os

def get_file(file_path, file_type='.png'):
    L=[]
    for root,dirs,files in os.walk(file_path):
        for file in files:
            if os.path.splitext(file)[1]==file_type:
                L.append(os.path.join(root,file))
    return L

file_path = '/home/omnisky/PycharmProjects/data/test/'

if __name__=='__main__':
    png_files = get_file(file_path)
    xml_files = get_file(file_path, file_type='.xml')
    print ("\n\npng files as following: ")
    for tp in png_files:
        print("\n{}".format(tp))

    print ("\n\nxml files as following: ")
    for tp in xml_files:
        print("\n{}".format(tp))
