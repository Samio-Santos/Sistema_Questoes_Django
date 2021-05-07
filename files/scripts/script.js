function mostraSenha() {
    var senha = document.getElementById("password")
    if (senha.type === "password") {
      senha.type = "text";
    } else {
      senha.type = "password";
    }
  }

  // Validador de senha no cadastro

var myInput = document.getElementById("id_new_password1");
var rsenha = document.getElementById('id_new_password2')

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

  rsenha.onkeyup = function() {
    if(myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
  }

  myInput.onkeyup = function() {
    // Validar letra minúsculas
    var lowerCaseLetters = /[a-z]/g;
    if(myInput.value.match(lowerCaseLetters)) {  
      letter.classList.remove("invalid");
      letter.classList.add("valid");
    } else {
      letter.classList.remove("valid");
      letter.classList.add("invalid");
    }
    
    // Valida letras maiúsculas
    var upperCaseLetters = /[A-Z]/g;
    if(myInput.value.match(upperCaseLetters)) {  
      capital.classList.remove("invalid");
      capital.classList.add("valid");
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
    }

    // Valida numeros
    var numbers = /[0-9]/g;
    if(myInput.value.match(numbers)) {  
      number.classList.remove("invalid");
      number.classList.add("valid");
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
    }
    
    // Valida o comprimento
    if(myInput.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
    }
    
    // Verica se as senhas são iguais
    if(myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
    rsenha
  }
}

function openNav() {
  document.getElementById("mySidepanel").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  document.body.style.transition = '1s'
  document.body.style.overflow = "hidden"
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
  document.body.style.backgroundColor = "whitesmoke";
  document.body.style.overflow = "visible"
}

// Função para habilitar o botão caso o usuario preencha todo o formulario
function enableButton(id_pergunta) {
    document.querySelector(`.button${id_pergunta}`).removeAttribute('disabled')
    document.querySelector(`.button${id_pergunta}`).style.cursor = 'pointer'
}

// Funciobalidade com Ajax e Django
// Quando o usuario fizer um comentário este código irá excultar

function x(y) {
  if(document.querySelector(`#question-form${y}`)){
    let form = document.querySelector(`#question-form${y}`);
    function sendForm(event)
    {
      event.preventDefault();
      let data = new FormData(form);
      let ajax = new XMLHttpRequest();
      let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
      ajax.open('POST', form.action);
      ajax.setRequestHeader('X-CSRF-TOKEN',token);
      ajax.onreadystatechange = function()
      {
        if(ajax.status === 200 && ajax.readyState === 4) {
          let alternativa_correta = document.querySelector(`#alternativas_correta${y}`).value
          respondida = false
          var mensagem = document.querySelector(`.mensagem${y}`);
          let resposta_certa = document.getElementsByName("resp").forEach(radio => { 
            if (radio.checked) {
              if (radio.value == alternativa_correta) {
                console.log('Chegou no if')
                mensagem.innerHTML = `
                    <span class="right">Parabéns! Você acertou!</span>
                  `
                document.querySelector(`.button${y}`).disabled = true;
              } else {
                  console.log('Chegou no else')
                  mensagem.innerHTML = `
                      <span class="error">Você errou! <b>Resposta:</b></span> 
                    `
                  document.querySelector(`.button${y}`).disabled = true;
                  
              }
            }
          });
          console.log(resposta_certa) 
        }
      }
      ajax.send(data);
    }
    form.addEventListener('submit',sendForm,false);
  }
}


