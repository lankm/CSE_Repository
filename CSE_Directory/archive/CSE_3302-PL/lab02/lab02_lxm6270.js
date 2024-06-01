function scaleTable(input, scale) {
  return input.map(function(num) {return num*scale})
}
function squareTable(input) {
  return input.map(function(num) {return num*num})
}
function tableSelection(scale, pairity) {
  //shorter representation of array found online
  var hundred = Array.from({length: 100}, (_, i) => i + 1);
  
  //pairity=0:even, pairity=1:odd
  pairity%=2;//even/odd -> pairity
  return hundred.filter(function(num){return num%2==pairity&&num%scale==0});
}
function getTotal(inputTable) {
  return inputTable.reduce(function(acc, num){return acc+=num});
}
function cylinder_volume(r) {
  return (h)=>{return 3.14*r*r*h}
}
function makeTag(beginTag, endTag){ 
  return function(textcontent){ 
     return beginTag +textcontent +endTag; 
  } 
}

var inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];     //1
console.log("1) inputTable:     "+inputtable)
var fiveTable = scaleTable(inputtable,5)              //2a
console.log("2a) fiveTable:     "+fiveTable)
var thirteenTable = scaleTable(inputtable,13)         //2b
console.log("2b) thirteenTable: "+thirteenTable)
var squaresTable = squareTable(inputtable)            //2c
console.log("2c) squaresTable:  "+squaresTable)

var oddFives = tableSelection(5,1)//1:odd
console.log("3) oddFives:  "+oddFives)                //3
var evenSeven = tableSelection(7,0)//0:even
console.log("4) evenTevel Sum:  "+getTotal(evenSeven))//4

var v = cylinder_volume(5)(10)
console.log("5) volume(5 10):  "+v)
v = cylinder_volume(5)(17)
console.log("5) volume(5 17):  "+v)
v = cylinder_volume(5)(11)                            //5
console.log("5) volume(5 11):  "+v)

var html = makeTag("<table>\n","\n</table>")(
             makeTag("<tr>\n","\n</tr>")(
              makeTag("<td>","</td>")("123")))
console.log("\n"+html)                                //6
