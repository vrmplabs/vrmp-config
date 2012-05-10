class cassandra{
	package	{"dsc":
        	ensure => present,
        }
	exec { "echo 'dsc by puppet' > /tmp/puppet_install_dsc":
	path => ["/bin", "/usr/bin", "/usr/sbin"]
	}

}
