# Puppet manifest to configure SSH client settings

# Ensure the .ssh directory exists
file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# SSH config file
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => @("END_OF_CONTENT"),
  replace => true,
}

# Add the necessary configuration to the SSH config file
file_line { 'Turn off password auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => 'PasswordAuthentication',
  ensure => present,
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => 'IdentityFile',
  ensure => present,
}

