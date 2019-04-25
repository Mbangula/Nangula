import re
import os

path_in = 'data/bible_raw/'
path_out = 'data/'

def parse_eng(output_file):
    f = open(path_in + 'john_eng.txt', 'r')
    lines = f.readlines()

    file = open(path_out + output_file,'w') 
    for i,text in enumerate(lines):
        lines[i] = re.sub('John [0-9]*:[0-9]*\t','',lines[i])
        file.write(lines[i])

    f.close()
    file.close()

def parse_osh(output_file):
    f = open(path_in + 'john_osh.txt', 'r')
    data = f.read()
    pattern = '\n\n.{1,100}\n\n.{1,100}\n\n'
    pattern2 = '\n\n.{1,100}\n\n'
    pattern3 = '\n{0,1}\s{0,1}[0-9]{1,2}\s'
    
    data = re.sub(pattern, '\s', data, flags=re.MULTILINE)
    data = re.sub(pattern2, '\s', data, flags=re.MULTILINE)

    #debug
    #matches = re.findall(pattern3, data, flags=re.MULTILINE)
    #print(len(matches))
    #print(matches)

    data = re.sub(pattern3, '\n', data, flags=re.MULTILINE)

    file = open(path_out + output_file,'w')
    file.write(data)
    file.close()

# Files must have equal amount of lines
def combine_files(file1, file2, output_file):
    f1 = open(path_out + file1, 'r')
    lines1 = f1.read().splitlines()
    f2 = open(path_out + file2, 'r')
    lines2 = f2.read().splitlines()
    output_data = ''

    for i, text in enumerate(lines1):
        output_data += lines1[i] + '\t' + lines2[i] + '\n'
    
    file = open(path_out + output_file, 'w')
    file.write(output_data)
    file.close()

    print('Combined ' + str(len(output_data.splitlines())) + ' lines into ' + output_file)
    # Clean up
    os.remove(path_out + file1)
    os.remove(path_out + file2)

if __name__ == '__main__':
    output_eng = 'john_eng_parsed.txt'
    output_osh = 'john_osh_parsed.txt'
    parse_eng(output_eng)
    parse_osh(output_osh)
    combine_files(output_eng, output_osh, 'john_eng-osh.txt')