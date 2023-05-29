# READ.me
#### Esse projeto faz parte do trabalho de conclusão de curso dos alunos: _Andrey Felicio_ e _Guilherme Gregório_ para o curso de Sistemas de Informação - Fundação Hermínio Ometto.
##### O trabalho escrito pode ser acessado [aqui]().

## Instalação

Esse projeto Python roda em [Django](https://www.djangoproject.com/) v4.1.

#### Para instalar o projeto localmente é necessário seguir os passos:

##### Clonar o projeto utilizando o comando:

```sh
git clone https://github.com/gregtherev/TCCGreg.git
```

##### Recomendamos usar um virtualenv para instalar as dependências, isso pode ser feito da seguinte maneira:

```sh
cd TCCGreg
python -m venv venv
```

##### Ativando o virtual env no _Windows_
```sh
cd .\venv\Scripts\
.\activate
```
_Linux_
```sh
source venv/bin/activate
```


##### Instalando as dependências necessárias:
```sh
pip install -r requirements.txt
```

##### Banco de dados

O projeto foi desenvolvido utilizando sqlite, para configurar o mesmo em sua máquina basta criar uma pasta "data" na raíz do projeto e executar o comando:
```sh
python manage.py migrate
```

##### Criando um superuser padrão

Para criar uma conta de admin em seu projeto basta executar o comando a seguir e inserir as informações solicitadas (email pode ser ignorado)
```sh
python .\manage.py createsuperuser
```

##### Executando o projeto

Para iniciar, por padrão no endereço _localhost:8000_, execute o comando:
```sh
python .\manage.py runserver
```

## Features

- Criação dos atores necessários para um evento (Alunos, Equipes, Juízes, Instituições, Eventos)
- Submissão de respostas dos problemas do evento
- Visualização do placar de cada evento em tempo real
- Histórico de submissões (individual ou geral caso a conta seja de Administrador)
- Acessar informações de eventos já finalizados
- Upload de arquivo pdf contendo questões para visualização dos participantes

## Observação

O cadastro das questões é feito através de um dicionário no ato de cadastro do evento. Este dicionário deve seguir o modelo chave[questão]: valor[alternativa correta].
```json
{
    "1": "a",
    "2": "b",
    "3": "a",
    "4": "c",
    "5": "d",
}
```

Os eventos possuem dois atributos que condicionam a renderização tanto do placar quanto dos botões disponíveis para uma equipe.

__is_active__ é o atributo responsável por marcar se um evento está ativo. Caso o mesmo esteja como ___false___, o botão para submissão de respostas não será renderizado para o usuário.
__is_finished__ é o atributo responsável por marcar a finalização de um evento. O placar do evento é congelado quando restarem apenas 5 minutos de competição, quando este atributo é marcado como ___true___ o placar final passa a ser exibido.

Para que um evento ocorra normalmente é necessário que durante sua duração, os atributos __is_active__ e __is_finished__ estejam marcados como ___true___ e ___false___ respectivamente. E para um evento finalizado basta seguir o caminho contrário, marcando __is_active__ e is_finished como ___false___ e ___true___ respectivamente.

Até o momento dessa publicação, essa atualização de atributos precisa ser feita pela interface do _Django Admin_.

## Direitos

FHO

__Esse projeto tem o intuito de ser passado para outros alunos da instiuição que tenham interesse em aprimorá-lo e expandi-lo para além da nossa universidade.__


_Agradecimento especial ao nosso orientador __Sérgio Antonello__ e à __Genese Lessa (o Dev mais arretado do Django)__ por todo apoio durante o desenvolvimento desse projeto._
