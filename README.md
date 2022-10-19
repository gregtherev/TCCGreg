"# First Commit" 

## TABELA EQUIPE
## OS CAMPOS SÃO STRING NO BANCO, MAS SERÃO TRABALHADOS COMO UM SET() PARA MANIPULAÇÃO    
	questoes_acertadas[]: acertou uma questao, set.add(numero_questao)
	questoes_erradas[]:  errou uma quiestao, set.add(numero_questao)
	questoes_recuperadas[]: questoes com punicao, mas, acertadas posteriormente

	EM TODO ENVIO COM ACERTO
	if questao in questoes_erradas:
		questoes_erradas.remove(questao)
		questoes_recuperadas.add(questao)
		return

	if not questao in questoes_acertadas:
		questoes_acertadas.add(questao)
	return
	

	ENVIO DE ERRRO
	if not questao in questoes_erradas:
		questoes_erradas.add(questao)



## CORPO DO RETORNO DO ENDPOINT DO PLACAR:
	{
		[
			{
                equipe: equipegreg,
                acertos: 10,
                tempo relativo: 3600s,
                punicoes: 3,
                tempo formatado: 5400s,
                q_acertadas: [1, 3, 4, 5, 6, 9, 10],
                q_erradas: [8],
                q_recupearadas: [2, 7]
			},

			{
                equipe: equipeandrey,
                acertos: 10,
                tempo relativo: 3000s,
                punicoes: 2,
                tempo formatado: 4200s,
                q_acertadas: [],
                q_erradas: [],
                q_recupearadas: []
			}
		]
	}
