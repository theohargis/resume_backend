function visitorCounter() {
	fetch("https://412dwkk7sb.execute-api.us-east-2.amazonaws.com/visitorCounter")
		.then(response => response.text())
		.then((body) => {
			document.getElementById("visitor-counter").innerHTML=body
		})
}