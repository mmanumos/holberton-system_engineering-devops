# This installs a package
package { 'puppet-lint':
  ensure   => '1.1.0',
  name     => 'puppet-lint',
  provider => 'gem'
}
