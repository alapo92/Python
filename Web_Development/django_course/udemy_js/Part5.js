var hot = false
var temp = 40
temp = 75
// temp = 30

if (temp > 80){
    console.log("Hot outside!")
} else if(temp <= 80 && temp >= 50){
    console.log('Nice outside!')
} else if(temp <= 50 && temp >= 32){
    console.log("Its cooler outside!")
} else{
    console.log("Its really cold outside!")
}

var ham =10;
var cheese = 10;

var report = "blank";

if (ham >= 10 && cheese >= 10){
    report = "Strong sales of both ham and cheese!"
} else if (ham === 0 && cheese === 0){
    report = "Nothing Sold!"
} else{
    report = "We had some sales of items"
}

console.log(report);