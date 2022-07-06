let menu = document.getElementById("menu");
let header = document.getElementById("header");
let logo = document.getElementById("logo");
let lupa = document.getElementById("lupa");
let time_table = document.getElementById("time_table");
let find_input = getComputedStyle(document.getElementById("find_input"));//.getBoundingClientRect();
function header_config(){
	var width = header.offsetWidth;
	var height = header.offsetHeight;
	var poses = 0;
	logo.style.width = height*0.8+"px";
	logo.style.height = height*0.8+"px";

	menu.style.width = height*0.8+"px";
	menu.style.height = height*0.8+"px";
	
	lupa.style.width = 0.35*height+"px";
	lupa.style.height = 0.35*height+"px";
	lupa.style.left = parseInt(find_input.left)-0.35*height+"px";

	time_table.style.width = height*0.8+"px";
	time_table.style.width = height*0.8+"px";
}
console.log("true");
let hm = document.getElementById("hm");
let dmy = document.getElementById("dmy");
function set_time(){
	var now = new Date();
	var time = [now.getDate(),now.getMonth(),now.getFullYear()].map((str)=>{if (str.toString().length<=2){return ("00"+str).slice(-2)}else{return str}}).join(".");
	var time1 =[now.getHours(),now.getMinutes()].map((str)=>("00"+str).slice(-2)).join(":");
	hm.innerHTML = time1;
	dmy.innerHTML = time;
}
set_time();

//let body = getComputedStyle(document);
//console.log(window.outerWidth+"|"+window.outerHeight);
if (window.outerWidth>window.outerHeight){
	header_config();
}else{alert("Not a PC version, mobile version.");}



