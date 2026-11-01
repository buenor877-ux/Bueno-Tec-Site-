Bueno TEC

Loja virtual de artigos de informática e utilidades para casa, desenvolvida com Python e Flask. Os pedidos são finalizados pelo WhatsApp da loja.

Status: versão 1.0 concluída em 01/11/2026. Funciona localmente; ainda sem domínio próprio e sem hospedagem.

Sumário
Visão geral
Tecnologias
Funcionalidades
Estrutura do projeto
Como executar
Como adicionar produtos
Desenvolvimento
Problemas e bugs corrigidos
Próximos passos
Autor
1. Visão geral

A Bueno TEC é uma loja especializada em artigos de informática e uso geral para casa. O proprietário atua com vendas há mais de dois anos e, com o negócio sólido e em crescimento, criou este site para preparar a loja para uma etapa maior: levar os produtos a um público mais amplo, com interface simples, acessível e fluida.

O projeto começou como prática e teste de conhecimentos. Ao longo do desenvolvimento, tornou-se uma ferramenta real para expandir a imagem e as vendas da loja.

Como o cliente compra hoje: escolhe os produtos e as quantidades no carrinho e clica em "Comprar". O pedido é enviado ao WhatsApp da loja, onde a venda é finalizada.

Item	Informação
Início do projeto	19/08/2026
Conclusão da versão 1.0	01/11/2026
Catálogo atual	65 produtos em 15 categorias
Hospedagem	Ainda não publicado
2. Tecnologias
Camada	Tecnologia	Uso no projeto
Servidor	Python 3 + Flask	Rotas, páginas, busca e filtro por categoria
Páginas	HTML5 + Jinja2	Modelos reutilizáveis (base.html, componentes)
Estilo	CSS3 (Grid e Flexbox)	Layout responsivo e identidade visual
Interatividade	JavaScript	Carrinho, busca, quantidades e envio ao WhatsApp
Produção	Gunicorn	Servidor preparado para a futura hospedagem
Versionamento	Git e GitHub	Histórico e backup do código

As dependências estão em requirements.txt (Flask e Gunicorn).

3. Funcionalidades
Catálogo com 15 categorias preenchidas (a categoria Livros está reservada, ainda sem produtos).
Filtro por categoria e busca que ignora maiúsculas e acentos (por exemplo, "eletronicos" encontra "Eletrônicos").
Página inicial com produtos em destaque sorteados a cada visita.
Carrinho de compras: adicionar, aumentar e diminuir quantidades, total calculado automaticamente. O carrinho fica salvo no navegador e não esvazia ao trocar de página.
Finalização pelo WhatsApp: o pedido segue com os itens, as quantidades e o total.
Páginas institucionais: Sobre, Contato e página de erro 404 personalizada.
Responsivo: funciona em computador, tablet e celular.
SEO básico: títulos e descrições por página, textos alternativos nas imagens e idioma pt-BR.
Preços no formato brasileiro (R$ 35,00) por um filtro próprio do Flask.
4. Estrutura do projeto
Bueno-Tec-Site/
├── app.py                 # Aplicação Flask: produtos, categorias e rotas
├── produtos_exemplo.py    # Produtos de teste (desligados por padrão)
├── requirements.txt       # Dependências
├── templates/
│   ├── base.html          # Estrutura comum (cabeçalho, carrinho, rodapé)
│   ├── _componentes.html  # Peças reutilizáveis
│   ├── index.html         # Página inicial
│   ├── produtos.html      # Lista de produtos
│   ├── sobre.html
│   ├── contato.html
│   └── 404.html
└── static/
    ├── css/style.css      # Estilos
    ├── js/script.js       # Carrinho e interações
    └── imagens/           # Logo, categorias e fotos dos produtos
5. Como executar

Requisitos: Python 3 instalado.

bash
# 1. Entrar na pasta do projeto
cd Bueno-Tec-Site

# 2. (Opcional) criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate          # Windows

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Iniciar o servidor
python app.py

Abra no navegador o endereço exibido no terminal (normalmente http://127.0.0.1:5000).

Importante: o site só funciona enquanto o terminal com python app.py estiver aberto. Após alterar o código, pare o servidor (Ctrl+C), inicie de novo e atualize a página com Ctrl+F5.

6. Como adicionar produtos

Os produtos ficam na lista PRODUTOS, em app.py. Para cadastrar um novo:

Salve a foto em static/imagens/.
Copie um bloco { ... } existente e cole no fim da lista.
Troque os dados:
python
{
    "nome": 'Nome do produto',
    "marca": '',
    "categoria": 'Casa',            # use uma das categorias da lista CATEGORIAS
    "descricao": 'Descrição curta e clara.',
    "preco": 35.00,                 # ponto decimal, sem "R$"
    "imagem": 'nome_do_arquivo.jpg',
},
Reinicie o servidor e confira a página do produto.
7. Desenvolvimento

O projeto evoluiu em fases, sempre de forma gradual e sem copiar templates prontos.

Fase	Período	O que foi feito
1. Base visual	19/08/2026	Layout inicial em HTML5 e CSS Grid: menu, banner de inauguração e grade de categorias responsiva
2. Melhorias e SEO	Ago/2026	Ícones no lugar de emojis, hierarquia de títulos, tags semânticas, textos alternativos, paleta de cores e logomarca
3. Interatividade	29/08/2026	Busca em tempo real, "Ver todas" nas categorias, botões de compra, newsletter, rodapé, seções Sobre, diferenciais e Ofertas
4. Migração para Flask	05/09/2026	Separação em templates, static/css, static/js e static/imagens; style.css refeito; responsividade
5. Carrinho	08/09/2026	Contador, total, quantidade por produto, abertura e fechamento do menu do carrinho
6. Visual de loja profissional	09/09/2026	Reorganização do cabeçalho e das categorias, inspirada em grandes lojas virtuais
7. Catálogo real e fechamento da v1.0	Out–Nov/2026	Cadastro de 65 produtos reais com descrição, preço de venda e foto tratada; carrinho com envio ao WhatsApp; revisão geral
Decisões de projeto
Paleta de cores preservada em todas as etapas, mantendo a identidade da loja.
Produtos em uma lista Python (sem banco de dados), simples de editar nesta fase.
Fotos padronizadas em 600×600 px, fundo branco, sem marca d'água de outros vendedores.
Produtos de exemplo desligados por padrão (MOSTRAR_EXEMPLOS = False); só os produtos reais aparecem.
Modo debug desligado por padrão, para não expor o código quando o site estiver na internet.
8. Problemas e bugs corrigidos
#	Problema	Causa	Solução
1	CSS não carregava (erro 404) após a migração para Flask	Caminho do arquivo incorreto; o Flask serve arquivos pela pasta static	Ajuste dos caminhos para static/css/style.css; confirmado o funcionamento
2	Imagens e links quebrados	Caminhos absolutos do computador no HTML	Caminhos relativos e uso das pastas do Flask
3	Carrinho esvaziava ao trocar de página	O carrinho existia só na memória da página	Carrinho salvo no navegador
4	Produtos duplicados no carrinho	Cada clique criava um item novo	Produto repetido passa a aumentar a quantidade (find + contador)
5	Busca não encontrava palavras com acento	Comparação literal de texto	Função que ignora acentos e maiúsculas
6	Produtos novos não apareciam no site	O servidor antigo continuava ativo com o código anterior	Parar o servidor, reiniciar e usar Ctrl+F5 (ou janela anônima)
7	Fotos de fornecedores com marcas d'água, faixas e mãos	Imagens copiadas direto dos anúncios	Escolha de fotos limpas, recorte e remoção das áreas com marca
8	Modo debug exposto	Servidor iniciava sempre em debug	Debug só liga por variável de ambiente (FLASK_DEBUG=1)

Revisão: os itens 1 a 5 e 8 foram montados a partir do diário de desenvolvimento e do código atual. Confirme se descrevem o que aconteceu e ajuste a causa ou a data, se necessário.

9. Próximos passos

Curto prazo

Completar categorias com poucos itens (Infantil, Bolsas, Móveis) e preencher Livros.
Atualizar o texto da página Sobre com a história real da loja.
Botão que leve direto ao grupo do WhatsApp da loja.

Médio prazo

Publicar o site em um servidor (opções avaliadas: PythonAnywhere ou Render) e registrar um domínio próprio.
Divulgar nas redes sociais da loja.
Deixar o site mais leve e estável (otimização de imagens e carregamento).

Longo prazo

Ampliar muito o catálogo.
Melhorar o carrinho e o fluxo de pedidos.
Evoluir a interface para um visual mais sofisticado e profissional.
Migrar os produtos para um banco de dados e criar uma área administrativa para cadastrar itens sem editar código.
10. Autor

Leonardo Henrique Bueno, administrador e estudante de Engenharia de Software. Projeto desenvolvido como loja real e como portfólio de programação (Python, Flask, HTML, CSS e JavaScript).

GitHub: buenor877-ux
