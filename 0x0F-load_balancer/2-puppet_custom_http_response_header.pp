# Automating the task: Creating a custom HTTP header response with Puppet

# Step 1: Update the package list
exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
  creates => '/var/lib/apt/periodic/update-success-stamp',
}

# Step 2: Install Nginx
exec { 'install':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin',
  require => Exec['update'],
}

# Step 3: Configure Nginx to add a custom HTTP header X-Served-By with the servers hostname
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    add_header X-Served-By $hostname;
  }",
  require => Exec['install'],
}

# Step 4: Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
}

# Step 5: Remove the default Nginx site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  require => File['/etc/nginx/sites-available/custom_header'],
}

# Step 6: Restart the Nginx service to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => [File['/etc/nginx/sites-enabled/custom_header'], File['/etc/nginx/sites-available/custom_header']],
}
