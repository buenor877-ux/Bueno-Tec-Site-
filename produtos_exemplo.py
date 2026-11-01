# =========================================================
# PRODUTOS DE EXEMPLO (só para encher a loja enquanto você pratica)
#
# ATENÇÃO: estes produtos e preços NÃO são reais.
# Antes de colocar a loja no ar, faça UMA destas duas coisas:
#   1) No app.py, troque  MOSTRAR_EXEMPLOS = True  por  False
#      (todos os exemplos somem de uma vez), ou
#   2) Troque cada exemplo por um produto real, com foto própria.
#
# Cada exemplo aparece no site com o selo "Exemplo".
# =========================================================

def _exemplo(categoria, imagem, nome, preco, descricao):
    return {
        "nome": nome,
        "marca": "",
        "categoria": categoria,
        "descricao": descricao,
        "preco": preco,
        "imagem": imagem,
        "exemplo": True,
    }


EXEMPLOS = [
    # ---- Roupas
    _exemplo("Roupas", "roupas.jpg", "Camiseta Básica de Algodão", 29.90, "Camiseta confortável para o dia a dia."),
    _exemplo("Roupas", "roupas.jpg", "Calça Jeans Masculina", 89.90, "Calça jeans com corte reto e bom caimento."),
    _exemplo("Roupas", "roupas.jpg", "Vestido Casual Feminino", 69.90, "Vestido leve, ideal para o calor."),
    # ---- Calçados
    _exemplo("Calçados", "calcados.jpg", "Tênis Esportivo Casual", 119.90, "Tênis leve para caminhada e uso diário."),
    _exemplo("Calçados", "calcados.jpg", "Chinelo Slide Confortável", 24.90, "Chinelo macio com solado antiderrapante."),
    _exemplo("Calçados", "calcados.jpg", "Sandália Feminina Rasteira", 49.90, "Sandália confortável para todas as ocasiões."),
    # ---- Acessórios
    _exemplo("Acessórios", "acessorios.jpg", "Relógio Digital Esportivo", 59.90, "Relógio digital com cronômetro e luz."),
    _exemplo("Acessórios", "acessorios.jpg", "Óculos de Sol Unissex", 39.90, "Óculos com proteção UV, estilo clássico."),
    _exemplo("Acessórios", "acessorios.jpg", "Cinto de Couro Sintético", 34.90, "Cinto resistente com fivela metálica."),
    # ---- Bolsas
    _exemplo("Bolsas", "bolsas.jpg", "Bolsa Feminina Tiracolo", 79.90, "Bolsa prática com alça ajustável."),
    _exemplo("Bolsas", "bolsas.jpg", "Mochila Casual Reforçada", 99.90, "Mochila com vários compartimentos."),
    _exemplo("Bolsas", "bolsas.jpg", "Pochete Esportiva", 29.90, "Pochete leve para guardar o essencial."),
    # ---- Eletrônicos
    _exemplo("Eletrônicos", "eletronicos.jpg", "Cabo USB-C Reforçado 1m", 19.90, "Cabo resistente para carga e dados."),
    _exemplo("Eletrônicos", "eletronicos.jpg", "Caixa de Som Bluetooth Portátil", 89.90, "Som potente e fácil de levar."),
    # ---- Casa
    _exemplo("Casa", "casa.jpg", "Garrafa Térmica 1 Litro", 49.90, "Mantém bebidas quentes ou frias por horas."),
    _exemplo("Casa", "casa.jpg", "Jogo de Panelas Antiaderente 3 Peças", 129.90, "Panelas fáceis de limpar."),
    # ---- Ferramentas
    _exemplo("Ferramentas", "ferramentas.jpg", "Jogo de Chaves de Fenda 6 Peças", 29.90, "Chaves de vários tamanhos para reparos."),
    _exemplo("Ferramentas", "ferramentas.jpg", "Trena 5 Metros", 19.90, "Trena com trava e fita resistente."),
    _exemplo("Ferramentas", "ferramentas.jpg", "Alicate Universal 8 Polegadas", 34.90, "Alicate com cabo emborrachado."),
    # ---- Brinquedos
    _exemplo("Brinquedos", "jogos.jpg", "Quebra-Cabeça 200 Peças", 24.90, "Diversão para toda a família."),
    _exemplo("Brinquedos", "jogos.jpg", "Jogo de Tabuleiro Família", 59.90, "Jogo para reunir amigos e família."),
    _exemplo("Brinquedos", "jogos.jpg", "Carrinho de Fricção Colorido", 19.90, "Carrinho resistente para os pequenos."),
    # ---- Beleza
    _exemplo("Beleza", "beleza.jpg", "Kit de Pincéis de Maquiagem", 34.90, "Pincéis macios para o dia a dia."),
    _exemplo("Beleza", "beleza.jpg", "Escova Alisadora Elétrica", 109.90, "Escova com aquecimento rápido."),
    _exemplo("Beleza", "beleza.jpg", "Hidratante Corporal 400ml", 24.90, "Hidratação suave para todos os tipos de pele."),
    # ---- Informática
    _exemplo("Informática", "informatica.jpg", "Teclado USB ABNT2", 49.90, "Teclado completo com teclas silenciosas."),
    _exemplo("Informática", "informatica.jpg", "Pen Drive 64GB", 44.90, "Armazenamento prático para levar seus arquivos."),
    # ---- Áudio e Vídeo
    _exemplo("Áudio e Vídeo", "audio.jpg", "Fone de Ouvido com Fio P2", 19.90, "Fone simples com bom som."),
    _exemplo("Áudio e Vídeo", "audio.jpg", "Fone Bluetooth Sem Fio", 79.90, "Fone sem fio com microfone embutido."),
    _exemplo("Áudio e Vídeo", "audio.jpg", "Cabo HDMI 1,5 Metros", 24.90, "Imagem e som em alta definição."),
    # ---- Livros
    _exemplo("Livros", "livros.jpg", "Livro de Receitas Práticas", 34.90, "Receitas rápidas para o dia a dia."),
    _exemplo("Livros", "livros.jpg", "Livro de Colorir Adulto", 22.90, "Para relaxar e soltar a criatividade."),
    _exemplo("Livros", "livros.jpg", "Agenda Planner Anual", 39.90, "Organize seus compromissos o ano todo."),
    # ---- Móveis
    _exemplo("Móveis", "moveis.jpg", "Prateleira Decorativa de Parede", 49.90, "Prateleira para livros e enfeites."),
    _exemplo("Móveis", "moveis.jpg", "Banco Multiuso Dobrável", 69.90, "Banco firme que dobra para guardar."),
    _exemplo("Móveis", "moveis.jpg", "Sapateira Organizadora", 89.90, "Organiza até 12 pares de calçados."),
    # ---- Esportes
    _exemplo("Esportes", "esportes.jpg", "Corda de Pular Ajustável", 19.90, "Corda com cabo antiderrapante."),
    _exemplo("Esportes", "esportes.jpg", "Par de Halteres 2kg", 49.90, "Halteres para treino em casa."),
    _exemplo("Esportes", "esportes.jpg", "Tapete de Yoga EVA", 59.90, "Tapete antiderrapante e confortável."),
    # ---- Automotivo
    _exemplo("Automotivo", "carros.jpg", "Aromatizante Automotivo", 12.90, "Perfume agradável para o carro."),
    _exemplo("Automotivo", "carros.jpg", "Suporte de Celular para Carro", 29.90, "Suporte firme para painel ou ventilação."),
    _exemplo("Automotivo", "carros.jpg", "Capa de Volante", 34.90, "Capa que protege e melhora a pegada."),
    # ---- Infantil
    _exemplo("Infantil", "infantil.jpg", "Copo com Canudo Infantil", 19.90, "Copo antivazamento para os pequenos."),
    _exemplo("Infantil", "infantil.jpg", "Mochila Escolar Infantil", 69.90, "Mochila leve com estampa divertida."),
    _exemplo("Infantil", "infantil.jpg", "Kit Massinha de Modelar", 24.90, "Massinha atóxica em várias cores."),
]
