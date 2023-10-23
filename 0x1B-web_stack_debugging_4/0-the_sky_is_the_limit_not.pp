# Increase the ulimit for the Nginx server

# Increase the ulimit in the default file
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart the Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['increase-nginx-ulimit'],
}

