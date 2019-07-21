#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)(\+?[\d]{11})?([A-Za-z]+)?(((.?[0-1].){4})(.?[0-1]))?/).join(",")
