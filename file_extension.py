print('Input the Filename:')
fn = input()
f_extns = fn.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))