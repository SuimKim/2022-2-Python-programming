print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "python")
print("%10s" % "python")


print("%d %5d %05d" % (123,123,123))
print("{0:d} {1:5d} {2:05d}".format(123,123,123))

print("{} {} {}".format(10,20,30))
print("{1} {2} {0}".format(10,20,30))
print("{b} {a} {c}".format(a=10,b=20,c=30))