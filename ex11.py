print "How old are you? Only use numbers.",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh? Only use numbers.",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "Your age, %d, times weight, %d, is: %d" % (age, weight, (age * weight))

print "What's your favorite band?",
print "-->",
band = raw_input()
print "You know who sucks? %s sucks." % band
