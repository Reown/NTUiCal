function abc(){
    document.getElementById("demo").innerHTML = "test";
 };

function parse(){
    var x = document.getElementById("myTextarea").value;
    document.getElementById("parse").innerHTML = x + 1;
}

$('#datepicker').datepicker({
    uiLibrary: 'bootstrap4',
    format: "dd/mm/yyyy"
  });

$(".readonly").on('keydown paste focus mousedown', function(e){
    if(e.keyCode != 9) // ignore tab
    e.preventDefault();
});