import gspread

sa = gspread.service_account(filename='service_file.json')
sh = sa.open("capsim")

wks = sh.add_worksheet(title='Year 1 differences', rows='50', cols= 20)

with open('year1_differences.csv', 'r') as file:
    content = file.read()

# Split the content into rows
rows = content.split('\n')

# Write each row to the worksheet
for row_index, row in enumerate(rows):
    values = row.split(',')
    wks.update(f"A{row_index+1}:{chr(ord('A') + len(values) - 1)}{row_index+1}", [values])
