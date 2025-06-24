aluno = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
if (media >= 7 and media <= 10):
    print(
        f'''
------------------------------------------------      
            notas do aluno: 
                1ª: {nota1}
                2ª: {nota2}
                3ª: {nota3}  
                4ª: {nota4}
            Média do aluno: {media}
        VOCÊ FOI APROVADO!!!!!!!!!!!
-------------------------------------------------      
      '''
    )
elif(media > 5 and media < 7):    
    print(
            f'''
    ------------------------------------------------      
                notas do aluno: 
                    1ª: {nota1}
                    2ª: {nota2}
                    3ª: {nota3}  
                    4ª: {nota4}
                Média do aluno: {media}
            VOCÊ ESTÁ DE RECUPERAÇÃO!!!!!!!!!!!
    -------------------------------------------------      
        '''
        )

elif (media >= 0 and media <= 4):   
    print(f'''
    ------------------------------------------------      
                notas do aluno: 
                    1ª: {nota1}
                    2ª: {nota2}
                    3ª: {nota3}  
                    4ª: {nota4}
                Média do aluno: {media}
        Você foi REPROVADO!!!!!!!!!!!!
    -------------------------------------------------      
        ''')
    
else:
    print("Média inválida")