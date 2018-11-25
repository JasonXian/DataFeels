document.getElementById("searchBtn").onclick = function() {
    var currentLocation = window.location.href;
    for (var i = 0; i  < currentLocation.length; i++) {
        if (currentLocation[i] == "/") {
            break;
        }
    }
    window.location.href = currentLocation.substring(0, i + 1) + "data/recommend/" + document.getElementById("searchQry").value;
}