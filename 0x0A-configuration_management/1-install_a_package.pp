# Install flask 2.1.0

package { 'python3-pip':
  ensure => 'installed',
}

# excutes the installation

exec { 'flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

