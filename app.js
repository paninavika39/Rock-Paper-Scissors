document.getElementById('rock').addEventListener('click', function() {
    play('rock');
});

document.getElementById('paper').addEventListener('click', function() {
    play('paper');
});

document.getElementById('scissors').addEventListener('click', function() {
    play('scissors');
});

function play(choice) {
    fetch('http://localhost:5500/play', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ choice: choice })
	})
	.then(response => response.json())
	.then(data => {
		document.getElementById('server-choice').innerText = 'Server chose: ' + data.server_choice;
		document.getElementById('result').innerText = 'Result: ' + data.result;
	})
}

