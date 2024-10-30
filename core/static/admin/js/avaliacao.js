document.addEventListener('DOMContentLoaded', function() {
    const strelas = document.querySelectorAll('.strela');
    const textoDeAvaliacao = document.getElementById('texto-de-avaliacao');
    let avaliacao = 0; // 
    // Adiciona evento de clique nas estrelas
    strelas.forEach(strela => {
        strela.addEventListener('click', function() {
            avaliacao = this.getAttribute('data-value'); 
            atualizarEstrelas(avaliacao); 
            textoDeAvaliacao.textContent = `Você avaliou com ${avaliacao} estrela(s).`;
        });
    });

    function atualizarEstrelas(valor) {
       
        strelas.forEach(strela => {
            strela.classList.remove('selected');
            if (strela.getAttribute('data-value') <= valor) {
                strela.classList.add('selected');
            }
        });
    }

  
    const botaoEnviar = document.getElementById('enviarcomentario');
    botaoEnviar.addEventListener('click', function() {
        const comentarioTexto = document.getElementById('armazenar-comentario').value;

        if (avaliacao === 0) {
            alert("Por favor, escolha uma avaliação com estrelas.");
            return;
        }

        if (comentarioTexto.trim() === "") {
            alert("Por favor, escreva um comentário.");
            return;
        }

        adicionarComentario(avaliacao, comentarioTexto);

        
        document.getElementById('armazenar-comentario').value = "";
        atualizarEstrelas(0); 
        textoDeAvaliacao.textContent = ""; 
    });

    function adicionarComentario(avaliacao, comentario) {
        const comentariosList = document.getElementById('comentarios-list');

        const novoComentario = document.createElement('div');
        novoComentario.classList.add('comentario');
        novoComentario.innerHTML = `
            <p><strong>Avaliação:</strong> ${avaliacao} estrela(s)</p>
            <p><strong>Comentário:</strong> ${comentario}</p>
        `;

        comentariosList.appendChild(novoComentario); 
    }
});