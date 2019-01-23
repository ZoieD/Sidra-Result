<!DOCTYPE html>
<html lang="en">
<head>
<title>Home</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Custom Theme files -->
<link href="/public/css/style.css" rel="stylesheet" type="text/css" media="all" />
<!-- //Custom Theme files -->

<!-- web font -->
<link href="http://fonts.googleapis.com/css?family=Montserrat+Alternates:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">
<!-- //web font -->
<!-- jS --> 
<script src="/public/js/jquery.min.js"></script> 
<!-- //js -->
</head>
<body>
	<!-- main -->
	<div class="main-agile">
		<h1>Calculate Result</h1>
		<div class="w3ls-grids">
			<div class="w3ls-right">
				<div class="w3l-dot">
					<div class="w3-heading">
						<h3>It'll be soon{{test}}</h3>
						<h4>OUR WEBSITE</h4>
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
					</div>
				</div>
				<div class="demo2">
					{{ pressure }}{{ impulses }}{{ t0 }}
				</div>
			</div>
			<div class="w3ls-left">
		<div class="login-w3l">	
			<div class="top-img-agileits-w3layouts">
				<h2 class="sub-head-w3-agileits">stay updated</h2>
			</div>			
			<div class="login-form">
				<form action="/calculate" method="post">
					<input type="text" name="n" placeholder="N" required="" />
					<input type="text" name="ll" placeholder="l/L" required="" />
					<input type="text" name="hh" placeholder="h/H" required="" />
					<input type="text" name="lh" placeholder="L/H" required="" />
					<input type="text" name="za" placeholder="Za" required="" />
					<input type="text" name="lra" placeholder="L/Ra" required="" />
					<input type="text" name="w" placeholder="W" required="" />
					<input type="submit" value="Calculate">
				</form>	
			</div>
			<!-- //login -->
				</div> 
				<div class="clear"></div>
			</div>
			<div class="clear"> </div>
		</div>
	</div>	
	<!-- //main --> 
</body>
</html>