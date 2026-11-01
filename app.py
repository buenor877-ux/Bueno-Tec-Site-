import os
import random
import unicodedata

from flask import Flask, render_template, request

from produtos_exemplo import EXEMPLOS

app = Flask(__name__)


# =========================================================
# PRODUTOS DA LOJA
#
# Para ADICIONAR um produto: copie um bloco { ... } inteiro,
# cole no fim da lista e troque os dados.
# A imagem precisa estar na pasta static/imagens.
# O preço é escrito com ponto (35.00), sem "R$".
# =========================================================
CATEGORIAS = [
    "Roupas", "Calçados", "Acessórios", "Bolsas", "Eletrônicos", "Casa",
    "Ferramentas", "Brinquedos", "Beleza", "Informática", "Áudio e Vídeo",
    "Livros", "Móveis", "Esportes", "Automotivo", "Infantil",
]

PRODUTOS = [
    {
        "nome": "Extensão Elétrica 10A Bivolt",
        "marca": "Prismatec",
        "categoria": "Eletrônicos",
        "descricao": (
            "Extensão elétrica de 10 metros, cor preta e 10A bivolt, ideal "
            "para ligar seus aparelhos com segurança e praticidade no dia a dia."
        ),
        "preco": 35.00,
        "imagem": "extensao.jpg",
    },
    {
        "nome": "Processador Manual de Alimentos 900ml",
        "marca": "Shock Imports",
        "categoria": "Casa",
        "descricao": (
            "O Processador Manual de Alimentos 900ml da Shock Imports é um "
            "utensílio indispensável para agilizar o preparo de receitas."
        ),
        "preco": 35.00,
        "imagem": "processador.jpg",
    },
    {
        "nome": "Secador de Cabelo Bee Electrics HD-3201",
        "marca": "Bee Electrics",
        "categoria": "Beleza",
        "descricao": (
            "Secador de cabelo compacto para uso doméstico, com potência "
            "de 1600W e voltagem de 127V."
        ),
        "preco": 85.00,
        "imagem": "secador.jpg",
    },
    {
        "nome": "Jogo de Talheres 25 Peças IDee Home",
        "marca": "IDee Home",
        "categoria": "Casa",
        "descricao": (
            "Jogo de talheres com 25 peças, combinando aço inoxidável e "
            "cabos plásticos ergonômicos."
        ),
        "preco": 45.00,
        "imagem": "talheres.jpg",
    },
    {
        "nome": "Mouse Sem Fio 2.4GHz Ergonômico",
        "marca": "",
        "categoria": "Informática",
        "descricao": (
            "Mouse sem fio com conexão 2.4GHz de até 10 metros, sensor óptico "
            "de 1200 DPI e design ergonômico. Instalação plug & play, "
            "compatível com Windows, macOS e Linux."
        ),
        "preco": 35.00,
        "imagem": "mouse_sem_fio.jpg",
    },
    {
        "nome": "Carregador de Parede Turbo com Cabo USB-C",
        "marca": "",
        "categoria": "Eletrônicos",
        "descricao": (
            "Carregador de parede com carregamento rápido e cabo USB-C "
            "incluso. Compacto e prático para casa, trabalho ou viagem."
        ),
        "preco": 35.00,
        "imagem": "carregador_turbo.jpg",
    },
    {
        "nome": "Ring Light de Mesa com Tripé e Suporte para Celular",
        "marca": "",
        "categoria": "Eletrônicos",
        "descricao": (
            "Anel de luz LED para mesa com tripé, suporte para celular e "
            "conexão USB. Ideal para selfies, vídeos, maquiagem e lives."
        ),
        "preco": 35.00,
        "imagem": "ring_light.jpg",
    },
    {
        "nome": "Kit 5 Potes Herméticos para Alimentos",
        "marca": "",
        "categoria": "Casa",
        "descricao": (
            "Kit com 5 potes herméticos (350ml, 650ml, 1000ml, 1800ml e "
            "2300ml) com tampa de vedação. Para guardar mantimentos, usar "
            "na geladeira, no micro-ondas ou levar marmita."
        ),
        "preco": 49.90,
        "imagem": "potes_hermeticos.jpg",
    },
    {
        "nome": "Suporte para Notebook Dobrável de Alumínio",
        "marca": "",
        "categoria": "Informática",
        "descricao": (
            "Suporte dobrável e portátil para notebook e tablet, em alumínio, "
            "com ajuste de altura e ângulo. Melhora a postura e a ventilação "
            "do aparelho."
        ),
        "preco": 35.00,
        "imagem": "suporte_notebook.jpg",
    },
    {
        "nome": "Hub USB 3.0 com 4 Portas",
        "marca": "",
        "categoria": "Informática",
        "descricao": (
            "Hub USB 3.0 com 4 portas e transmissão de até 5 Gbps. Compacto "
            "e portátil, amplia as entradas USB do notebook ou computador."
        ),
        "preco": 29.90,
        "imagem": "hub_usb.jpg",
    },
    {
        "nome": "Jarra de Vidro com Tampa de Bambu 1 Litro",
        "marca": "",
        "categoria": "Casa",
        "descricao": (
            "Jarra de vidro resistente de 1 litro com tampa de bambu e vedação. "
            "Ideal para suco, água, chá e bebidas geladas na geladeira ou na mesa."
        ),
        "preco": 47.90,
        "imagem": "jarra_vidro.jpg",
    },
    {
        "nome": "Porta Temperos Giratório com 9 Potes de Vidro",
        "marca": "",
        "categoria": "Casa",
        "descricao": (
            "Porta temperos giratório com 9 potes de vidro e tampas dosadoras. "
            "Base que gira 360° para pegar o tempero com facilidade e deixar a "
            "bancada da cozinha organizada."
        ),
        "preco": 49.90,
        "imagem": "porta_temperos.jpg",
    },
    {
        "nome": "Garrafa Térmica Inox 304 com Alça 1 Litro",
        "marca": "",
        "categoria": "Casa",
        "descricao": (
            "Garrafa térmica esportiva de aço inox 304 com capacidade de 1 litro "
            "e alça para carregar. Mantém a bebida gelada ou quente por horas, "
            "ótima para o trabalho, a academia e o dia a dia."
        ),
        "preco": 79.90,
        "imagem": "garrafa_termica.jpg",
    },
    {
        "nome": "Jogo de Chaves Catraca 46 Peças com Maleta",
        "marca": "",
        "categoria": "Ferramentas",
        "descricao": (
            "Kit com 46 peças: catraca, soquetes, extensões e chaves de vários "
            "tamanhos, tudo organizado em maleta resistente. Ótimo para reparos "
            "em casa, na oficina e no carro."
        ),
        "preco": 49.90,
        "imagem": "jogo_catraca.jpg",
    },
    {
        "nome": 'Caixa de Som Bluetooth Portátil com Luz RGB 10W',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Caixa de som Bluetooth portátil com luz RGB, alça para carregar e entradas USB e AUX. Som potente de 10W para ouvir música em casa ou levar para qualquer lugar.'
        ),
        "preco": 39.90,
        "imagem": 'som_speaker_rgb.jpg',
    },
    {
        "nome": 'Caixa de Som Bluetooth Portátil Speaker MP3',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Caixa de som Bluetooth portátil com formato cilíndrico, entrada para cartão de memória e rádio FM. Compacta, de som potente e fácil de levar.'
        ),
        "preco": 49.90,
        "imagem": 'som_speaker_mp3.jpg',
    },
    {
        "nome": 'Mini Caixinha de Som Bluetooth de Metal 3W',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Mini caixa de som Bluetooth em metal com 3W de potência. Pequena e prática, cabe no bolso e conecta fácil ao celular. Disponível em várias cores.'
        ),
        "preco": 35.00,
        "imagem": 'som_mini_metal.jpg',
    },
    {
        "nome": 'Fone de Ouvido Headphone Bluetooth P47 Sem Fio',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Headphone Bluetooth 5.0 dobrável, com som estéreo, almofadas macias e microfone embutido. Confortável para ouvir música e atender chamadas.'
        ),
        "preco": 35.00,
        "imagem": 'fone_p47.jpg',
    },
    {
        "nome": 'Fone de Ouvido Bluetooth Sem Fio E6s com Case Carregador',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Fone de ouvido Bluetooth 5.0 sem fio com case carregador e visor digital de bateria. Pequeno e prático para música, chamadas e o dia a dia.'
        ),
        "preco": 35.00,
        "imagem": 'fone_e6s.jpg',
    },
    {
        "nome": 'Cabo HDMI 4K Full HD Flat Blindado',
        "marca": "",
        "categoria": 'Áudio e Vídeo',
        "descricao": (
            'Cabo HDMI 4K de alta velocidade, tipo flat, blindado e reforçado, com conectores banhados a ouro. Liga TV, videogame, projetor e computador com imagem Full HD e 4K.'
        ),
        "preco": 29.90,
        "imagem": 'cabo_hdmi.jpg',
    },
    {
        "nome": 'Kit 13 Pincéis de Maquiagem com Bolsa',
        "marca": '',
        "categoria": 'Beleza',
        "descricao": (
            'Kit com 13 pincéis de maquiagem de cerdas macias para base, pó, contorno e olhos. Acompanha bolsa de tecido para guardar e levar na bolsa.'
        ),
        "preco": 29.90,
        "imagem": 'pinceis_13.jpg',
    },
    {
        "nome": 'Máquina de Barbear e Aparador de Pelos 3 em 1',
        "marca": 'Kemei',
        "categoria": 'Beleza',
        "descricao": (
            'Kit 3 em 1 recarregável com barbeador, aparador de cabelo e barba e aparador de pelos do nariz. Prático para o cuidado pessoal no dia a dia e para viagens.'
        ),
        "preco": 75.00,
        "imagem": 'barbeador_kemei.jpg',
    },
    {
        "nome": 'Espelho de Mesa com 16 LEDs para Maquiagem',
        "marca": '',
        "categoria": 'Beleza',
        "descricao": (
            'Espelho de mesa com 16 LEDs de luz e acionamento touch. Gira para o melhor ângulo e deixa a maquiagem bem iluminada em qualquer ambiente.'
        ),
        "preco": 49.90,
        "imagem": 'espelho_led.jpg',
    },
    {
        "nome": 'Organizador de Maquiagem Giratório 360° Acrílico',
        "marca": '',
        "categoria": 'Beleza',
        "descricao": (
            'Organizador giratório 360° em acrílico transparente, com várias divisórias para maquiagens, perfumes e cremes. Tudo à vista e ao alcance da mão na penteadeira ou no banheiro.'
        ),
        "preco": 69.90,
        "imagem": 'organizador_giratorio.jpg',
    },
    {
        "nome": 'Porta Pincel Organizador Acrílico 3 Divisórias',
        "marca": '',
        "categoria": 'Beleza',
        "descricao": (
            'Organizador de mesa em acrílico com 3 divisórias e efeito diamante. Guarda pincéis, batons e lápis de forma organizada na penteadeira, no banheiro ou no escritório.'
        ),
        "preco": 29.90,
        "imagem": 'porta_pincel.jpg',
    },
    {
        "nome": 'Kit Manicure Pedicure 12 Peças com Estojo',
        "marca": '',
        "categoria": 'Beleza',
        "descricao": (
            'Kit com cortador de unhas, alicate, tesoura, pinça e espátulas em aço inoxidável, organizado em estojo portátil. Ideal para cuidar das unhas em casa e em viagens.'
        ),
        "preco": 29.90,
        "imagem": 'kit_manicure.jpg',
    },
    {
        "nome": 'Suporte Universal de Celular para Carro com Ventosa',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Suporte veicular com base de ventosa para painel, ajustável para diversos tamanhos de celular. Ideal para GPS e aplicativos de motorista.'
        ),
        "preco": 29.90,
        "imagem": 'suporte_carro.jpg',
    },
    {
        "nome": 'Mini Aspirador de Pó Portátil Sem Fio 3 em 1',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Aspirador portátil recarregável via USB com 3 bicos, sucção de 6000Pa e filtro lavável. Ótimo para limpar o carro, o teclado e cantos difíceis da casa.'
        ),
        "preco": 47.90,
        "imagem": 'aspirador_portatil.jpg',
    },
    {
        "nome": 'Mini Compressor de Ar Portátil Digital Recarregável',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Compressor de ar portátil recarregável via USB com visor digital e vários bicos. Calibra pneus de carro, moto, bicicleta e enche bolas. Leve e fácil de guardar no carro.'
        ),
        "preco": 100.00,
        "imagem": 'compressor_portatil.jpg',
    },
    {
        "nome": 'Organizador de Banco de Carro com Bolsos',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Organizador para encosto do banco do carro com vários bolsos e divisória transparente para tablet ou celular. Mantém brinquedos, garrafas e objetos sempre à mão.'
        ),
        "preco": 35.00,
        "imagem": 'organizador_banco.jpg',
    },
    {
        "nome": 'Aromatizador de Carro Helicóptero Solar Rotativo',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Aromatizador decorativo para o painel do carro em formato de helicóptero, com hélice movida a energia solar. Acompanha essência para perfumar o ambiente.'
        ),
        "preco": 47.90,
        "imagem": 'aromatizador_solar.jpg',
    },
    {
        "nome": 'Kit de Panos de Microfibra 30x30 cm Multiuso',
        "marca": '',
        "categoria": 'Automotivo',
        "descricao": (
            'Panos de microfibra de alta absorção, macios e que não soltam fiapos. Servem para lavar e secar o carro, limpar vidros, móveis e a casa toda.'
        ),
        "preco": 29.90,
        "imagem": 'panos_microfibra.jpg',
    },
    {
        "nome": 'Kit 5 Faixas Elásticas de Exercício Mini Band',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Kit com 5 faixas elásticas de diferentes níveis de resistência para treinar em casa ou na academia. Ótimo para pernas, glúteos, braços e fisioterapia.'
        ),
        "preco": 29.90,
        "imagem": 'elasticos_mini_band.jpg',
    },
    {
        "nome": 'Corda de Pular Profissional com Rolamento 3 m',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Corda de pular de aço com rolamento para giro rápido e cabos de alumínio. Comprimento ajustável de até 3 metros. Ideal para cardio, crossfit e boxe.'
        ),
        "preco": 35.00,
        "imagem": 'corda_pular.jpg',
    },
    {
        "nome": 'Colchonete EVA 100x50 cm para Yoga, Pilates e Abdominal',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Colchonete de EVA 100 x 50 cm com 1 cm de espessura. Leve, macio e fácil de guardar, ideal para yoga, pilates, abdominais e alongamento em casa ou na academia.'
        ),
        "preco": 47.90,
        "imagem": 'colchonete_eva.jpg',
    },
    {
        "nome": 'Roda Abdominal com Apoio para Treino em Casa',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Roda abdominal com pneu antiderrapante e duas empunhaduras de espuma confortáveis. Fortalece abdômen, braços e ombros, ocupa pouco espaço e é ideal para treinar em casa.'
        ),
        "preco": 47.90,
        "imagem": 'roda_abdominal.jpg',
    },
    {
        "nome": 'Coqueteleira Shaker 600 ml para Academia',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Coqueteleira de 600 ml com tampa de rosca e bico flip, ideal para shakes, whey protein, vitaminas e suplementos. Leve, resistente e fácil de lavar.'
        ),
        "preco": 29.90,
        "imagem": 'coqueteleira.jpg',
    },
    {
        "nome": 'Bomba de Ar Manual para Bolas com Bico',
        "marca": '',
        "categoria": 'Esportes',
        "descricao": (
            'Bomba de ar manual compacta com bico agulha, ideal para encher bolas de futebol, vôlei, basquete e outros infláveis. Fácil de usar e de guardar.'
        ),
        "preco": 29.90,
        "imagem": 'bomba_ar.jpg',
    },
    {
        "nome": 'Cubo Mágico Profissional 3x3x3 Speed',
        "marca": '',
        "categoria": 'Brinquedos',
        "descricao": (
            'Cubo mágico 3x3x3 sem adesivos, com cores vivas e giro rápido e suave. Ótimo para treinar raciocínio, concentração e coordenação, para crianças e adultos.'
        ),
        "preco": 29.90,
        "imagem": 'cubo_magico.jpg',
    },
    {
        "nome": 'Kit 12 Tubos Poptube Sensorial Anti Estresse',
        "marca": '',
        "categoria": 'Brinquedos',
        "descricao": (
            'Kit com 12 tubos coloridos que esticam, dobram e voltam ao formato. Brinquedo sensorial que ajuda a relaxar, acalma a ansiedade e estimula a criatividade de crianças e adultos.'
        ),
        "preco": 35.00,
        "imagem": 'poptube.jpg',
    },
    {
        "nome": 'Blocos de Montar Coloridos 140 Peças com Caixa',
        "marca": '',
        "categoria": 'Brinquedos',
        "descricao": (
            'Kit com 140 blocos de encaixe coloridos e peças com rodinhas para montar carrinhos e construções. Estimula criatividade, coordenação motora e raciocínio. Acompanha caixa organizadora.'
        ),
        "preco": 47.90,
        "imagem": 'blocos_montar.jpg',
    },
    {
        "nome": 'Jogo 3 em 1 Xadrez, Dama e Gamão de Madeira Dobrável',
        "marca": '',
        "categoria": 'Brinquedos',
        "descricao": (
            'Tabuleiro dobrável de madeira com 3 jogos em 1: xadrez, dama e gamão. Acompanha todas as peças, fecho metálico e funciona como maleta para guardar e levar para qualquer lugar.'
        ),
        "preco": 75.00,
        "imagem": 'xadrez_3em1.jpg',
    },
    {
        "nome": 'Banqueta Dobrável Portátil até 100 kg',
        "marca": '',
        "categoria": 'Móveis',
        "descricao": (
            'Banqueta de plástico resistente que dobra e fica com apenas 2 cm de espessura. Suporta até 100 kg, pesa só 900 g e tem alça para carregar. Ótima para cozinha, banheiro, camping e pesca.'
        ),
        "preco": 35.00,
        "imagem": 'banqueta_dobravel.jpg',
    },
    {
        "nome": 'Sapateira Organizadora 4 Andares',
        "marca": '',
        "categoria": 'Móveis',
        "descricao": (
            'Sapateira de metal com 4 andares para organizar calçados e liberar espaço. Estrutura reforçada, montagem simples sem ferramentas, ideal para quarto, corredor ou entrada de casa.'
        ),
        "preco": 35.00,
        "imagem": 'sapateira_4.jpg',
    },
    {
        "nome": 'Mesa Dobrável para Notebook e Cama',
        "marca": '',
        "categoria": 'Móveis',
        "descricao": (
            'Mesa portátil dobrável com pernas retráteis e porta-copo. Perfeita para usar notebook, tablet, ler ou tomar café da manhã na cama ou no sofá. Fácil de guardar.'
        ),
        "preco": 75.00,
        "imagem": 'mesa_notebook.jpg',
    },
    {
        "nome": "Relógio Digital Esportivo à Prova d'Água 50M",
        "marca": '',
        "categoria": 'Acessórios',
        "descricao": (
            'Relógio digital esportivo com cronógrafo, alarme, calendário e luz de fundo LED. Resistente à água até 50 metros, pulseira de silicone macia e ajustável. Ótimo para o dia a dia e para treinar.'
        ),
        "preco": 47.90,
        "imagem": 'relogio_digital.jpg',
    },
    {
        "nome": 'Carteira Masculina Ultrafina Porta Cartão',
        "marca": '',
        "categoria": 'Acessórios',
        "descricao": (
            'Carteira slim de couro sintético com vários compartimentos para cartões e documentos. Fina, resistente e cabe no bolso da frente da calça. Ótima para o dia a dia.'
        ),
        "preco": 35.00,
        "imagem": 'carteira_slim.jpg',
    },
    {
        "nome": 'Chaveiro Retrátil de Aço com Mosquetão 60 cm',
        "marca": '',
        "categoria": 'Acessórios',
        "descricao": (
            'Chaveiro retrátil com cabo de aço de 60 cm e mosquetão reforçado. Prende chaves, crachá ou acessórios no cinto e puxa quando precisa. Resistente e prático para o dia a dia, trilha e trabalho.'
        ),
        "preco": 29.90,
        "imagem": 'chaveiro_retratil.jpg',
    },
    {
        "nome": 'Brinco Argola de Aço Inoxidável Dourado',
        "marca": '',
        "categoria": 'Acessórios',
        "descricao": (
            'Argolas de aço inoxidável 316L banhadas a ouro, antialérgicas e que não escurecem. Disponíveis em vários tamanhos, de 3 a 7 cm. Leves e elegantes para usar todos os dias.'
        ),
        "preco": 29.90,
        "imagem": 'brinco_argola.jpg',
    },
    {
        "nome": 'Trena Métrica 5 Metros Emborrachada com Trava',
        "marca": '',
        "categoria": 'Ferramentas',
        "descricao": (
            'Trena de aço de 5 metros com capa emborrachada resistente a impactos, trava de fita e clipe para o cinto. Ideal para obras, marcenaria, reformas e uso doméstico.'
        ),
        "preco": 29.90,
        "imagem": 'trena_5m.jpg',
    },
    {
        "nome": 'Kit Chaves de Precisão 31 em 1',
        "marca": '',
        "categoria": 'Ferramentas',
        "descricao": (
            'Kit com 31 pontas de precisão (fenda, Phillips, Torx e outras) em um cabo giratório compacto. Ideal para consertar celular, notebook, óculos, controle e pequenos eletrônicos.'
        ),
        "preco": 29.90,
        "imagem": 'kit_precisao_31.jpg',
    },
    {
        "nome": 'Alicate Universal 8 Polegadas com Cabo Isolado',
        "marca": '',
        "categoria": 'Ferramentas',
        "descricao": (
            'Alicate universal de 8 polegadas em aço forjado, com cabos emborrachados antiderrapantes. Corta, dobra e segura fios e peças. Indispensável na caixa de ferramentas de casa ou oficina.'
        ),
        "preco": 29.90,
        "imagem": 'alicate_universal.jpg',
    },
    {
        "nome": 'Kit 3 Camisetas Masculinas 100% Algodão',
        "marca": '',
        "categoria": 'Roupas',
        "descricao": (
            'Kit com 3 camisetas masculinas de algodão, gola redonda e modelagem confortável, com estampa minimalista. Tecido macio e respirável para o dia a dia. Tamanhos P, M, G e GG.'
        ),
        "preco": 100.00,
        "imagem": 'kit_camisetas.jpg',
    },
    {
        "nome": 'Calça Legging Suplex Fitness Feminina',
        "marca": '',
        "categoria": 'Roupas',
        "descricao": (
            'Legging de suplex com cintura alta, tecido grosso que não marca nem fica transparente. Confortável para academia, caminhada e dia a dia. Vários tamanhos (P ao GG) e cores.'
        ),
        "preco": 35.00,
        "imagem": 'legging_suplex.jpg',
    },
    {
        "nome": 'Chinelo Slide Nuvem Unissex',
        "marca": '',
        "categoria": 'Calçados',
        "descricao": (
            'Chinelo slide de EVA super macio e leve, com sola antiderrapante e palmilha anatômica. Confortável para casa, praia, piscina e dia a dia. Tamanhos do 34 ao 45.'
        ),
        "preco": 47.90,
        "imagem": 'chinelo_slide.jpg',
    },
    {
        "nome": 'Mochila Executiva Impermeável para Notebook 15,6"',
        "marca": '',
        "categoria": 'Bolsas',
        "descricao": (
            'Mochila reforçada e impermeável com compartimento acolchoado para notebook de até 15,6", bolso lateral para garrafa, alça de mão e zíperes resistentes. Ótima para trabalho, faculdade e viagem.'
        ),
        "preco": 49.90,
        "imagem": 'mochila_executiva.jpg',
    },
    {
        "nome": 'Conjunto Bebê Menina 3 Peças em Algodão',
        "marca": '',
        "categoria": 'Infantil',
        "descricao": (
            'Kit com 3 peças para bebê: body manga longa, body manga curta e calça, em algodão macio e confortável. Ótimo para o enxoval. Tamanhos RN, P, M, G e GG.'
        ),
        "preco": 75.00,
        "imagem": 'conjunto_bebe.jpg',
    },
    {
        "nome": 'Bermuda Moletom Masculina',
        "marca": '',
        "categoria": 'Roupas',
        "descricao": (
            'Bermuda de moletom macio com cordão e bolsos laterais, ideal para academia, caminhada e uso casual. Modelagem confortável. Tamanhos P ao GG.'
        ),
        "preco": 47.90,
        "imagem": 'bermuda_moletom.jpg',
    },
    {
        "nome": 'Kit 6 Pares de Meia Cano Médio Unissex',
        "marca": '',
        "categoria": 'Roupas',
        "descricao": (
            'Kit com 6 pares de meia de algodão, cano médio, nas cores branca, preta e cinza. Macias, com boa elasticidade e confortáveis para o dia a dia e para treinar. Servem para homens e mulheres.'
        ),
        "preco": 29.90,
        "imagem": 'kit_meias.jpg',
    },
    {
        "nome": 'Vestido Midi Canelado Tomara Que Caia com Fenda',
        "marca": '',
        "categoria": 'Roupas',
        "descricao": (
            'Vestido midi em malha canelada com modelagem ajustada, tomara que caia e fenda lateral. Elegante e confortável, ótimo para passeios e festas. Tamanhos P ao GG.'
        ),
        "preco": 35.00,
        "imagem": 'vestido_canelado.jpg',
    },
    {
        "nome": 'Tênis Casual Branco Masculino',
        "marca": '',
        "categoria": 'Calçados',
        "descricao": (
            'Tênis casual branco com solado macio e leve, cabedal em material sintético e cadarço. Combina com qualquer look e é confortável para usar o dia inteiro. Numeração 37 ao 46.'
        ),
        "preco": 90.00,
        "imagem": 'tenis_branco.jpg',
    },
    {
        "nome": 'Sandália Rasteirinha Feminina Preta',
        "marca": '',
        "categoria": 'Calçados',
        "descricao": (
            'Sandália rasteira feminina preta com fivela dourada e detalhes vazados. Leve, macia e confortável para o dia a dia. Numeração 34 ao 40.'
        ),
        "preco": 47.90,
        "imagem": 'sandalia_preta.jpg',
    },
    {
        "nome": 'Tênis de Corrida Esportivo Solado Macio',
        "marca": '',
        "categoria": 'Calçados',
        "descricao": (
            'Tênis esportivo para corrida e caminhada, com cabedal em malha respirável e solado alto com amortecimento macio. Leve, confortável e com ótima aderência. Numeração 35 ao 46.'
        ),
        "preco": 120.00,
        "imagem": 'tenis_corrida.jpg',
    },
    {
        "nome": 'Bolsa Feminina Transversal Multifuncional',
        "marca": '',
        "categoria": 'Bolsas',
        "descricao": (
            'Bolsa transversal feminina em tecido leve e resistente, com vários bolsos e compartimentos para organizar celular, carteira e documentos. Alça ajustável e pompom removível.'
        ),
        "preco": 59.90,
        "imagem": 'bolsa_transversal.jpg',
    },
    {
        "nome": 'Bolsa de Viagem Sport Impermeável 30L',
        "marca": '',
        "categoria": 'Bolsas',
        "descricao": (
            'Bolsa de viagem esportiva em tecido impermeável, capacidade de 30 litros, com compartimento inferior para tênis ou roupa molhada, alça de mão e alça transversal removível. Ótima para academia e fim de semana.'
        ),
        "preco": 80.00,
        "imagem": 'bolsa_viagem.jpg',
    },
]


# =========================================================
# PRODUTOS DE EXEMPLO
# True  = mostra os produtos de exemplo (selo "Exemplo")
# False = mostra só os seus produtos reais
# Antes de colocar a loja no ar, troque para False.
# =========================================================
MOSTRAR_EXEMPLOS = False


# LISTA FINAL QUE O SITE USA (reais + exemplos, se estiverem ligados)
def produtos_da_loja():
    if MOSTRAR_EXEMPLOS:
        return PRODUTOS + EXEMPLOS
    return PRODUTOS


# Tira acentos e maiúsculas, para a busca achar "eletronicos" = "Eletrônicos"
def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto.casefold().strip()


# TRANSFORMA 35.0 EM "R$ 35,00" (usado nos templates: {{ preco | brl }})
@app.template_filter("brl")
def formatar_real(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


# PÁGINA INICIAL (mostra 4 produtos sorteados; mudam a cada visita)
@app.route("/")
def inicio():
    todos = produtos_da_loja()
    destaque = random.sample(todos, min(4, len(todos)))
    return render_template("index.html", produtos=destaque)


# PÁGINA DE PRODUTOS
# Aceita  /produtos?categoria=Casa  e  /produtos?busca=fone
@app.route("/produtos")
def produtos():
    categoria = request.args.get("categoria", "").strip()
    busca = request.args.get("busca", "").strip()

    lista = produtos_da_loja()

    if categoria:
        lista = [p for p in lista if normalizar(p["categoria"]) == normalizar(categoria)]

    if busca:
        termo = normalizar(busca)
        lista = [
            p for p in lista
            if termo in normalizar(" ".join([p["nome"], p["marca"], p["categoria"], p["descricao"]]))
        ]

    return render_template(
        "produtos.html",
        produtos=lista,
        categoria=categoria,
        busca=busca,
        categorias=CATEGORIAS,
    )


# PÁGINA SOBRE NÓS
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# PÁGINA DE CONTATO
@app.route("/contato")
def contato():
    return render_template("contato.html")


# PÁGINA 404 (endereço que não existe)
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("404.html"), 404


# EXECUÇÃO DO SERVIDOR (no seu computador)
# O modo "debug" só liga se você pedir. Na internet ele fica DESLIGADO,
# porque mostra detalhes do código para qualquer visitante.
# Para ligar no seu PC: no PowerShell, rode  $env:FLASK_DEBUG="1"  e depois  python app.py
if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
