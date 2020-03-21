const socket = io();

socket.on('connect', () => {
	socket.emit("connect_event", {data: 'connected'});
	console.log("User connected");
});
