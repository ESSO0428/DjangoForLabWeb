/*For fix table title , need to add thead tag wrap title(th tag) */
/*and <!DOCTYPE html>*/
/*<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>*/

// <script>
/*  reference trash 

	// document.documentElement.scroll(
	var newtag = document.createElement("BR"); 
	//var newContent = document.createTextNode("Hi there and greetings!"); 
	//document.body.insertBefore(newtag, currentDiv); 
	var table = document.getElementsByTagName("table")[0];  
	//or// var table = $("table")[0];
	
	// document.body.insertBefore(newtag, table); 
	//O//
	var thead = table.getElementsByTagName("thead");
	//R//
	// document.body.insertBefore(newtag, thead[1]); 
	// document.body.insertAfter(newtag, thead[0]); 
*/
		/*create src jquery but can't usful the js file jquery*/
		// var script = document.createElement('script');
		// script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js';
		// script.type = 'text/javascript';
		// document.getElementsByTagName('head')[0].appendChild(script);
		// var head = document.getElementsByTagName('head')[0];
		// var src = head.getElementsByTagName("script");
		// head.insertBefore(script, src[0]); 
	
	  // $(document).ready(function(){ 
	function adjust_table() {
		var wind = document.body.clientWidth;
		var p = $("table").position();
		var p = p.left;
		var TitleHeight = $("thead").height();
		$("thead").css({position: "fixed", top:0});
		if ($("table").width() > wind) {
			$("thead").css({position: "fixed", right:0-($("table").width()-wind)});
		}else{
			$("thead").css({position: "fixed"});
			$("thead").css({ 'right' : '' });
		}
		$("thead").css({position: "fixed", left:p});
		$("table").css({position: "absolute", top:TitleHeight});
		window.addEventListener("scroll", myFunction);
		function myFunction() {
			/*developer's kit*/
			// var p = document.createElement('p');
			// p.id = 'demo';
			// document.body.appendChild(p);
			// $("#demo").css({position: "fixed" , top:150});
			// $("#demo").css({border: "solid"});
			var x = document.documentElement.scrollLeft;
			var y = document.documentElement.scrollTop;
			// document.getElementById ("demo").innerHTML = "Horizontally: " + x + "px<br>Vertically: " + y + "px" + "px<br>table: " + $("table").width()+"<br>thead hight: " + TitleHeight + "px";
			
			
			// var x = document.documentElement.scrollLeft;
			// var y = document.documentElement.scrollTop;
			
			
			 // $("body").append("<p>test</p>");
			 
			var wind = document.body.clientWidth;
			if ($("table").width() > wind) {
				$("thead").css({position: "fixed", right:0-($("table").width()-wind)});
			}else{
				$("thead").css({position: "fixed"});
				$("thead").css({ 'right' : '' });
			}
			$("thead").css({position: "fixed", left:p-x});
		}
	}
	$(window).ready(function(){ 

		// $("<Br>").insertAfter("thead");
		
		adjust_table();
		
	}
	);
	window.onresize = function(){
		adjust_table();
	}
		// </script>