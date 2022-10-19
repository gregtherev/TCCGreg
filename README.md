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

## Componente header

{{{
Nome do evento e nome da instituição
Para logo: quando for tela de time (logo do time)
tela pública (logo da instituição)

Compôr menu (horizontal, fixed, top):
	admin
	placar pública
	logout
	dashboard
	(OBS: mudar cor do menu no hover)

}}}


## Component timer

{{{
Data e hora de início do evento (lado esquerdo)
Tempo decorrido e tempo restante (lado direito)
Quando faltarem 5 minutos para finalizar, congelar o placar.
}}}


## Componente de placar
{{{
Lista das equipes participantes
Lista das questões no evento
Momento de início para cada equipe
Punições (tempo adicional em cada questão)
Punições (tempo total geral por equipe)

## Regras para tempo:
para cada questão resolvida, somar o tempo de resolução individual, ou seja, cada questão estará atrelada a quantidade de tempo que ela foi resolvida, somando-se todos os tempos de todas as questões ao final.

no caso de erro, soma-se uma punição temporal (por cada erro) ao tempo total

## Ordenação:

o django deverá fornecer num primeiro momento as equipes são retornadas em ordem alfabética. a partir daí elas devel vir do django ordenadas por quantidade de questões acertadas, mas o endpoint precisa retornar tb: quantidade de questões acertadas e quantidade de punições