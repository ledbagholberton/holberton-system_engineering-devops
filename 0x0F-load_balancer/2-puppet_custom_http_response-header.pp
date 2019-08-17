#Header HTTP creation
exec {'ensure update':
command => 'usr/bin/apt-get update'
}

-> package {'nginx':
  ensure => 'present'
}

-> file_line {'header':
path => 'etc/nginx/conf/nginx.conf',
match => 'http {',
line => "http {
     	add_header X-Served_By "${hostname}";",
}

-> exec {'restart':
command => 'usr/sbin/service ngnix reload',
command => 'usr/sbin/service nginx restart',
}
