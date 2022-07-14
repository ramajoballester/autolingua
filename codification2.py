import openpyxl
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Automated replacement program')
parser.add_argument('-fases_filename', default='PRUEBA', help='Excel file with fases replacement columns')
parser.add_argument('-input_filename', default='CA_UNIVERSIDAD_LEXICO_FASE1-2', help='Input file to replace words from')
parser.add_argument('-extension', default='.xlsx', help='Default Excel files extension')
parser.add_argument('-filename_change', default='_new', help='Suffix for automated files')
parser.add_argument('-fase2_1_col', default='AB', help='Name of two columns for fase 2.1')
parser.add_argument('-fase2_2_col', default='CD', help='Name of two columns for fase 2.2')
parser.add_argument('-fase2_3_col', default='EF', help='Name of two columns for fase 2.3')
parser.add_argument('-fase3_col', default='GH', help='Name of two columns for fase 3')
parser.add_argument('-fase4_col', default='JK', help='Name of two columns for fase 4')
parser.add_argument('-input_col', default='D', help='Name of column for input file content')
parser.add_argument('-inplace', action='store_true', default=False, help='If true, change existing input file. Default: false')

args = parser.parse_args()



def get_column_data(sheet, column):
    return [cell.value for cell in sheet[column] if cell.value is not None]

fases_filename = os.path.join('..', args.fases_filename + args.extension)
fases_workbook = openpyxl.load_workbook(filename=fases_filename)
fases_sheet = fases_workbook.worksheets[0]

input_filename = os.path.join('..', args.input_filename + args.extension)
input_workbook = openpyxl.load_workbook(filename=input_filename)
input_sheet = input_workbook.worksheets[0]

if not args.inplace:
    output_filename = os.path.join('..', args.input_filename + args.filename_change + args.extension)
    shutil.copy(input_filename, output_filename)
else:
    output_filename = os.path.join('..', args.input_filename + args.extension)

output_workbook = openpyxl.load_workbook(filename=output_filename)
output_sheet = output_workbook.worksheets[0]


f2_1 = dict(zip(get_column_data(fases_sheet, args.fase2_1_col[0])[1:],
                get_column_data(fases_sheet, args.fase2_1_col[1])[1:]))
f2_2 = dict(zip(get_column_data(fases_sheet, args.fase2_2_col[0])[1:],
                get_column_data(fases_sheet, args.fase2_2_col[1])[1:]))
f2_3 = dict(zip(get_column_data(fases_sheet, args.fase2_3_col[0])[1:],
                get_column_data(fases_sheet, args.fase2_3_col[1])[1:]))
f3 = dict(zip(get_column_data(fases_sheet, args.fase3_col[0])[1:],
                get_column_data(fases_sheet, args.fase3_col[1])[1:]))
f4 = dict(zip(get_column_data(fases_sheet, args.fase4_col[0])[1:],
                get_column_data(fases_sheet, args.fase4_col[1])[1:]))


input_rows = get_column_data(input_sheet, args.input_col[0])[1:]
fases_dict = f2_1.copy()
fases_dict.update(f2_2)
fases_dict.update(f2_3)
fases_dict.update(f3)
fases_dict.update(f4)

n_changes = 0
for each_row in range(len(input_rows)):
    new_row = [each[1:] if each[0] == ' ' else each for each in input_rows[each_row].split(',')]
    for each_key in fases_dict.keys():
        for each_word in range(len(new_row)):
            if new_row[each_word] == each_key:
                n_changes += 1
                new_row[each_word] = fases_dict[each_key]

    new_row = ', '.join(new_row)
    output_sheet[args.input_col + str(each_row + 2)].value = new_row

print(output_filename)
output_workbook.save(filename=output_filename)


print('\n Input file: {}'.format(input_filename))
print(' Output file: {}'.format(output_filename))
print(' {} words have been replaced\n'.format(n_changes))



