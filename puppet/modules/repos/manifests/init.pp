class repos{
	file {
        	"/etc/yum.repos.d":
	        source => 'puppet:///files/repos',
	        links => "follow",
		purge => true,
	        recurse => true,
		force => true,
        	}
	}
