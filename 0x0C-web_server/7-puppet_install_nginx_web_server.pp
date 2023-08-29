# Install and configure an Nginx server with the following requirements:
# configure
# configure
# configure


package { 'nginx':
      ensure => installed,
}

file_line { 'rewrite redirect':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require => Package['nginx'],
    notify  => Service['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
      content => 'Hello World!',
      require => Package['nginx'],
}

service { 'nginx':
    ensure  => 'running',
    require => file_line['rewrite redirect'],
}
