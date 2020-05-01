function token() {
  var value = document.cookie.match('(^|;) ?' + 'jwt-auth-token' + '=([^;]*)(;|$)');
  return value = value? value[2] : null
}

function cookieInfo() {
  var value = document.cookie.match('(^|;) ?' + 'login_user' + '=([^;]*)(;|$)');
  return value = value? value[2] : null
}




function updateCookie() {
  var value = token()
  if (value !== null) {
      var day = new Date();
      // ms단위기에 1초로 변환->60초->60분->24시간->최종적으로 day
      day.setTime(day.getTime() + (60*60*1000));
      var expires = "expires=" + day.toUTCString();
      document.cookie = 'jwt-auth-token' + "=" + value + ";" + expires + ";path=/" + ";";
      document.cookie = 'login_user' + "=" + cookieInfo() + ";" + expires + ";path=/" + ";";
      return true
  } else {
    return false
  }
}

function cookieCreate(token, user) {
  let d = new Date();                
  d.setTime(d.getTime() + (60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = "login_user=" + user + ";" + expires + ";path=/";
  document.cookie = "jwt-auth-token=" + token + ";" + expires + ";path=/";
}

function logout() {
  var date = new Date();
  document.cookie = 'login_user' + "= " + "; expires=" + date.toUTCString() + "; path=/";
  document.cookie = 'jwt-auth-token' + "= " + "; expires=" + date.toUTCString() + "; path=/";
}

const cookie = {
  token:()=>token(),
  updateCookie:()=>updateCookie(),
  cookieInfo:()=>cookieInfo(),
  logout:()=>logout(),
  cookieCreate:(email, headers)=>cookieCreate(email, headers),
}
export default cookie
