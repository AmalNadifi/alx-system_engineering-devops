# Automating the task of updating the package list using Puppet

# Executing the 'apt-get update' command to refresh the package list
exec {'update':
  command => '/usr/bin/apt-get update',
}

# Ensuring the 'nginx' package is present using Puppet
package {'nginx':
  ensure => 'present',
}

# Adding a custom HTTP header 'X-Served-By' with the server's hostname to the 'nginx.conf' file
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',   # Searching for the 'http {' section in the configuration
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",  # Inserting the custom header with the server's hostname
}

# Executing the 'service nginx restart' command to restart Nginx and apply the changes
exec {'run':
  command => '/usr/sbin/service nginx restart',
}
