# This Puppet manifest configures the SSH client to use the private key ~/.ssh/school
# and disables password authentication.

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => @("EOF"),
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  EOF
}

