# The limit of requests is changed in Nginx default file
exec { 'increase the uLimit of nginx':
  command => 'sed -i \'s/15/15000/g\' /etc/default/nginx',
  path    => ['/bin']
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin']
}
