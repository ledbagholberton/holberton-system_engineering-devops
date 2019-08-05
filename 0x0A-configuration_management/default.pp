$doc_root = "/var/www/example"

exec { 'apt-get update':
 command => '/usr/bin/apt-get update'
}

package { 'apache2':
 ensure  => "installed",
 require => Exec['apt-get update']
}

file { $doc_root:
 ensure => "directory",
 owner => "www-data",
 group => "www-data",
 mode => 644
}

file { "$doc_root/index.html":
   ensure => "present",
   source => "puppet:///modules/main/index.html",
   require => File[$doc_root]
}

file { "/etc/apache2/sites-available/000-default.conf":
   ensure => "present",
   content => template("main/vhost.erb"),
   notify => Service['apache2'],
   require => Package['apache2']
}

service { 'apache2':
   ensure => running,
   enable => true
}
