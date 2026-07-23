
import eatiht.v2 as v2
import glob
path = '/home/zelalem/Desktop/html/*.html' # a path which contains the whole html pages

files=glob.glob(path)

for i in files:

    files = "file://"+str(i)
    files = files.replace("[", "")
    files = files.replace("]", "")
    ccc = files.replace("'", "")
    read_file = ccc.read()

    # print read_file
    # for xx in ccc:
    #
    #     read_html = open(xx)
    #     read_file = read_html.read()
    #     print read_file
    #     extracted_txt = (v2.extract(read_file))
    #     full_path =  file.split('/')
    #     exact_path =  full_path[5].split('.') # this should to changed according to your path
    #     final_file_name = exact_path[0]
    #     file_write = open('/home/zelalem/Desktop/html_out/'+'.txt','w') # a path which contains a file to write
    #     file_write.write(extracted_txt)
    #
    #     file_write.close()
    #
