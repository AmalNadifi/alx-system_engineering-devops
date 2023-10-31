# The following script is a Puppet manifest to install and configure Nginx with a 301 redirect

# Installing the Nginx package
package { 'nginx':
  ensure => present,
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

# Setting up the 301 redirect configuration
file { '/etc/nginx/sites-available/redirect':
  ensure  => file,
  content => 'server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 https://www.blog.ehoneahobed.com;
    }

    location / {
        root /var/www/html;
    }
}',
  require => Package['nginx'],
}

# Enabling the redirect site configuration
file { '/etc/nginx/sites-enabled/redirect':
  ensure  => link,
  target  => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect'],
  notify  => Service['nginx'],
}
