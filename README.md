<div align="center">

![LogoProductivity](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/17a6a928-22a4-4225-a66c-32396e09ad8c)

</div>

<br>

<div align="center">

![EllipseToDoList](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/3f71ecd0-7eb9-4f73-9056-269c7f337401)![EllipseBlocoDeNotas](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/5126925d-34b0-46cf-8857-17c08c224c93)![EllipseCalendario](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/c4f0660c-25de-484d-b003-c4ee4d9d1c63)![EllipsePomodoro](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/b230b07d-241b-467f-934e-b1d5cce33064)

</div>


---

# Productivity

No âmbito da disciplina de Programação 1, foi desenvolvido um projeto de aplicação de produtividade em Python, com o objetivo de fornecer aos usuários uma ferramenta abrangente para melhorar sua eficiência e organização pessoal. A aplicação engloba quatro sistemas principais: Todolist, Pomodoro, Calendário e Bloco de Anotações. Cada sistema oferece funcionalidades específicas para atender às diferentes necessidades dos usuários, proporcionando uma experiência integrada e centralizada para melhorar sua produtividade no dia a dia.


### 1. Todolist (Lista de Tarefas):
Uma Todolist é uma lista organizada de tarefas que precisam ser realizadas. É uma ferramenta eficaz para ajudar as pessoas a acompanhar e priorizar suas atividades diárias, semanais ou mensais. As tarefas geralmente são listadas com breves descrições e podem ser marcadas como concluídas à medida que são realizadas. Muitas vezes, aplicativos e ferramentas digitais são usados para criar e gerenciar listas de tarefas, tornando-as facilmente acessíveis em dispositivos eletrônicos.

### 2. Pomodoro:
A Técnica Pomodoro é um método de gerenciamento de tempo que envolve dividir o trabalho em intervalos de tempo curtos, geralmente 25 minutos, chamados "pomodoros", seguidos por uma pausa curta de 5 minutos. Após quatro pomodoros, é recomendada uma pausa mais longa de 15-30 minutos. Essa técnica visa aumentar a produtividade, minimizando a procrastinação e a fadiga mental, incentivando a concentração intensa durante os pomodoros.

### 3. Calendário:
Um calendário é uma representação visual dos dias, semanas e meses de um ano, usado para acompanhar datas e eventos importantes. Pode ser físico ou digital. Calendários ajudam na organização do tempo, permitindo que as pessoas agendem compromissos, lembrem-se de datas importantes, como aniversários e feriados, e planejem suas atividades futuras. Além disso, muitos calendários digitais permitem a sincronização com dispositivos móveis e colaboração entre usuários.

### 4. Bloco de Anotações:
Um bloco de anotações é um local onde as pessoas podem registrar informações importantes, ideias, listas, pensamentos e notas em geral. Pode ser um caderno físico, um aplicativo de anotações em dispositivos eletrônicos ou um software dedicado. Os blocos de anotações são utilizados para manter registros organizados e acessíveis, facilitando a referência futura e a organização de informações pessoais ou profissionais. Eles são uma ferramenta valiosa para capturar e arquivar conhecimento.


O projeto foi desenvolvido em linguagem Python devido à sua simplicidade, versatilidade e ampla gama de bibliotecas disponíveis. Além disso, a interface gráfica da aplicação foi criada usando uma biblioteca como o Tkinter para fornecer uma experiência de usuário amigável e intuitiva.

---

## 🎴 Imagens do projeto
### tela home 
![home](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/eb237c63-005a-4aff-9b55-69da7f55ec29)
### Tela To-do List
![To-do List](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/21281d80-82fc-4c58-883a-73889adc3835)
### Tela Bloco de notas
![Bloco-de-notas](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/7d570e23-b3c1-44a6-909f-06f5813e384e)
### Tela calendario
![Calendario](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/258d4129-5369-4471-846d-1cd3f024e266)
### Tela pomorodo
![Pomodoro](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/a0693459-01b5-4570-80a9-c6832d13f575)
### Tela team
![Team](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/8ecd5291-eb31-4340-b12a-9fef9b833573)
### Tela dashBoard
![dashBoard](https://github.com/Jeova-1704/Projeto-programacao-1/assets/127805808/19e953ed-94cf-4d92-ac1d-7b5257f08b7f)

---

### 📋 Pré-requisitos
```
Python 3.10
```
```
TKinter
```
```
Pillow~=10.0.0
```
```
tkcalendar~=1.6.1
```
```
tkcalendar~=1.6.1
```
---


### 🔧 Instalação

Primeiramente baixe o projeto em computador:
```
git clone https://github.com/Jeova-1704/Projeto-programacao-1
```
Após isso faça o download dos pré-requisitos do projeto
```
pip install -r requirements.txt
```
---

## 🛠️ como foi construido e com quais ferramentas

O projeto foi desenvolvido usando arquitetura MVC, divida em 4 pacores, sendo eles:
1. view
   1. Onde fica a parte visual do projeto, com todas as telas do sistema, como a do main, to-do list, pomodoro, calendario, bloco de notas, team e dashboard.
   2. pacote assets
      1. Onde se localiza as imagens do projeto, como logo e icones
2. utils
   1. Onde se localiza as constantes do proojeto, com cores, fontes e o Tooltip 
3. dao 
   1. Onde se localiza o banco de dados, junto com os codigos sqlite 3 que gerenciam os banco de dados 
4. core 
   1. Onde ficam as funcionalidades do sistema, que são as funções do projeto, que permitem que o projeto mude de tela, entre em contato com o banco de dados, etc.
---

## ✒️ Autores

* **Ana Oliveira** - *desenvolvedora* - [GitHub Ana Oliveira](https://github.com/holyvieri)
* **Arthur Lopes** - *desenvolvedor* - [GitHub Arthur Lopes](https://github.com/ArthurSampaio13)
* **Emerson Feitosa** - *desenvolvedor* - [GitHub Emerson Marcolino](https://github.com/emerson-feitosa)
* **Jeová Bezerra** - *desenvolvedor* - [GitHub Jeová Bezerra](https://github.com/Jeova-1704)
* **Pierre Monteiro** - *desenvolvedor* - [GitHub Marcos Pierre](https://github.com/PierreOF)
---

## 📄 Licença

...

---




