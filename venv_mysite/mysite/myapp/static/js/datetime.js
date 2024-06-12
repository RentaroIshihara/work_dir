function showClock() {
  let nowTime = new Date();
  let nowHour = nowTime.getHours();
  let nowMin  = nowTime.getMinutes();
  let nowSec  = nowTime.getSeconds();
  let msg = "現在時刻：" + nowHour + ":" + nowMin + ":" + nowSec;
  document.getElementById("realtime").innerHTML = msg;
}
setInterval(showClock, 1000);

function updateEmail() {
  const nameSelect = document.getElementById('name');
  const emailSelect = document.getElementById('email');
  const emailMapping = {
      'sample1': 'ac244701@edu.okinawa-ct.ac.jp',
      'sample2': 'ac244702@edu.okinawa-ct.ac.jp',
      'sample3': 'ac244703@edu.okinawa-ct.ac.jp'
  };
  emailSelect.value = emailMapping[nameSelect.value];
}