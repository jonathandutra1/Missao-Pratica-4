from Pessoa import Pessoa

pessoa = Pessoa("João", "2000-01-01", "000.111.222-33", "15975388-1", "false") 


print(f'Nome: {pessoa.nome}')
print(f'Data de Nascimento: {pessoa.dataNascimento}')
print(f'CPF: {pessoa.cpf}')
print(f'RG: {pessoa.rg}')
print(f'Status: {pessoa.status}')