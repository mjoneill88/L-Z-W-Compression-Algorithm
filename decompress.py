import sys

#Matthew O'Neill
#3/8/2020

#Lempel–Ziv–Welch decompression algorithm for ascii text
#python 3.7.4

def decompress(argv):

    MAX_TABLE_SIZE = (2**int(argv[1]))

    #assemble table for ascii characters
    table = {}
    for i in range(256):
        table.update({i:chr(i)})

    #open byte input file and create file for
    #text output
    f = open(argv[0], 'rb')
    out_file_name = ""
    out_file_name = argv[0][:len(out_file_name) - 4]
    out_file_name = out_file_name + "_decoded.txt"
    out = open(out_file_name, 'x')

    #fetch first character from input file and
    #write to output file
    code = f.read(2)
    code = int.from_bytes(code, 'big')
    string = table[code]
    out.write(string)

    #iterate through all inputs in 2 byte chunks and
    #run LZW compression algorithm
    index_count = 256
    while True:
        code = f.read(2)

        if not code:
            break
        #convert 2-byte int into python int type,
        #using big indian encoding
        code = int.from_bytes(code, 'big')
        try:
            new_string = table[code]
        except KeyError:
            new_string = string + string[0]
        #output string to text file
        out.write(new_string)

        #build table dynamically
        if len(table) < MAX_TABLE_SIZE:
            table.update({index_count : string + new_string[0]})
            index_count = index_count + 1
        string = new_string
    f.close()
    out.close()


if __name__ == "__main__":
    decompress(sys.argv[1:])
