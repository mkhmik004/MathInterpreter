#MKHABELE MMM
#28/06/2023
def main():
    n=input("Expression: ")
    x,y,z=n.split(' ')
    if y=="+":
        solution=float(x)+float(z)
    if y=="-":
        solution=float(x)-float(z)
    if y=="*":
        solution=float(x)*float(z)
    if y=="/":
        solution=float(x)/float(z)

    print(solution)
main()