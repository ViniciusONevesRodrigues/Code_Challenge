function InvertStr() {
  var input = document.getElementById("desafio1").value;
  var invertedStr = input.split(" ").reverse().join(" ");
  document.getElementById("feedback").innerHTML = invertedStr;
}
