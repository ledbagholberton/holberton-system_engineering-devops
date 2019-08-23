#Header HTTP creation
exec {'ensure update':
command => 'usr/bin/apt-get update'
}

-> package {'nginx':
  ensure => 'installed'
}

-> file_line {'header':
path => 'etc/nginx/nginx.conf',
match => 'http {',
line => "http {\n\tadd_header X-Served-By ${hostname};",
}

-> exec {'start':
command => 'usr/sbin/service nginx restart',
}
