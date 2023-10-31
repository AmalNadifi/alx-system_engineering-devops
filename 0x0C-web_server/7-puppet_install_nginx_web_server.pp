# The following script is a Puppet manifest to install and configure Nginx with a 301 redirect

# Installing the Nginx package
package { 'nginx':
  ensure =>installed,
}

# Add a 301 redirect rule to the Nginx configuration
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/AmalNadifi permanent;',
}

# Creating a default HTML page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Setting up the Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Enabling the Nginx site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Defining the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}
