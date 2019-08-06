file { '/tmp/holberton':
  content => 'I love Puppet',
  ensure => 'file',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744'
}
