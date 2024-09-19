#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: ./100-textme.rb 'log_entry'"
  exit
end

log_entry = ARGV[0]

# Use regex to extract sender, receiver, and flags
if log_entry.match(/from:(?<sender>[^]]+)\] \[to:(?<receiver>[^]]+)\] \[flags:(?<flags>[^]]+)\]/)
  sender = $~[:sender]
  receiver = $~[:receiver]
  flags = $~[:flags]
  
  # Output the required format
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found."
end

