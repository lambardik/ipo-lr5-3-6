input_filename = 'text.txt'
output_filename = 'output.txt'

words = set()  

with open(input_filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
  for line in input_file:
    for word in line.split():
      words.add(word.lower())

  for word in words:
    output_file.write(word + '\n')

print(f"Уникальные слова записаны в файл '{output_filename}'")
