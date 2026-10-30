console.log("Bueno TEC - JavaScript funcionando!");


// ======================================================
// ELEMENTOS DO HTML
// ======================================================

const contadorCarrinho =
    document.querySelector('.contador-carrinho');

const carrinhoTotal =
    document.querySelector('#carrinhoTotal');

const carrinhoItens =
    document.querySelector('#carrinhoItens');

const botaoCarrinho =
    document.querySelector('#botaoCarrinho');

const carrinhoMenu =
    document.querySelector('#carrinhoMenu');

const botaoFinalizar =
    document.querySelector('#botaoFinalizar');

const campoBusca =
    document.querySelector('#campoBusca');

const botoesAdicionar =
    document.querySelectorAll('.botao-adicionar');

const botoesOferta =
    document.querySelectorAll('.botao-oferta');


// ======================================================
// CARRINHO
// ======================================================

let carrinho = [];


// ======================================================
// FORMATAR PREÇO
// ======================================================

function formatarPreco(preco) {

    return preco.toLocaleString('pt-BR', {

        minimumFractionDigits: 2,

        maximumFractionDigits: 2

    });

}


// ======================================================
// CALCULAR QUANTIDADE TOTAL
// ======================================================

function calcularQuantidadeTotal() {

    return carrinho.reduce(function (total, item) {

        return total + item.quantidade;

    }, 0);

}


// ======================================================
// CALCULAR VALOR TOTAL
// ======================================================

function calcularTotal() {

    return carrinho.reduce(function (total, item) {

        return total + (
            item.preco * item.quantidade
        );

    }, 0);

}


// ======================================================
// ATUALIZAR RESUMO DO CARRINHO
// ======================================================

function atualizarResumo() {

    const quantidadeTotal =
        calcularQuantidadeTotal();

    const valorTotal =
        calcularTotal();


    contadorCarrinho.textContent =
        quantidadeTotal;


    carrinhoTotal.textContent =
        formatarPreco(valorTotal);

}


// ======================================================
// MOSTRAR CARRINHO VAZIO
// ======================================================

function mostrarCarrinhoVazio() {

    carrinhoItens.innerHTML = `

        <p>
            Seu carrinho está vazio.
        </p>

    `;

}


// ======================================================
// RENDERIZAR CARRINHO
// ======================================================

function renderizarCarrinho() {

    carrinhoItens.innerHTML = '';


    // ----------------------------------------------
    // CARRINHO VAZIO
    // ----------------------------------------------

    if (carrinho.length === 0) {

        mostrarCarrinhoVazio();

        atualizarResumo();

        return;

    }


    // ----------------------------------------------
    // CRIAR OS PRODUTOS
    // ----------------------------------------------

    carrinho.forEach(function (item) {


        const itemCarrinho =
            document.createElement('div');


        itemCarrinho.className =
            'item-carrinho';


        const subtotal =
            item.preco * item.quantidade;


        itemCarrinho.innerHTML = `

            <p class="nome-produto-carrinho">
                ${item.nome}
            </p>


            <p class="quantidade-produto-carrinho">
                Quantidade:
                ${item.quantidade}
            </p>


            <div class="controles-quantidade">

                <button
                    type="button"
                    class="diminuir-quantidade"
                    data-nome="${item.nome}">
                    -
                </button>


                <span>
                    ${item.quantidade}
                </span>


                <button
                    type="button"
                    class="aumentar-quantidade"
                    data-nome="${item.nome}">
                    +
                </button>

            </div>


            <p class="preco-unitario-carrinho">
                Preço:
                R$ ${formatarPreco(item.preco)}
            </p>


            <p class="subtotal-carrinho">
                Subtotal:
                R$ ${formatarPreco(subtotal)}
            </p>


            <button
                type="button"
                class="remover-produto"
                data-nome="${item.nome}">

                Remover

            </button>

        `;


        carrinhoItens.appendChild(itemCarrinho);

    });


    atualizarResumo();

}


// ======================================================
// ADICIONAR PRODUTO
// ======================================================

function adicionarProduto(nome, preco) {


    const produtoExistente =
        carrinho.find(function (item) {

            return item.nome === nome;

        });


    // ----------------------------------------------
    // PRODUTO JÁ EXISTE
    // ----------------------------------------------

    if (produtoExistente) {

        produtoExistente.quantidade++;

    }


    // ----------------------------------------------
    // PRODUTO NOVO
    // ----------------------------------------------

    else {

        carrinho.push({

            nome: nome,

            preco: preco,

            quantidade: 1

        });

    }


    renderizarCarrinho();


    console.log(
        "Carrinho atualizado:",
        carrinho
    );

}


// ======================================================
// AUMENTAR QUANTIDADE
// ======================================================

function aumentarQuantidade(nomeProduto) {


    const produto =
        carrinho.find(function (item) {

            return item.nome === nomeProduto;

        });


    if (!produto) {

        return;

    }


    produto.quantidade++;


    renderizarCarrinho();

}


// ======================================================
// DIMINUIR QUANTIDADE
// ======================================================

function diminuirQuantidade(nomeProduto) {


    const produto =
        carrinho.find(function (item) {

            return item.nome === nomeProduto;

        });


    if (!produto) {

        return;

    }


    produto.quantidade--;


    // ----------------------------------------------
    // SE CHEGAR A ZERO, REMOVE O PRODUTO
    // ----------------------------------------------

    if (produto.quantidade <= 0) {

        removerProduto(nomeProduto);

        return;

    }


    renderizarCarrinho();

}


// ======================================================
// REMOVER PRODUTO
// ======================================================

function removerProduto(nomeProduto) {


    carrinho =
        carrinho.filter(function (item) {

            return item.nome !== nomeProduto;

        });


    renderizarCarrinho();


    console.log(
        "Produto removido:",
        nomeProduto
    );

}


// ======================================================
// LIMPAR CARRINHO
// ======================================================

function limparCarrinho() {

    carrinho = [];


    renderizarCarrinho();


    console.log(
        "Carrinho limpo."
    );

}


// ======================================================
// BOTÕES "ADICIONAR AO CARRINHO"
// ======================================================

botoesAdicionar.forEach(function (botao) {


    botao.addEventListener(
        'click',
        function () {


            const cardProduto =
                botao.closest('.card-produto');


            if (!cardProduto) {

                return;

            }


            const nomeElemento =
                cardProduto.querySelector('h3');


            const precoElemento =
                cardProduto.querySelector(
                    '.preco-produto'
                );


            if (
                !nomeElemento ||
                !precoElemento
            ) {

                console.error(
                    "Nome ou preço não encontrado."
                );

                return;

            }


            const nome =
                nomeElemento.textContent.trim();


            const precoTexto =
                precoElemento.textContent.trim();


            const preco =
                Number(
                    precoTexto
                        .replace('R$', '')
                        .replace(/\./g, '')
                        .replace(',', '.')
                        .trim()
                );


            if (isNaN(preco)) {

                console.error(
                    "Preço inválido:",
                    precoTexto
                );

                return;

            }


            adicionarProduto(
                nome,
                preco
            );

        }
    );

});


// ======================================================
// BOTÕES "COMPRAR AGORA" DAS OFERTAS
// ======================================================

botoesOferta.forEach(function (botao) {


    botao.addEventListener(
        'click',
        function () {


            const cardOferta =
                botao.closest('.card-oferta');


            if (!cardOferta) {

                return;

            }


            const nomeElemento =
                cardOferta.querySelector('h3');


            const precoElemento =
                cardOferta.querySelector(
                    '.preco-oferta'
                );


            if (
                !nomeElemento ||
                !precoElemento
            ) {

                console.error(
                    "Nome ou preço da oferta não encontrado."
                );

                return;

            }


            const nome =
                nomeElemento.textContent.trim();


            const precoTexto =
                precoElemento.textContent.trim();


            const preco =
                Number(
                    precoTexto
                        .replace('R$', '')
                        .replace(/\./g, '')
                        .replace(',', '.')
                        .trim()
                );


            if (isNaN(preco)) {

                console.error(
                    "Preço da oferta inválido:",
                    precoTexto
                );

                return;

            }


            adicionarProduto(
                nome,
                preco
            );


            // Abrir o carrinho automaticamente
            carrinhoMenu.classList.add('ativo');

        }
    );

});


// ======================================================
// BOTÕES INTERNOS DO CARRINHO
// ======================================================

carrinhoItens.addEventListener(
    'click',
    function (evento) {


        const botao =
            evento.target.closest('button');


        if (!botao) {

            return;

        }


        const nomeProduto =
            botao.dataset.nome;


        if (!nomeProduto) {

            return;

        }


        // ----------------------------------------------
        // BOTÃO +
        // ----------------------------------------------

        if (
            botao.classList.contains(
                'aumentar-quantidade'
            )
        ) {

            aumentarQuantidade(
                nomeProduto
            );

        }


        // ----------------------------------------------
        // BOTÃO -
        // ----------------------------------------------

        if (
            botao.classList.contains(
                'diminuir-quantidade'
            )
        ) {

            diminuirQuantidade(
                nomeProduto
            );

        }


        // ----------------------------------------------
        // BOTÃO REMOVER
        // ----------------------------------------------

        if (
            botao.classList.contains(
                'remover-produto'
            )
        ) {

            removerProduto(
                nomeProduto
            );

        }

    }
);


// ======================================================
// ABRIR / FECHAR CARRINHO
// ======================================================

if (
    botaoCarrinho &&
    carrinhoMenu
) {

    botaoCarrinho.addEventListener(
        'click',
        function () {

            carrinhoMenu.classList.toggle(
                'ativo'
            );

        }
    );

}


// ======================================================
// FINALIZAR COMPRA
// ======================================================

if (botaoFinalizar) {

    botaoFinalizar.addEventListener(
        'click',
        function () {


            if (carrinho.length === 0) {

                alert(
                    'Seu carrinho está vazio.'
                );

                return;

            }


            const total =
                calcularTotal();


            alert(
                'Compra iniciada! Total: R$ ' +
                formatarPreco(total)
            );


            console.log(
                'Pedido:',
                carrinho
            );

        }
    );

}


// ======================================================
// BUSCA DE PRODUTOS
// ======================================================

const formularioBusca =
    document.querySelector('.busca-container');


if (formularioBusca) {

    formularioBusca.addEventListener(
        'submit',
        function (evento) {


            evento.preventDefault();


            const termo =
                campoBusca.value
                    .trim()
                    .toLowerCase();


            if (!termo) {

                return;

            }


            const produtos =
                document.querySelectorAll(
                    '.card-produto'
                );


            produtos.forEach(function (produto) {


                const nome =
                    produto
                        .querySelector('h3')
                        .textContent
                        .toLowerCase();


                if (
                    nome.includes(termo)
                ) {

                    produto.style.display =
                        '';

                }

                else {

                    produto.style.display =
                        'none';

                }

            });

        }
    );

}


// ======================================================
// ESTADO INICIAL
// ======================================================

renderizarCarrinho();


console.log(
    "Sistema de carrinho carregado com sucesso."
);