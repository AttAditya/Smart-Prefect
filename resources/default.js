// Default JS

const client_id = "1017386686956720168";
const permissions = "1644971949297";
const scope = "bot%20applications.commands";

var bot_invite = "https://discord.com/api/oauth2/authorize";
bot_invite = `${bot_invite}?client_id=${client_id}&permissions=${permissions}&scope=${scope}`;

function select(element) {
	document.querySelector("[selected=true]").setAttribute("selected", false);
	element.setAttribute("selected", true);
}

