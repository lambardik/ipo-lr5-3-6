def create_unique_word_file(input_filename, output_filename):

  with open(input_filename, 'r',encoding = 'utf-8') as input_file, open(output_filename, 'w',encoding='utf-8') as output_file:
    words = set()
    for line in input_file:
      for word in line.split():
        words.add(word.lower())  # Добавляем слово в множество, не учитывая регистр
    for word in words:
      output_file.write(word + '\n')  # Записываем уникальные слова в выходной файл

input_filename = 'text.txt'
output_filename = 'output.txt'
create_unique_word_file(input_filename, output_filename)
print(f"Уникальные слова записаны в файл '{output_filename}'")