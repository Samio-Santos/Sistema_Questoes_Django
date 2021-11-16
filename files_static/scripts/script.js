/* Quando o usuário clica no botão,
alternar entre ocultar e mostrar o conteúdo suspenso  */
function myfilter() {
  filter = document.getElementById("myfilter").classList.toggle("show");
  iconeSeta = document.querySelector(".seta");

  if (filter === true) {
    iconeSeta.src = "/static/img/seta-suspensa-cima.png";
  } else {
    iconeSeta.src = "/static/img/seta-suspensa.png";
  }
}

window.onclick = function (e) {
  if (!e.target.matches(".filter")) {
    var dropdowns = document.getElementsByClassName("dropdown-filter");
    for (var d = 0; d < dropdowns.length; d++) {
      var openDropdown = dropdowns[d];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

function mostraSenha() {
  var senha = document.getElementById("password");
  var iconSenha = document.getElementById("hide");

  if (senha.type === "password") {
    senha.type = "text";
    iconSenha.src = "/static/img/mostrar.png";
  } else {
    senha.type = "password";
    iconSenha.src = "/static/img/escondido.png";
  }
}

// Validador de senha no cadastro

var myInput = document.getElementById("id_new_password1");
var rsenha = document.getElementById("id_new_password2");

var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var repeat_password = document.getElementById("repeat-password");

if (myInput) {
  // Quando o usuário clica no campo de senha, mostra a caixa de mensagem
  // myInput.onfocus = function() {
  //   document.getElementById("Valid-password").style.display = "block";
  // }

  // Quando o usuário clicar fora do campo de senha, oculte a caixa de mensagem
  // myInput.onblur = function() {
  //   document.getElementById("Valid-password").style.display = "none";
  // }

  // Função execulta dentro do CADASTRO.
  // Quando o usuário começa a digitar algo dentro dos campos de senha e repetir senhas

  rsenha.onkeyup = function () {
    if (myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
  };

  myInput.onkeyup = function () {
    // Validar letra minúsculas
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
      letter.classList.remove("invalid");
      letter.classList.add("valid");
    } else {
      letter.classList.remove("valid");
      letter.classList.add("invalid");
    }

    // Valida letras maiúsculas
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
      capital.classList.remove("invalid");
      capital.classList.add("valid");
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
    }

    // Valida numeros
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
      number.classList.remove("invalid");
      number.classList.add("valid");
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
    }

    // Valida o comprimento
    if (myInput.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
    }

    // Verica se as senhas são iguais
    if (myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
    rsenha;
  };
}

function openNav() {
  document.getElementById("mySidepanel").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  document.body.style.transition = "1s";
  document.body.style.overflow = "hidden";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
  document.body.style.backgroundColor = "whitesmoke";
  document.body.style.overflow = "visible";
}

// Função para habilitar o botão caso o usuario preencha todo o formulario
function enableButton(id_pergunta) {
  document.querySelector(`.button${id_pergunta}`).removeAttribute("disabled");
  document.querySelector(`.button${id_pergunta}`).style.cursor = "pointer";
}

// Na pasta template/PERGUNTAS_TEMPLATES/index.html
// Se a pergunta tiver respondida, então trecho de codigo abaixo impede que o usuário responda a questão novamente
document.querySelectorAll("#id_pergunta").forEach((id_pergunta) => {
  id = id_pergunta.value;
  questoes_respondidas = document.getElementById(`id_resposta${id}`);
  banca = document.getElementById(`banca${id}`);

  if (questoes_respondidas == null) {
    //pass
  } else {
    if (questoes_respondidas.value == "True" && banca.value == "Cespe") {
      certo = document.querySelector(`#certo${id}`);
      errado = document.querySelector(`#errado${id}`);

      resposta_usuario = document.querySelector(`#resposta_usuario${id}`);
      if (resposta_usuario.value == "Certo") {
        certo.checked = true;
        errado.disabled = true;
      } else if (resposta_usuario.value == "Errado") {
        errado.checked = true;
        certo.disabled = true;
      }
    }

    if (questoes_respondidas.value == "True" && banca.value == "Vunesp") {
      a = document.querySelector(`#A${id}`);
      b = document.querySelector(`#B${id}`);
      c = document.querySelector(`#C${id}`);
      d = document.querySelector(`#D${id}`);
      e = document.querySelector(`#E${id}`);
      resposta_usuario = document.querySelector(`#resposta_usuario${id}`);
      if (resposta_usuario.value == "A") {
        a.checked = true;
        b.disabled = true;
        c.disabled = true;
        d.disabled = true;
        e.disabled = true;
      } else if (resposta_usuario.value == "B") {
        a.disabled = true;
        b.checked = true;
        c.disabled = true;
        d.disabled = true;
        e.disabled = true;
      } else if (resposta_usuario.value == "C") {
        a.disabled = true;
        b.disabled = true;
        c.checked = true;
        d.disabled = true;
        e.disabled = true;
      } else if (resposta_usuario.value == "D") {
        a.disabled = true;
        b.disabled = true;
        c.disabled = true;
        d.checked = true;
        e.disabled = true;
      } else if (resposta_usuario.value == "E") {
        a.disabled = true;
        b.disabled = true;
        c.disabled = true;
        d.disabled = true;
        e.checked = true;
      }
    }
  }
});

// Funciobalidade com Ajax e Django
// Quando o usuario responder uma questão este código irá excultar
function resp_ajax(id_pergunta) {
  if (document.querySelector(`#question-form${id_pergunta}`)) {
    let form = document.querySelector(`#question-form${id_pergunta}`);
    function sendForm(event) {
      event.preventDefault();
      let data = new FormData(form);
      let ajax = new XMLHttpRequest();
      let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
      ajax.open("POST", form.action);
      ajax.setRequestHeader("X-CSRF-TOKEN", token);
      ajax.onreadystatechange = function () {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let alternativa_correta = document.querySelector(
            `#alternativas_correta${id_pergunta}`
          ).value;
          var mensagem = document.querySelector(`.mensagem${id_pergunta}`);
          banca = document.getElementById(`banca${id_pergunta}`);

          document.getElementsByName("resp").forEach((radio) => {
            if (radio.checked && banca.value == "Cespe") {
              if (radio.value == alternativa_correta) {
                mensagem.innerHTML = `
                  <div class="sk-circle">
                    <div class="sk-circle1 sk-child"></div>
                    <div class="sk-circle2 sk-child"></div>
                    <div class="sk-circle3 sk-child"></div>
                    <div class="sk-circle4 sk-child"></div>
                    <div class="sk-circle5 sk-child"></div>
                    <div class="sk-circle6 sk-child"></div>
                    <div class="sk-circle7 sk-child"></div>
                    <div class="sk-circle8 sk-child"></div>
                    <div class="sk-circle9 sk-child"></div>
                    <div class="sk-circle10 sk-child"></div>
                    <div class="sk-circle11 sk-child"></div>
                    <div class="sk-circle12 sk-child"></div>
                  </div>
                `;

                setTimeout(function () {
                  mensagem.innerHTML = `
                    <img src="/static/img/verificacao-verde.png" alt="Resposta-correta" />
                    <span class="right">Parabéns! Você acertou!</span>`;
                }, 1000);

                document.querySelector(`.button${id_pergunta}`).disabled = true;
                document.querySelector(`#certo${id_pergunta}`).disabled = true;
                document.querySelector(`#errado${id_pergunta}`).disabled = true;
              } else {
                mensagem.innerHTML = `
                  <div class="sk-circle">
                    <div class="sk-circle1 sk-child"></div>
                    <div class="sk-circle2 sk-child"></div>
                    <div class="sk-circle3 sk-child"></div>
                    <div class="sk-circle4 sk-child"></div>
                    <div class="sk-circle5 sk-child"></div>
                    <div class="sk-circle6 sk-child"></div>
                    <div class="sk-circle7 sk-child"></div>
                    <div class="sk-circle8 sk-child"></div>
                    <div class="sk-circle9 sk-child"></div>
                    <div class="sk-circle10 sk-child"></div>
                    <div class="sk-circle11 sk-child"></div>
                    <div class="sk-circle12 sk-child"></div>
                  </div>
                `;
                setTimeout(function () {
                  mensagem.innerHTML = `
                    <img src="/static/img/verificacao-vermelho.png" alt="Resposta-correta" />
                    <span class="error">Você errou! <b>Resposta: ${alternativa_correta}</b></span>`;
                }, 1000);

                document.querySelector(`.button${id_pergunta}`).disabled = true;
                document.querySelector(`#certo${id_pergunta}`).disabled = true;
                document.querySelector(`#errado${id_pergunta}`).disabled = true;
              }
            } else if (radio.checked && banca.value == "Vunesp") {
              if (radio.value == alternativa_correta) {
                mensagem.innerHTML = `
                  <div class="sk-circle">
                    <div class="sk-circle1 sk-child"></div>
                    <div class="sk-circle2 sk-child"></div>
                    <div class="sk-circle3 sk-child"></div>
                    <div class="sk-circle4 sk-child"></div>
                    <div class="sk-circle5 sk-child"></div>
                    <div class="sk-circle6 sk-child"></div>
                    <div class="sk-circle7 sk-child"></div>
                    <div class="sk-circle8 sk-child"></div>
                    <div class="sk-circle9 sk-child"></div>
                    <div class="sk-circle10 sk-child"></div>
                    <div class="sk-circle11 sk-child"></div>
                    <div class="sk-circle12 sk-child"></div>
                  </div>
                `;
                setTimeout(function () {
                  mensagem.innerHTML = `
                    <img src="/static/img/verificacao-verde.png" alt="Resposta-correta" />
                    <span class="right">Parabéns! Você acertou!</span>`;
                }, 1000);

                document.querySelector(`.button${id_pergunta}`).disabled = true;
                document.querySelector(`#A${id_pergunta}`).disabled = true;
                document.querySelector(`#B${id_pergunta}`).disabled = true;
                document.querySelector(`#C${id_pergunta}`).disabled = true;
                document.querySelector(`#D${id_pergunta}`).disabled = true;
                document.querySelector(`#E${id_pergunta}`).disabled = true;
              } else {
                mensagem.innerHTML = `
                  <div class="sk-circle">
                    <div class="sk-circle1 sk-child"></div>
                    <div class="sk-circle2 sk-child"></div>
                    <div class="sk-circle3 sk-child"></div>
                    <div class="sk-circle4 sk-child"></div>
                    <div class="sk-circle5 sk-child"></div>
                    <div class="sk-circle6 sk-child"></div>
                    <div class="sk-circle7 sk-child"></div>
                    <div class="sk-circle8 sk-child"></div>
                    <div class="sk-circle9 sk-child"></div>
                    <div class="sk-circle10 sk-child"></div>
                    <div class="sk-circle11 sk-child"></div>
                    <div class="sk-circle12 sk-child"></div>
                  </div>
                `;
                setTimeout(function () {
                  mensagem.innerHTML = `
                    <img src="/static/img/verificacao-vermelho.png" alt="Resposta-correta" />
                    <span class="error">Você errou! <b>Resposta: ${alternativa_correta}</b></span>`;
                }, 1000);

                document.querySelector(`.button${id_pergunta}`).disabled = true;
                document.querySelector(`#A${id_pergunta}`).disabled = true;
                document.querySelector(`#B${id_pergunta}`).disabled = true;
                document.querySelector(`#C${id_pergunta}`).disabled = true;
                document.querySelector(`#D${id_pergunta}`).disabled = true;
                document.querySelector(`#E${id_pergunta}`).disabled = true;
              }
            }
          });
        }
      };
      ajax.send(data);
    }
    form.addEventListener("submit", sendForm, false);
  }
}

// Função para pesquisar uma matéria no dashboard
function filterFunction() {
  var input, filter, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("box-container");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;

    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
      a.innerText = "Samy";
    } else {
      a[i].style.display = "none";
    }
  }
}

// Codigo para pre-loader no Dashboard
if (document.querySelector(".spinner")) {
  var loader = setInterval(function () {
    clearInterval(loader);
    document.querySelector(".spinner").style.display = "none";
    document.querySelector(".secao").style.display = "inherit";
    document.querySelector(".aside").style.display = "inherit";
    document.querySelector(".footer").style.display = "inherit";
  }, 3000);
}

// Codigo para pre-loader nas perguntas
if (document.querySelector(".sk-circle")) {
  var loader = setInterval(function () {
    clearInterval(loader);
    document.querySelector(".sk-circle").style.display = "none";
  }, 800);
}

// Quando o usuário clicar em qualquer lugar fora do modal, feche-o
var modal = document.getElementById("id01");
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Script para o botão "zera questões resolvidas"
// Enquanto o usuario não digitar a frase corretamente o botão para deletar ficará desabilitado
frase = document.getElementById("frase");
if (frase) {
  frase.onkeyup = function () {
    if (frase.value === "Desejo zerar minhas estatísticas") {
      document.querySelector(".deletebtn").disabled = false;
    } else {
      document.querySelector(".deletebtn").disabled = true;
    }
  };
}

function mostratexto(text, vertext) {
  var container = document.getElementById(text);
  var vertext = document.getElementById(vertext);

  if (container.style.display === "none") {
    container.style.display = "block";
    vertext.textContent = "Texto associado -";
  } else {
    container.style.display = "none";
    vertext.textContent = "Texto associado +";
  }
}

// Script para pré-visualizar a foto de perfil antes de salvar
if (document.querySelector(".img-perfil") && document.getElementById("file")) {
  foto_perfil = document.querySelector(".img-perfil");
  file = document.getElementById("file");

  file.addEventListener("change", () => {
    if (file.files.length <= 0) {
      return;
    }

    let reader = new FileReader();

    reader.onload = () => {
      foto_perfil.src = reader.result;
    };

    reader.readAsDataURL(file.files[0]);
  });
}

if (document.querySelector(".alert-errorinput")) {
  input_username = document.querySelector("#username").style.borderBottom =
    "1px solid red";
  input_password = document.querySelector("#password").style.borderBottom =
    "1px solid red";
}
