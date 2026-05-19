<div align="center">
<a href="https://ibb.co/ZRgbgC7v"><img src="https://i.ibb.co/LDgsgfHB/Plus-AB.png" alt="Plus-AB" border="0"></a>
<br><br>

[![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white)](https://spring.io/projects/spring-boot)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
<br>
[![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com/)

---

## 📋 Sobre o Projeto

O **Aquality** é um software de monitoramento inteligente de hidratação corporal, desenvolvido especificamente para otimizar a performance e a segurança de atletas de alto rendimento. 

Nascido de uma cooperação tecnológica e científica entre a **Centro Universitário São Camilo** e o **Instituto Mauá de Tecnologia (IMT)**, o sistema une a expertise da saúde com a excelência em engenharia e desenvolvimento de software.

</div>

### 🚀 Como Funciona?
A plataforma centraliza dados fisiológicos cruciais e níveis de hidratação em tempo real. Isso permite que comissões técnicas — compostas por treinadores, médicos e nutricionistas — tenham acesso a métricas precisas e baseadas em evidências para tomadas de decisão rápidas e eficazes.

### 🎯 Diferenciais Estratégicos
Mais do que um simples painel de visualização, o **Aquality** atua como uma ferramenta preditiva e estratégica que proporciona:
* **Recomendações Personalizadas:** Ajustes individuais de hidratação de acordo com a demanda de cada atleta.
* **Prevenção de Fadiga:** Mitigação da queda de rendimento físico causada pela desidratação.
* **Redução de Riscos à Saúde:** Monitoramento ativo para evitar quadros severos de estresse térmico e desequilíbrio eletrolítico.

---

## 🛠️ Como Iniciar o Projeto

Siga as instruções abaixo para configurar e executar os ambientes de Front-end e Back-end da aplicação.

### 💻 1. Inicializar o Front-end Web

Abra o terminal e navegue até o diretório do Front-end:

```bash
cd SC_HydraSense/SC-HydraSense/sc-hydrasense-web/Front-End
Bash
# Instale as dependências necessárias
npm install

# Inicie o servidor de desenvolvimento
npm run dev
(Nota: Caso o script do seu package.json utilize a nomenclatura tradicional do React, você também pode tentar npm run start se o comando acima não funcionar).

Após inicializar, conecte-se à porta local disponível exibida no terminal (ex: http://localhost:5173 ou http://localhost:3000).

⚙️ 2. Inicializar o Back-end Web
Passo A: Configuração do Banco de Dados
Abra o seu MySQL Workbench (ou gerenciador de banco de dados de sua preferência) e execute o seguinte comando para criar o banco de dados do projeto:

SQL
CREATE DATABASE hydrasense;
Passo B: Executar a Aplicação Spring Boot
Abra um novo terminal na raiz do projeto back-end:

Bash
# Instale as dependências do terminal
npm install
Em seguida, execute o comando correspondente ao seu sistema operacional para rodar o servidor Spring Boot:

No Linux / macOS:

Bash
./mvnw spring-boot:run
No Windows (Prompt de Comando ou PowerShell):

DOS
mvnw spring-boot:run
Desenvolvido por 

