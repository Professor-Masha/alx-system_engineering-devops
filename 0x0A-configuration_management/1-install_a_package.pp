# This Puppet manifest installs Flask version 2.1.0 and Werkzeug version 1.0.1 using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '1.0.1',
  provider => 'pip3',
}

