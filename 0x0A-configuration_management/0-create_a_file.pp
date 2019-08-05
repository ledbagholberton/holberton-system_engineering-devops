$doc_root = '/tmp/holberton'

exec { 'create_file':
  command => '/bin/echo I love Puppet > /tmp/holberton'
}

file { $doc_root:
  ensure => 'file',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744'
}
