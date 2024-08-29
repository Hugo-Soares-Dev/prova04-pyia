"""Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada. """

def media(n1, n2, n3):
    res = (n1 + n2 + n3)/ 3
    print(f'ao somar as notas ({n1}) - ({n2}) - ({n3}) a média aritmética é de: ({res:.2f})')
    return res

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))

media(nota1, nota2, nota3)
