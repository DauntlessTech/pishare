var http = require('http');
var userCount = 0;

http.createServer(function (request, response) {
	console.log('New Connection');
	userCount++;

	response.writeHead(200, {'Content-Type': 'text/plain'});
	response.write('Hello!\n');
	response.write('We have had ' +userCount+ ' visits!\n');
	response.end('HELLO WORLD\n');
	
}).listen(3000);

console.log("Server started, hosting at port 8000");
