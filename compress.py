import sys

#Matthew O'Neill
#3/8/2020

#Lempel–Ziv–Welch compression algorith for ascii text
#python 3.7.4

def compress(argv):

    MAX_TABLE_SIZE = (2**int(argv[1]))

    #assemble table for ascii characters
    table = {}
    for i in range(256):
        table.update({chr(i): i})

    string = ""
    #open input file and create file for binary output
    f = open(argv[0], 'r')
    out_file_name = ""
    out_file_name =  argv[0][:len(out_file_name) - 4]
    out_file_name = out_file_name + ".lzw"
    out = open(out_file_name, 'x')
    out.close()
    out = open(out_file_name, "wb")

    #iterate through character inputs and
    #build the table dynamically
    count = 256
    while True:
        char = f.read(1)
        if not char:
            break
        tempString = string + char
        if table.get(tempString) != None:
            string = string + char
        else:
            s = table.get(string)
            s = int(s)
            #convert to bytes in big indian encoding
            #and write to the output file
            out.write(s.to_bytes(2,'big'))
            #build on the table dynamically
            if len(table) < MAX_TABLE_SIZE:
                table.update({tempString : count})
                count = count + 1
            string = char

    s = table.get(string)
    s = int(s)
    #write to output file
    out.write(s.to_bytes(2,'big'))
    f.close()
    out.close()



if __name__ == "__main__":
    compress(sys.argv[1:])
