#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb 'your_string'"
  exit
end

input_string = ARGV[0]

# Match the word "School" using regex
matches = input_string.scan(/School/)

# Print the matched string or nothing if no match
puts matches.join

