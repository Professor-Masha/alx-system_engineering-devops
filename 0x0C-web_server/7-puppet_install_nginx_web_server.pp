class { 'nginx':
  manage_repo => true,
}

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],  # Notify service to restart if this changes
}

# Ensure the default site is enabled
exec { 'enable_default_site':
  command => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

