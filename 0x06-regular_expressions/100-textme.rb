#!/usr/bin/env ruby
#This uses a preceeded by method to catch tha sender reciever and flag
puts ARGV[0].scan(/(?<=from|to|flags):(\+?\w+|[-?[01]:?]+)/).join(',')
