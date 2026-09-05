/* =========================
   CARRINHO
========================= */

const cartCounter =
    document.querySelector('.contador-carrinho');

let cartItems = 0;


/* =========================
   BUSCA DE PRODUTOS
========================= */

const campoBusca =
    document.querySelector('#campoBusca');

const produtos =
    document.querySelectorAll('.card-produto');


if (campoBusca) {

    campoBusca.addEventListener(
        'input',
        function () {

            const textoBusca =
                this.value
                    .toLowerCase()
                    .trim();


            produtos.forEach(
                function (produto) {

                    const textoProduto =
                        produto.textContent
                            .toLowerCase();


                    const encontrou =
                        textoProduto.includes(
                            textoBusca
                        );


                    produto.style.display =
                        encontrou ? '' : 'none';

                }
            );

        }
    );

}


/* =========================
   VER TODAS AS CATEGORIAS
========================= */

const verTodas =
    document.querySelector('#verTodas');

const categorias =
    document.querySelector('.Categorias');


if (verTodas && categorias) {

    verTodas.addEventListener(
        'click',
        function (event) {

            event.preventDefault();


            categorias.classList.toggle(
                'categorias-expandida'
            );


            if (
                categorias.classList.contains(
                    'categorias-expandida'
                )
            ) {

                verTodas.textContent =
                    'Mostrar menos ↑';

            } else {

                verTodas.textContent =
                    'Ver todas →';

            }

        }
    );

}


/* =========================
   BOTÕES DE COMPRAR
========================= */

document
    .querySelectorAll(
        '.botao-comprar, .botao-oferta'
    )
    .forEach(function (button) {

        button.addEventListener(
            'click',
            function () {

                cartItems += 1;


                if (cartCounter) {

                    cartCounter.textContent =
                        cartItems;

                }


                const previousText =
                    this.textContent;


                this.textContent =
                    'Adicionado';


                this.disabled = true;


                setTimeout(function () {

                    button.textContent =
                        previousText;

                    button.disabled =
                        false;

                }, 900);

            }
        );

    });


/* =========================
   NEWSLETTER
========================= */

const newsletterForm =
    document.querySelector(
        '.newsletter-form'
    );


if (newsletterForm) {

    newsletterForm.addEventListener(
        'submit',
        function (event) {

            event.preventDefault();


            const button =
                this.querySelector(
                    '.botao-newsletter'
                );

            const input =
                this.querySelector(
                    'input'
                );


            if (button) {

                button.textContent =
                    'Cadastrado!';

                button.disabled =
                    true;

            }


            if (input) {

                input.value = '';

            }


            setTimeout(function () {

                if (button) {

                    button.textContent =
                        'Quero receber';

                    button.disabled =
                        false;

                }

            }, 1200);

        }
    );

}
