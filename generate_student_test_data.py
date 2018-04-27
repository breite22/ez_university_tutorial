# generate_student_test_data


def main():
    infile_name = 'test_student_names.txt'
    outfile_name = 'student_names_python_code.txt'
    infile = open(infile_name, 'r')
    outfile = open(outfile_name, 'w')

    for line in infile:
        first, last = line.split()
        print('    {', file=outfile)
        print('        "first_name": "' + first + '",', file=outfile)
        print('        "last_name":  "' + last  + '",', file=outfile)
        print('         "nickname": ""', file=outfile)
        print('    },', file=outfile)

    infile.close()
    outfile.close()
    print('student names have been written to ' + outfile_name)


main()