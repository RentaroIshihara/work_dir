var nowDate = new Date();
console.log(nowDate);

var year = nowDate.getFullYear();
var month = nowDate.getMonth()+1;
var date = nowDate.getDate();

var today = year + '年' + month + '月' + date + '日';
console.log(today);

/* 曜日追加 */
var day_array = ['日','月','火','水','木','金','土'];
var day = day_array[now.getDay()];

var today = year + '年' + month + '月' + date + '日' + '（' + day + '）';
console.log(today);