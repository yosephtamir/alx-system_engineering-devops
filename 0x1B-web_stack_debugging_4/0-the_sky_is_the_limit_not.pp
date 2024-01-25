# Nginx is doing under pressure and it turns out it’s not doing well:
# Then we will fix it as below

exec { 'fix--for-nginx':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix--for-nginx']
}
