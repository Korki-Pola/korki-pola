## Zadanie 3: Użycie funkcji `input`

#**Cel:** Pobierz od użytkownika/Pobierz z pliku jego imię i wydrukuj "Hello, [imię]!".

with open('./zadanie3-input.txt') as input_file:
    lines = input_file.readlines()
    outputs = []

    for (index, line) in enumerate(lines):
        output = []

        name = line.strip()
        output_for_line = f'Output dla linijki [{index}]: {name}'

        print(output_for_line)
        output.append(output_for_line)

        hello_message = f'Hello, {name}!'

        print(hello_message)
        output.append(hello_message) 

        outputs.append(output)

    with open('./zadanie3-output.txt', 'w') as output_file:
        for output in outputs:
            for (index, line) in enumerate(output):
                output[index] = f'{line}\n'
            
            output_file.writelines(output)
            output_file.write('\n')
        


