# Design Patterns: Transporte Escolar

## 🚌 Sobre o projeto

Projeto em Python que demonstra a aplicação de diversos _design patterns_ no contexto de um sistema de transporte escolar. O objetivo é servir como referência educativa para quem quer aprender padrões de projeto (como Strategy, Observer, Decorator etc.) e ver como eles podem ser aplicados em um cenário realista de sistema de transporte.


## 🔧 Arquitetura e organização

A estrutura de pastas está segmentada por responsabilidade / padrão, por exemplo:

- `domain/` — classes de domínio, entidades e lógica central.  
- `infra/` — código de infraestrutura para armazenamento local de dados.  
- `strategies/`, `observers/`, `decorators/` — implementação dos padrões respectivos.  
- `app/` — código da interface CLI da aplicação.  
- `main.py` — ponto de entrada do sistema, onde você pode testar/executar o projeto.

Essa organização facilita navegar entre os diferentes padrões utilizados, comparar implementações e estender com novos padrões ou funcionalidades.

## ✅ Funcionalidades demonstradas

- uso de padrão **Strategy** para definir diferentes modos de cobrança das rotas.  
- Uso de padrão **Observer** para notificar o sucesso ou falha na execução de rotas selecionadas pelo usuário.
- Aplicação de **Decorator** para estender comportamentos — por exemplo, adicionar funcionalidades de informar pontos extras em uma rota sem modificar sua estrutura original.  
- **Singleton** _Data_ para realizar o armazenamento local dos dados da aplicação. 

> 💡 O foco principal é didático — o código serve para ilustrar como aplicar _design patterns_ de forma organizada e compreensível, e não como um sistema pronto para produção.

## 🚀 Como executar / testar o projeto

Para executar os exemplos do projeto, siga os passos abaixo:

```bash
# Clone o repositório
git clone https://github.com/Kalyo-silva/DesignPatterns-TransporteEscolar.git
cd DesignPatterns-TransporteEscolar

# Execute o script principal
python main.py
```

## ⚙️ Fluxo de trabalho da aplicação

- Navegar o **menu** utilizando os numeros informados antes de cada opção.
- Cadastrar **rotas**, informado Titulo, distância, quantidade de pontos, quantidade de alunos vinculados e tipo de cobrança da rota.
- Cadastrar **veículos**, informando marca, modelo e Eficiencia de consumo de combustível
-  Seguir para a seção de **Execução**, onde será selecionado uma rota, um veículo e informado o valor do combustível no momento da execução.
- Obtenção dos **Resultados**
- Verificação de **notificações**, caso a rota seja definida como acompanhada durante a sua criação.

## 👤 Contato
- Autor: Kalyo Airan da Silva
- GitHub: https://github.com/Kalyo-silva
- Email: kalyo.silva@unidavi.edu.br
