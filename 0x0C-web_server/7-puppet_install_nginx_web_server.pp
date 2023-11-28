# Install Nginx web server with Puppet
include stdlib

$locate = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$placeh = "\trewrite ^/redirect_me/$ ${locate} permanent;"

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $placeh,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}
