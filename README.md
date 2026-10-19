# Projeto-Integrador-Fatec
Repositorio de projetos para o curso de analise e desenvolvimento na faculdade de tecnologia de são paulo (FATEC)

## FATEC Bank

O programa `fatec_bank.py` guarda as movimentacoes em `movimentacoes.csv`,
criado na mesma pasta do programa quando o primeiro deposito ou saque for
realizado. O arquivo usa `;` como separador e pode ser aberto em um editor de
texto ou planilha. Para continuar funcionando, mantenha o cabecalho e as
colunas do arquivo; os valores numericos devem usar ponto como separador decimal.

Ao iniciar, o programa carrega o historico do CSV e usa o saldo final da ultima
movimentacao de cada conta. Se o arquivo ainda nao existir, sao usados os saldos
iniciais definidos no programa.
