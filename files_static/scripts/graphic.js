// script para grafico de roscar
var ctx = document.getElementById("myChart");
var respostas_certas = document.getElementById("respostas_certas").value;
var respostas_erradas = document.getElementById("respostas_erradas").value;

if (respostas_certas == 0 && respostas_erradas == 0) {
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      datasets: [
        {
          data: [1],
          backgroundColor: ["black"],
          hoverOffset: 4,
          label: "Label",
        },
      ],
      labels: ["Nem uma questão respondida"],
    },
  });
} else {
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      datasets: [
        {
          data: [respostas_certas, respostas_erradas],
          backgroundColor: ["green", "red"],
          hoverOffset: 4,
          label: "Label",
        },
      ],
      labels: ["Total Acertos", "Total Erros"],
    },
    options: {
      responsive: true,
      animation: {
        animateScale: true,
      },
    },
  });
}

// Script para gráfico de linha
if (document.getElementById("myChartBar")) {
  var ctx = document.getElementById("myChartBar");

  var portugues_certas = document.getElementById("portugues_certas").value;
  var portugues_erradas = document.getElementById("portugues_erradas").value;
  var informatica_certas = document.getElementById("informatica_certas").value;
  var informatica_erradas = document.getElementById(
    "informatica_erradas"
  ).value;
  var logica_certas = document.getElementById("logica_certas").value;
  var logica_erradas = document.getElementById("logica_erradas").value;
  var estatistica_certas = document.getElementById("estatistica_certas").value;
  var estatistica_erradas = document.getElementById(
    "estatistica_erradas"
  ).value;
  var direito_certas = document.getElementById("direito_certas").value;
  var direito_erradas = document.getElementById("direito_erradas").value;
  var contabilidade_certas = document.getElementById(
    "contabilidade_certas"
  ).value;
  var contabilidade_erradas = document.getElementById(
    "contabilidade_erradas"
  ).value;
  var criminologia_certas = document.getElementById(
    "criminologia_certas"
  ).value;
  var criminologia_erradas = document.getElementById(
    "criminologia_erradas"
  ).value;

  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "Português",
        "Informatica",
        "Lógica",
        "Estatísca",
        "Direito",
        "Contabilidade",
        "Criminologia",
      ],
      datasets: [
        {
          label: "Acertos",
          data: [
            portugues_certas,
            informatica_certas,
            logica_certas,
            estatistica_certas,
            direito_certas,
            contabilidade_certas,
            criminologia_certas,
          ],
          backgroundColor: ["Green"],
        },
        {
          label: "Erros",
          data: [
            portugues_erradas,
            informatica_erradas,
            logica_erradas,
            estatistica_erradas,
            direito_erradas,
            contabilidade_erradas,
            criminologia_erradas,
          ],
          backgroundColor: ["Red"],
        },
      ],
    },
  });
}
