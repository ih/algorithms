function how_many(number)
    return length(filter(digit -> digit != 0 && number % digit == 0, digits(number)))
end

println(how_many(12345))
println(how_many(661232))
println(how_many(52527))
println(how_many(73000000))
