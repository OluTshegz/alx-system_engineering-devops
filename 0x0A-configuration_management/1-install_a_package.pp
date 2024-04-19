# Using Puppet, install a specific version of flask (2.1.0) from pip3
package {   'python3-pip':
  ensure   => installed,  # Ensure pip3 is installed (adjust if needed)
}

# Install Flask using pip3
package {   'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],  # Ensure pip3 is installed first
}
